# Quadratic covers, projected thickenings and conductor descent

**Scope.** Fix the smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), over an algebraically closed field. Characteristic zero is the default; every positive-characteristic statement below identifies its extra hypotheses. Characteristic-zero STCI remains open.

This chapter asks which multiple structures and intersections with this
support can arise from actual homogeneous equations, and what projection
and conductor constructions produce. The explicit power sources give
real embedded thickenings whose projected section rings can be tested. A
primary lift of an arbitrary supported pair has different hypotheses and
need not be Gorenstein. Failures of the explicit sources therefore retain
their source-specific scope.

For any pair in the separated quadratic-cover setting, the full conductor
scheme carries both local gluing and global postulation data. The canonical
and norm bounds describe necessary geometry for a realization, including
its infinitesimal endpoint structure. Conversely, an embedded AG conjugate
union would descend to the required complete intersection. These conditions
and the automatic descent criterion leave a concrete construction problem;
they do not presume that no such intersection exists.

## 1. What the natural birational transport can and cannot do

Write B=Bl_C(P3), with H the pullback of a plane and E exceptional.
The second contraction identifies B with the blowup of a conic in V5;
its hyperplane class is L=3H−E. This precise quartic is covered by
[Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).
The [blowup residual account](../residuals/blowup_residual_geometry.md) retains the equation dictionary.

**Uniform source boundary.** Every birational morphism B→P3 is the
original contraction followed by a projective automorphism. Indeed,
Pic(B) has integral basis H,L, and its two nef boundary rays are H,L.
If D is the pullback of O_P3(1) under such a morphism, it is nef with
D³=1. It is not ample, since an ample pullback would make the morphism
finite, hence an isomorphism to the normal target, contradicting
Picard rank two. Thus D=nH or nL for an integer n>0. But

    H³=1, H²E=0, HE²=−4, E³=−14, L³=5.

Only D=H works, and h0(B,H)=4 proves the assertion. Consequently a
nontrivial Cremona proposal cannot be resolved by this reduced-curve
blowup alone. It must specify additional centers or another resolution,
and the effect of those changes on its defining equations.

There is nevertheless a concrete transport of a genuinely thick CI.
In coordinates [a:b:c:d], let

    Φ=[ab:b²:ac:ad],       Ψ=[y0²:y0y1:y1y2:y1y3].

These are mutually inverse rational maps, and Φ sends C generically
onto the twisted cubic D=[s3:s2t:st2:t3]. The latter has the supported
complete intersection

    Q=y0y2−y1²,   G=y2³−2y1y2y3+y0y3²,

of generic multiplicity two. Pullback and removal of the full surface
factors give

    Φ*Q=b f0,  Φ*G=a² h0,
    f0=a²c−b³,  h0=ac³−2b²cd+abd².

The exact remaining cycle is

    [V(f0,h0)]=2[C]+3[ℓ]+[M],
    ℓ=V(a,b),       M=V(b,c).                         (1)

On ab≠0, substitution c=b³/a² gives
h0=(b/a5)(a³d−b4)², proving multiplicity two along C. At a general
point of ℓ, h0 solves a=(2d/c²)b²+O(b³), and f0=−b³+O(b4),
giving multiplicity three. At M, h0 is b times a unit modulo f0,
giving multiplicity one. On a=0 or b=0 the equations allow precisely
these lines. The cycle degrees 8+3+1=12 exhaust the CI degree.
Here ℓ is the tangent at p_infinity, and M is the endpoint secant.

Thus actual transverse thickness survives this transport, but four
units of genuine residual degree remain on specified lines. Removing
exceptional surface factors has not removed these curves. Keeping the
irreducible cubic f0 cannot succeed with any mate, by the inherited
cubic exclusion recorded in [R-0001](../../results/quartic_carrier_exclusion.md).
This control does not select an enumeration of Cremona transforms or
corrections on that fixed carrier. The primary
[Cremona linearization constructions, §§1–2](https://people.math.osu.edu/cueto.5/CremonaLinearizations.pdf)
concern ambient equivalence at the generic points of reduced varieties;
they do not supply the missing supported-CI correction.

## 2. Global Cohen–Macaulayness is a substantive compatibility condition

[Singh–Walther, Example 3.5 and Question 3.6](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf),
published in 2007, explicitly use k[s4,s3t,st3,t4] and ask whether in
characteristic zero its defining ideal has the same radical as an
ideal with Cohen–Macaulay quotient. The question does not require that
ideal to be homogeneous. This is the historical formulation in that paper; no claim about the current literature's resolution status follows from citing it.

An embedded ACM thickening supported on C would answer its homogeneous
version. It need not be a CI. An embedded arithmetically Gorenstein
thickening in P3 would be a CI: a perfect height-two ideal of type one
has two generators by Hilbert–Burch. Local Gorensteinness alone supplies
neither conclusion.

Two automatic operations do not cross this boundary. First, a scheme
spanning P^N, N>3, that projects isomorphically to P3 keeps at least
N+1 sections of its polarization. Its image therefore fails linear
normality and is not ACM. The AG double constructions in
[Notari–Ojeda–Spreafico, Theorems 4.4 and 4.6](https://arxiv.org/pdf/0812.2578)
have the stated rational-normal embeddings; for degree four the relevant
ambient spaces are P4 and P7, not the fixed projected P3. Nonisomorphic
projections are outside the preceding argument.

Second, for a local ring A and a nonzero finite module K,

    edim(A ⋉ K)=edim(A)+dim_k(K/m_A K).

This follows from (m_A⊕K)²=m_A²⊕m_A K. In particular canonical
idealization of an ACM cone of embedding dimension four has embedding
dimension 4+type(A)>4. It is not a quotient of the fixed four-variable
coordinate ring. For a ring not known CM, replace type by μ(ω_A)
and do not call this idealization automatically Gorenstein. Nontrivial
canonical extensions and embedded Ferrand constructions are not excluded;
[Manolache, *Linkage Extensions*, introduction and §2](https://imar.ro/journals/Revue_Mathematique/pdfs/2007/4/manolache.pdf)
explicitly distinguishes abstract extensions from embedded ones.

These are source boundaries, not an exclusion of all ACM or AG
thickenings. A new operation must retain the actual four-coordinate
image while controlling its global deficiency.

## 3. An actual projection source with prescribed reduced support

Put S=k[a,b,c,d], T=S[z], r=2bc−ad, and

    f=b²−az,       g=c²−dz,       h=z²−r.

Their common reduced support is the rational normal quartic
D=[s4:s3t:s2t2:st3:t4] in P4. On z=0 the equations give b=c=0,
ad=0, exactly the endpoints. On z≠0, eliminating a,d gives
(z²−bc)²=0 and hence the usual rational-normal ratios. They form a
regular sequence, with cycle 2D. This classical three-quadric
construction is also described in
[Torrente's 2015 primary abstract](https://unige.iris.cineca.it/handle/11567/809282);
the direct verification here does not rely on access to the full chapter.

For arbitrary positive u,v, take the actual AG complete intersection

    W_uv=V(h,f^u,g^v),   B_uv=T/(h,f^u,g^v).

Projection forgetting z is finite because h is monic. Its scheme image
Y_uv has homogeneous coordinate ring A_uv=image(S→B_uv), and reduced
support exactly C. Thus support is supplied by a construction, not
assumed as a final condition on unknown equations. The smooth quadric
threefold h=0 is a double cover of P3 branched over r=0. Its involution
z↦−z sends D to another lift of C, meeting D only at the endpoints.
Projection is generically an isomorphism on the full W_uv, as the
explicit conductor calculation below proves; it can change the scheme
at the endpoints. Étaleness alone is not used as a descent argument.

As a finite graded S-module, B_uv has dimension and depth two. In
0→A_uv→B_uv→M_uv→0, local cohomology therefore gives

\[
H^1_{S_+}(A_{uv})\simeq H^0_{S_+}(M_{uv}).              \tag{2}
\]

The elimination ideal is saturated: A_uv⊂B_uv has no irrelevant
torsion. Thus Y_uv is ACM exactly when M_uv has no irrelevant torsion.
Geometrically M_uv records source functions that fail to be generated
by the four retained coordinates. Its irrelevant torsion is the part
still obstructing the completeness of the projected linear series.

Reduction modulo z²=r writes

    f^u=P_u+Q_u z,      g^v=R_v+T_v z.

The S-module B_uv has generators 1,z. The coefficient relations of
f^u,zf^u,g^v,zg^v show that

\[
M_{uv}\simeq(S/K_{uv})(-1),\qquad
K_{uv}=(P_u,Q_u,R_v,T_v).                              \tag{3}
\]

Consequently the entire two-parameter source has the precise test

    Y_uv is ACM  ⇔  K_uv is saturated.                (4)

This is an exact structural interface for this explicit source. It does not assert that arbitrary ACM thickenings arise this way.

## 4. Uniform obstruction: the projected image is never AG

**Theorem.** For every pair of positive integers u,v, Y_uv is not
arithmetically Gorenstein and hence is not a scheme-theoretic complete
intersection in P3. If u≥2, Y_uv is not locally Gorenstein at
p_a=[1:0:0:0]; if v≥2, the same holds at p_d=[0:0:0:1].
The remaining Y_11 fails ACM. This does not assert that the common
reduced support C is not a set-theoretic complete intersection.

We first identify the conductor of A⊂B, suppressing u,v. Every element
of B is represented by p+qz, p,q∈S. By (3), it belongs to A exactly
when q∈K. Since B is generated as an A-module by 1,z, it belongs to
the conductor precisely when both it and its product with z belong to
A. The latter product is qr+pz. Therefore

\[
\mathfrak c=\{\beta\in B:\beta B\subset A\}
=KB=(Q_u,T_v)B.                                      \tag{5}
\]

The last equality uses P_u=−Q_u z and R_v=−T_v z in B.
This computation does not first assume birationality. On D away from
the endpoints,

    Q_u|D=−2^(u−1) a^u z^(u−1) ≠0.

Since Q_u B⊂A and Q_u∈A is generically a unit, A=B there, including
the entire nilpotent structure. Both rings are pure one-dimensional
locally along the projective curve: B is a CI, and a local parameter
nonzero on its reduced support is also a nonzerodivisor on A⊂B.
Thus they share the total quotient ring.

Suppose u≥2 and work on a=1. Eliminate d=2bc−z². The source local
ring at the endpoint is

\[
B_p=\bigl(k[b,c,z]/(f^u,g^v)\bigr)_{(b,c,z)},\quad
f=b^2-z,\quad g=c^2-2bzc+z^3.
\]

We prove that both generators of (5) are necessary.

First, Q_u is not in (T_v,f^u,g^v). Specializing c=z=0 sends this
ideal to (b^(2u)) in k[b], whereas Q_u maps to
−u b^(2u−2), nonzero in k[b]/(b^(2u)). This test is local at the
endpoint as well: every denominator with nonzero constant term remains
a unit in that Artinian local quotient.

For the other generator set

\[
R_u=k[b,z]/\bigl((b^2-z)^u,Q_u(b,z^2)\bigr).
\]

This is Artinian local. Indeed

    2z Q_u=(b²−z)^u−(b²+z)^u

makes both b²−z and b²+z nilpotent in R_u, hence b,z nilpotent.
Moreover b is nonzero: when u≥2, both defining polynomials belong
to (b,z)². In R_u[c], g^v is monic of c-degree 2v, whereas the
coefficient T_v, after substituting d=2bc−z², is

\[
T_v=-\sum_{\substack{1\le j\le v\\j\text{ odd}}}
\binom vj c^{2v-2j}(2bc-z^2)^jz^{j-1}.
\]

It has c-degree 2v−1 and nonzero leading coefficient −2v b.
Division by the monic polynomial g^v therefore leaves T_v as a
nonzero remainder. Hence T_v is not in (Q_u,f^u,g^v).
There is no loss on localization: R_u[c]/(g^v) is Artinian local,
since modulo the maximal ideal of R_u it is k[c]/(c^(2v)).

The conductor thus has exactly two minimal generators over B_p and
is not principal. If the target local ring A_p were Gorenstein, finite
duality would identify Hom_(A_p)(B_p,A_p) with the canonical module of
B_p, which is a free rank-one B_p-module. The Hom module is the
conductor ideal: the rings are finite birational with the same total
quotient ring, so such homomorphisms are multiplication by elements
of the conductor. It would be principal, a contradiction.

This is the standard conductor consequence of
[finite duality, Stacks Tag 0AX0](https://stacks.math.columbia.edu/tag/0AX0),
also stated before Proposition 2.9 of
[Piene, *Polar classes of singular varieties*](https://www.numdam.org/item/10.24033/asens.1346.pdf).
The local canonical-module argument here retains the full nonreduced
schemes; no reduction to their underlying smooth curves is made.

The involution exchanging a,d and b,c exchanges u,v and the endpoints,
proving the assertion when v≥2. Finally, when u=v=1,

    K_11=(a,d,b²,c²).

Thus B_11/A_11 is nonzero and entirely irrelevant torsion. Equation
(2) proves that Y_11 is not ACM. This completes the uniform proof.


The coefficient/conductor calculation generalizes to any quadratic
algebra S[z]/(z²−r) with two imposed relations P+Qz and R+Tz.
Its source/image cokernel B/A is S/(P,Q,R,T), up to the grading twist, and its
conductor is (Q,T) in the source. When the map is finite birational
and source and target are Gorenstein, that conductor must be invertible.
The characteristic-zero nonmembership proof is specific to the displayed
power source; no arbitrary-curve or arbitrary-projection exclusion follows.

There is also a bounded characteristic comparison. The same exclusion
proof works over an algebraically closed field of characteristic p
when p does not divide 2uv. Its essential coefficients are 2, u and
2v. In contrast, take odd p and u=v=n=p^e, e≥1. Frobenius gives

    P=b^(2n), Q=−a^n r^((n−1)/2),
    R=c^(2n), T=−d^n r^((n−1)/2).

The homogeneous cone conductor is r^((n−1)/2)(a^n,d^n)B.
On the projective source W_nn, a,d have no common zero on its
support D, so the conductor sheaf is exactly

    c_(W/Y)=r^((n−1)/2) O_W.

It is an effective Cartier ideal: W is a pure CI and r is nonzero
at its generic support point, hence a nonzerodivisor. Thus Frobenius
makes this precise endpoint non-Cartier obstruction disappear. By
itself this does not establish that the image is locally Gorenstein,
ACM, AG or a CI; invertibility of the conductor was used as a necessary
condition, not a sufficient one. The next section extracts a further global
consequence of the same formula, without a new exponent search.


The [uniform projected-section obstruction](projected_thickening_section_defects.md) gives a stronger result for this source: every power image, and every homogeneous binary mixture in the stated source, fails ACM when \(uv\ne0\) in the field. It exhibits an actual missing ambient section and Rao lower bounds \(1,2,1\) in three specified degrees. All positive degrees in characteristic zero are covered; characteristic-divisible degrees are not. The proof needs neither a generic-birational projection nor a Gorenstein image. Its actual source-ring comparison does not apply to arbitrary primary lifts, and it does not decide the ACM status of the odd-Frobenius family considered next.

## 5. Frobenius images: global adjunction in odd characteristic and CI images in characteristic two

Keep the same family with u=v=n. First take odd characteristic p and
n=p^e, e≥1. Although the preceding conductor computation proves that the projective conductor is
Cartier, its degree still rules out a complete-intersection image.

Suppose Y_nn were a CI of surface degrees α,β. Projection is generically
an isomorphism on the full schemes, so

    αβ=deg Y=deg W=8n².

The source is a CI of degrees (2,2n,2n) in P4, hence
ω_W=O_W(4n−3). The conductor sheaf is O_W(1−n), and projection
preserves the hyperplane bundle. Finite duality for the hypothetical
Gorenstein image gives

\[
\omega_W=\mathfrak c\otimes\pi^*\omega_Y
=\mathcal O_W(\alpha+\beta-n-3).
\]

Restriction to D≅P1, where O_W(1) has degree four, forces
α+β=5n. These are equalities of integer degrees, not elements of the
ground field. They are incompatible with αβ=8n², since

    (α−β)²=(5n)²−4(8n²)=−7n²<0.

Thus these odd-Frobenius images also fail to be AG/CI. The argument
does not decide their local Gorensteinness or ACM property. It shows
why the Cartier conductor condition alone was insufficient: its global
twist must also match the degree and canonical class of the image.

Now take characteristic two and n=2^e, e≥1. Here h=z²+ad and
Frobenius makes both remaining equations lie in S itself:

\[
F=b^{2n}+a^{3n/2}d^{n/2},\qquad
G=c^{2n}+a^{n/2}d^{3n/2}.
\]

Consequently

    B=(S/(F,G))[z]/(z²+ad),   A=S/(F,G).

The inclusion of A is injective because the extension is monic.
Moreover F=(b4+a³d)^(n/2) and G=(c4+ad³)^(n/2). These are
the powers of the known characteristic-two quartic pair in the
[positive-characteristic construction record, §3](../arithmetic/positive_characteristic_constructions.md).
Directly, on a≠0 the first quartic gives d=b4/a³; the second gives
c4=b12/a8 and hence c=b³/a², by injectivity of Frobenius over the
field. On a=0, they force b=c=0, leaving the other endpoint. Thus
the radical is exactly I_C, and F,G are a proper regular sequence.

The actual image is a CI of degrees (2n,2n), degree 4n². The
projection W→Y is finite flat radicial of rank two, and deg W=8n².
It is an isomorphism on the reduced curves but not on their full
generic nilpotent structures. There is no degree-two extension of their
reduced function fields. Hence the birational conductor argument used
above does not apply. The characteristic-two quadric h=0 is singular
along a=d=z=0, disjoint from D; the CI source remains well defined.

This recovers an already known positive-characteristic construction;
the new extraction is its place in the same projection operation and
the distinction between non-Cartier conductor, incompatible global
canonical degree, and finite flat nilpotent projection. It supplies
no characteristic-zero construction or unrestricted nonexistence proof.

## 6. The entire hypothetical intersection and its separated branches

Write \(S=k[a,b,c,d]\),
\[
E=S[z]/(z^2-r),\qquad r=2bc-ad,\qquad Q_3=\operatorname{Proj}E.
\]
The projection \(\pi:Q_3\to\mathbf P^3\) is finite flat of degree two,
with involution \(\sigma(z)=-z\). Its inverse image of C has reduced
branches
\[
D=[s^4:s^3t:s^2t^2:st^3:t^4],\qquad D^-=\sigma D,
\]
where the coordinates in this display are \([a:b:z:c:d]\).
They meet at \(p_a=[1:0:0:0:0]\) and \(p_d=[0:0:0:0:1]\),
with intersection length two at each point.

Suppose \(Y=V(F_\alpha,G_\beta)\subset\mathbf P^3\) is a complete
intersection with \(Y_{\mathrm{red}}=C\), and put
\[
m=\alpha\beta/4,\qquad e=\alpha+\beta-4,\qquad A=S/(F_\alpha,G_\beta).
\]
Extract the full D-primary component W of \(\pi^{-1}Y\); its conjugate
is the full other primary component. The inverse image is a complete
intersection of degrees \((2,\alpha,\beta)\), hence has no embedded
components. W is pure and locally Cohen–Macaulay. Let B be its saturated
homogeneous coordinate ring, viewed as a finite S-algebra.

The inclusion \(A\hookrightarrow B\) is birational on the **full
generic Artin algebras**, not only on the reduced curves. Indeed r is a
unit generically on C and its two roots are distinct; its square root
lifts uniquely through the nilpotent generic algebra on either chosen
branch. Thus the quadratic algebra splits there. Away from the two
endpoints the same splitting holds locally. Purity then gives the
inclusion globally. Moreover \(B=A+Az\), with \(\deg z=1\).

Do not assume B is Cohen–Macaulay at its cone vertex, or that W is
locally Gorenstein. Neither assertion follows from the extraction.

## 7. The conductor and the actual quadratic boundary

Let \(\mathfrak c=\{q\in A:qB\subset A\}\), an ideal in both rings.
Finite birationality identifies it with \(\operatorname{Hom}_A(B,A)\).
Put \(T=A/\mathfrak c\). Multiplication by z gives the exact graded
sequence
\[
0\longrightarrow A\longrightarrow B\longrightarrow T(-1)
\longrightarrow0.                                                    \tag{1}
\]
In fact \(qz\in A\) if and only if \(q\in\mathfrak c\), since
B is generated by 1 and z. The associated projective boundary
\(\Delta=\operatorname{Proj}T\) is supported at the two endpoints.
Write \(\delta_p=\ell((\pi_*\mathcal O_W/\mathcal O_Y)_p)\) and
\(\delta=\delta_{p_a}+\delta_{p_d}=\ell\Delta\).

At an endpoint, use local rings \(A_p\subset B_p\) and temporarily
trivialize the degree-one twist. The ring \(A_p\) is one-dimensional
Gorenstein and \(B_p\) is maximal CM over it. Dualizing (1) locally
therefore identifies
\[
A_p/\mathfrak c_p
\simeq \operatorname{Ext}^1_{A_p}(B_p/A_p,A_p)
\simeq (B_p/A_p)^\vee.
\]
Together with \(B_p/A_p\simeq A_p/\mathfrak c_p\), this proves that
\(A_p/\mathfrak c_p\) is Artinian Gorenstein. Also
\(\ell(B_p/\mathfrak c_p)=2\delta_p\). The evident surjection from
the quadratic algebra has equal lengths, so
\[
\boxed{\quad B_p/\mathfrak c_p
\simeq (A_p/\mathfrak c_p)[z]/(z^2-r).\quad}                           \tag{2}
\]
Globally the quadratic algebra has underlying module
\(\mathcal O_\Delta\oplus\mathcal O_\Delta(-1)\).

Thus the conductor boundary downstairs is itself locally Gorenstein,
and its boundary upstairs is the prescribed quadratic pullback. This
strengthens the general self-orthogonal half-algebra description in
the tropical-conductor note. It does **not** make T arithmetically
Gorenstein or make \(\mathfrak c\) invertible on W.

The standard input is finite duality, including nonreduced rings:
[Stacks, Lemma 47.15.8](https://stacks.math.columbia.edu/tag/0AX0).

## 8. Attachment and a global lower bound on boundary length

For \(H=W\cap W^-\), the attachment ideal on W is
\[
I_{H/W}=z\mathfrak c.                                                 \tag{3}
\]
One way to see this is to write an equation of W as \(p+zq\).
Its conjugate restricts to \(-2zq\) on W. The possible q are exactly
the conductor elements. Since z is regular on W and has order two
on its reduced branch at each endpoint,
\[
\ell H_p=\ell(B_p/zB_p)+\ell(B_p/\mathfrak c_p)
=2m+2\delta_p,
\qquad \ell H=\alpha\beta+2\delta.                                   \tag{4}
\]
The total attachment/genus relation is bookkeeping; it is not by
itself an additional obstruction or a positive residual degree.

There is a distinct **graded** consequence. Since A is CM of dimension
two and B is saturated, (1) gives \(H^0_{\mathfrak m}(T)=0\).
Consequently T, when nonzero, is a one-dimensional standard graded
CM ring, with no irrelevant torsion. It is nonzero: W spans P4 and Y
spans P3, so \(\dim(B_1/A_1)=1\). The absence of irrelevant torsion
then ensures a nonempty projective boundary, rather than a quotient
concentrated only at the cone vertex.

Apply \(\operatorname{Ext}_S^\bullet(-,S(-4))\) to (1).
The canonical module of A is A(e); that of T is
\(\omega_T=\operatorname{Ext}^3_S(T,S(-4))\). The result contains
\[
0\to\omega_B\to A(e)\to\omega_T(1)
\to\operatorname{Ext}^3_S(B,S(-4))\to0.                              \tag{5}
\]
Here \(\omega_B=\operatorname{Hom}_A(B,A(e))=\mathfrak c(e)\).
The last module has finite length because B is CM away from its vertex.
In particular (5) supplies an injection
\[
\boxed{\quad T(e-1)\hookrightarrow\omega_T\quad}                     \tag{6}
\]
with finite-length cokernel. No ACM hypothesis on B is used.

Let \(h_0,\ldots,h_s\) be the h-vector of T, obtained by reducing
modulo a regular general linear form. Then
\(\operatorname{indeg}\omega_T=1-s\). The degree \(1-e\) element
of \(T(e-1)\) is nonzero, so (6) forces \(s\ge e\).
A standard graded Artinian algebra has no internal zero in its
h-vector: a zero graded piece makes all higher pieces zero. Thus
\(h_i\ge1\) for \(0\le i\le s\), and
\[
\boxed{\quad \delta\ge e+1=\alpha+\beta-3.\quad}                     \tag{7}
\]

The full restriction-function inequality is slightly stronger. Put
\(H_\Delta(n)=\dim_k T_n\), with zero in negative degrees. This is
the dimension of restrictions of ambient forms, **not** the dimension
of all sections of \(\mathcal O_\Delta(n)\). If \(\ell\) is a regular
linear form, the free graded \(k[\ell]\)-module decomposition is
\(T=\bigoplus_i k[\ell]\bigl(-i\bigr)^{h_i}\). Its canonical dual has summands
\(k[\ell]\bigl(i-1\bigr)^{h_i}\), giving
\(\dim_k(\omega_T)_j=\delta-H_\Delta(-j)\). Thus (6) gives
\[
H_\Delta(n)+H_\Delta(e-1-n)\le\delta
\quad\hbox{for every integer }n.                                    \tag{7a}
\]

This is the classical canonical-module mechanism behind
Cayley–Bacharach Hilbert-function inequalities; compare
[Kreuzer, §1 and Theorem 2.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7DC79E96BB5A7CBA61D74E9F5835E927/S0008414X00045843a.pdf/div-class-title-on-the-canonical-module-of-a-0-dimensional-scheme-div.pdf).
Here the CI twist and the degree-one extra generator fix the degree
of a faithful canonical element. If s=e, it is in the initial
canonical degree and the maximal-degree Cayley–Bacharach criterion
applies. If s>e, this argument does not establish that stronger
maximal-degree property. Formula (7a) follows directly from (6).

Geometrically, the missing fifth linear section on Y becomes regular
on the separated branch W. Its failure to descend is concentrated at
the marked endpoints. The canonical grading of an actual two-equation
intersection forces that boundary to retain postulation through degree
at least \(\alpha+\beta-4\). Its length must therefore grow with the
sum of the equation degrees. This is an unrestricted necessary
condition, not an upper bound on the available endpoint defect.

The proof of (6)–(7) generalizes to a nontrivial finite birational graded
extension of any nondegenerate complete-intersection curve in P3,
with \(B=A+Aw\) as an **A-module**, where \(\deg w=1\), provided B
is saturated and locally CM away from the vertex and the quotient has
finite projective support. Algebra generation by one integral element
alone is insufficient: its higher powers could require more module
generators. This graded extension statement is characteristic free.
The special quartic fixes where the boundary occurs and ensures the
extension is nontrivial.

All quadratic-cover steps above require only that 2 be invertible:
the generic roots are simple, the full nilpotent algebra splits into
the two branches, and conjugation separates even and odd parts.
Thus (7) also applies in odd characteristic and contains no mechanism
specific to characteristic zero. In characteristic two this cover
does not separate the branches, so its application here is unavailable.

## 8.1. Ambient quadratic norms force conductor postulation

**Independently reviewed theorem.** The actual ambient equation
degrees add a norm constraint to the canonical Hilbert-function inequality
(7a). This uses the separated quadratic extension of §§6–8.
Order the defining degrees as \(5\le\alpha\le\beta\); the lower bound
five uses the accepted characteristic-zero low-carrier exclusions and
factor reduction, including
[STCI-R-0001](../../results/quartic_carrier_exclusion.md).
Put
\[
q=\left\lceil\frac{\alpha}{2}\right\rceil-1,\qquad
L_q=\binom{q+2}{3}.
\]
Let \(J_\Delta\subset S\) be the inverse image of \(\mathfrak c\)
under \(S\to A\), so \(T=S/J_\Delta\). The earlier vanishing
\(H^0_{\mathfrak m}(T)=0\) makes this the saturated ideal of the
actual projective boundary.

**Theorem.** Every supported complete-intersection pair of §§6–8 in
characteristic zero, with the ordered degrees above, satisfies
\[
(J_\Delta)_d=0\quad(0\le d<q),                                    \tag{7b}
\]
and
\[
\boxed{\quad
\delta\ge\alpha+\beta-3+
2\left[\binom{q+2}{3}-q\right].
\quad}                                                           \tag{7c}
\]
This strengthens (7), uniformly in both degrees and without a
carrier-normality, generic-normal-order or local-type hypothesis.
It is a new consequence of (7a) and the norm input below, not a
second independent duality budget. No optimality claim is made.

**Proof.** Take \(0\ne h\in(J_\Delta)_d\), with \(d<q\). Since \(d<\alpha\),
h has a nonzero class in A. Conductor membership means that
\(hz\in A_{d+1}\). Choose a homogeneous polynomial
\(P\in S_{d+1}\) representing it. In B,
\[
P^2-rh^2=0,\qquad r=2bc-ad.
\]
The injection \(A\hookrightarrow B\) implies
\[
P^2-rh^2\in(F_\alpha,G_\beta).
\]
This is a nonzero polynomial. Otherwise \(r=(P/h)^2\) in
\(\operatorname{Frac}S\), whereas the irreducible quadratic r has
odd valuation at its prime divisor and is not a rational square.
The argument divides only in the fraction field of the polynomial
ring S; h may be nilpotent in A. The fact that r becomes a square
on the reduced curve is irrelevant to this nonvanishing.

Its degree is \(2d+2\le2q<\alpha\), contradicting the least degree
of a nonzero element of \((F_\alpha,G_\beta)\). This proves (7b).
All representatives were taken in the actual graded rings. No
replacement of B by a full section ring was made.

Consequently
\[
H_\Delta(n)=\binom{n+3}{3}\quad(0\le n<q),\qquad
H_\Delta(q-1)=L_q.
\]
Reduce T by a regular general linear form. Its h-vector has
\(h_i=\binom{i+2}{2}\) for \(i<q\), and the earlier canonical
injection gives \(s\ge e=\alpha+\beta-4\). Since there are no
internal zeros, \(h_i\ge1\) for \(q\le i\le e\). Also
\(e-q\ge q-1\), because \(\beta\ge\alpha\ge5\). Therefore
\[
H_\Delta(e-q)\ge L_q+e-2q+1.
\]
Apply (7a) at \(n=q-1\):
\[
\delta\ge H_\Delta(q-1)+H_\Delta(e-q)
       \ge2L_q+e-2q+1,
\]
which is (7c). This uses neither symmetry of the h-vector nor an
arithmetically Gorenstein boundary.

Two reusable ingredients are separated by this proof. The norm
argument works for a homogeneous inclusion \(A\hookrightarrow B\)
with \(B=A+Aw\), \(\deg w=1\), and \(w^2=r\), whenever r is a
quadratic polynomial nonsquare in \(\operatorname{Frac}S\).
The ideal defining A need only have no nonzero form below degree
\(\alpha\) for (7b). To obtain (7c), retain finite birationality on
the full generic algebras, saturation, local CM and finite projective quotient-support
hypotheses stated above, with A a complete intersection. Separately,
any one-dimensional standard graded CM quotient of S with
\(J_{<q}=0\), \(s\ge e\), and (7a) satisfies the same scalar
bound when \(q\ge1\) and \(e\ge2q-1\). These algebraic deductions
are characteristic free under their explicit hypotheses; applying
this particular separated cover still requires characteristic
different from two, and the low-degree premise used here is the
characteristic-zero one.

Geometrically, the actual conductor boundary of \(W\to Y\) cannot
lie scheme-theoretically on an ambient hypersurface of degree below
q. Such an equation would allow its multiple of the omitted
coordinate to descend and create a forbidden low-degree equation
of Y. Although the reduced boundary has only the two marked
points, its full infinitesimal structure must impose independent
conditions on all these low-degree ambient forms. Canonical
duality then requires complementary later postulation. This adds
a term growing cubically with the smaller defining degree to the
boundary-length requirement. It is not a bound on distinct points,
an upper bound on conductor capacity, or a positive residual degree.

The canonical Hilbert-function input remains the direct proof of
(7a) and the already checked Kreuzer comparison. The elementary
norm specialization is a new explicit repository consequence;
no literature priority or exhaustive literature-search claim is made.
The frozen source and its companion audit record a separate independent
reconstruction of this norm and postulation deduction. The current chapter
retains that reviewed scope.

The distinction from the general theorem in §11 is essential. Its
canonical injection and Hilbert inequality allow any positive degree of
the extra module generator and any two-dimensional standard graded
Gorenstein base. The norm step here additionally uses an actual polynomial
ambient ring, the quadratic relation for a degree-one generator, and a
lower bound on the initial degree of the defining ideal. The extremal
argument in §12 instead uses an irreducible nonlinear reduced support and
its embedding, without requiring a quadratic relation. For the fixed
quartic application with \(\alpha\ge5\), (7c) gives the stronger scalar
bound, but it does not replace those more general statements.

## 8.2. Endpoint lattice capacity of the same conductor

### An upper bound from the conormal moment

Use the separated quadratic cover of the fixed rational quartic with z²=r=2bc−ad in characteristic different from two. Assume an actual proper CI Y=V(F_a,G_b) with sole reduced support C. At either marked endpoint choose t=b/a or c/d on its standard affine chart. The completed algebra A is finite free over O=k[[t]]: reduction modulo its nilpotent ideal J=I_C O_Y is O, so finiteness follows by the finite nilpotent filtration and t is regular by the local CI Cohen–Macaulay property. On the first and last charts r restricted to C is t⁴; hence ε=r−t⁴∈J. In A_K=A⊗_O k((t)), the order-two cover splits and the root chosen by the marked branch is, up to sign,
    z=t² Σ_{l≥0} binom(1/2,l) (ε/t⁴)^l,
a finite sum. In odd positive characteristic interpret the coefficients by lifting dyadic rationals or the unique finite square-root recursion. The full branch lattice is B=A+Az inside the same generic algebra, by the actual homogeneous separated-branch theorem. Therefore the length of B/A is minus the minimum valuation of all minors of multiplication by z in any O-basis of A, including the size-zero minor 1. Equivalently it is the sum of negative Smith pole orders. This computes the same δ_i used by the global conductor theorem, not a normalized carrier or Frobenius specialization boundary.

For j≥0 let K_j=ann_A(J^j). Each K_j is saturated as an O-submodule: t^s u∈K_j implies t^s J^j u=0 and t is regular. Thus one can choose an O-basis compatible with the nested K_j. If s∈K_j then the summands with l≥j vanish on s; multiplying zs by t^max(0,4j−6) therefore puts it in A. The length of B/A is no larger than the sum of these column pole bounds, since the quotient is generated by the corresponding cyclic O-modules. Generic Artin CI duality identifies ann(J^j) with the orthogonal of J^j for the perfect multiplication pairing. Thus rank(K_j/K_(j−1))=h_(j−1), where h_i is the generic rank of J^i/J^(i+1). Writing n=ab/4 and M=Σ i h_i, the two endpoints give
    δ≤2 Σ_{i≥0} h_i max(0,4i−2)=8M−4(n−1).
This is an all-pair upper bound on the exact same conductor as §8.1, not a claim the upper bound conflicts with its lower bound. Sharper actual local bound: if ε∈t^u J at an endpoint, replace 4 by max(0,4−u) in the general exponent max(0,(4−u)(j−1)−2); do not infer this divisibility from abstract generic contact type.

The same calculation gives (0:_A J)⊂c because its elements satisfy zs=t²s. Off the marked points c=A; the known saturated homogeneous conductor quotient globalizes the inclusion.

### Fixed local-cohomology targets, and what they cannot see

For a hypothetical supported CI the Cech fraction h↦h/(FG) identifies A(a+b) with (0:_{H_I²(S)}(F,G)) (standard regular-sequence fraction representation, or the Koszul transition maps). Because the two fixed KG09 targets are killed by I, they correspond to the graded relative socle (0:_A I); the calculation above shows that both die in A/c. This is an actual object-level bridge and a limitation: full-conductor postulation constrains realization, but the conductor quotient cannot itself carry the two target values needed for a separating covector. Positive-contact multiplication also kills the targets, so any degree-persistence map must preserve them by changing the ancestor (bounded q-division comparison available separately), not by multiplying outputs. A next finite test is to compare the five added generators in the quartic q-shift with one concrete lifted multiplication image; the whole q-ray eventually has a common factor and cannot prove ambient coprimality.

### Nonsplit lower onset in the same conductor quotient

Order a≤b, and assume the smaller carrier F_a is integral and r is nonsquare in its function field. A boundary form h of degree d gives a homogeneous P of degree d+1 with P²−r h²∈(F_a,G_b) by the actual degree-one generator z of the branch algebra. For 2d+2<b this lies in (F_a) alone. If F_a does not divide h, the identity on the carrier makes r=(P/h)², a contradiction. Thus (J_Δ)_d=(F_a)_d in that degree range, with no assertion that the boundary ideal is zero in degrees ≥a. Put q_b=ceil(b/2)−1 and H*=binom(q_b+2,3)−binom(q_b−a+2,3), taking out-of-range binomials as zero. Combining this exact Hilbert onset with the existing canonical complementary inequality and no internal h-vector zeros gives
    δ≥2H*+(a+b−4)−2q_b+1.
A genuine new bound only if the onset improves; no contradiction follows automatically. Contrapositively, a low-degree boundary form independent of F forces splitting of the smaller carrier in the fixed cover. An odd valuation of r on the smaller carrier's normalization provides a direct nonsplit test; an arbitrary carrier need not satisfy it.

### Split carrier: the overlap is an actual complete intersection

Let \(Y=V(F,G)\) be a proper complete intersection with sole reduced
support \(C\), with \(F\) integral of degree \(a\ge5\) and \(G\) of
degree \(b\). This discussion does not require \(a\le b\). Work over
the algebraically closed ground field with \(2\) invertible. Write
\(X=V(z^2-r)\subset\mathbf P^4\) for the fixed smooth quadric
threefold and \(D,D'\) for its two reduced lifts of \(C\).
If \(r\) is square in \(k(V(F))\) in an affine trivialization,
the pullback of \(V(F)\) to \(X\) consists of two distinct conjugate
prime divisors, each with multiplicity one: the generic point is off
the branch quadric and the generic extension splits. Finiteness
excludes further divisors over lower-dimensional subsets. The
[Grothendieck–Lefschetz hyperplane theorem](https://www.journalofsing.org/volume4/brevik-nollet.pdf)
gives \(\operatorname{Pic}(X)=\mathbf Z[\mathcal O_X(1)]\).
Conjugation preserves this generator, so \(a=2m\). A section cutting
out one divisor is \(P+zQ\), with \(\deg P=m\) and \(\deg Q=m-1\),
by the double-cover module decomposition. The product of the two
sections cuts out the full pullback. Rescaling \(F\), we have
\[
F=P^2-rQ^2,\qquad \gcd(P,Q)=1 .
\]
In particular, an integral odd-degree carrier is always nonsplit in
this cover.

Suppose \(Q|_C\not\equiv0\). Choose conjugate signs so that
\(P+zQ\) vanishes on \(D\). The other factor is a unit at the
generic Artin point over \(D\); on \(D'\) the roles reverse.
Thus \(W=V_X(P+zQ,G)\) and its conjugate are precisely the two
separated branch schemes. Indeed the equations cut a proper
complete intersection (the integral factor surface dominates
\(V(F)\)); its curve support can only be \(D\), and it has the
same full generic algebra as the separated branch. Both schemes are
locally Cohen–Macaulay, so equality at the generic point gives equality
everywhere, with their saturated homogeneous ideals. In particular,
\(W\) is ACM in this case, without an ACM hypothesis on the general
separated branch.

Here the same conductor can be read from the overlap of the two
branches. With \(S=k[x_0,x_1,x_2,x_3]\) and \(A=S/(F,G)\),
the branch ring is \(B=S[z]/(z^2-r,P+zQ,G)\). Modulo the
image of \(S\) in \(B\), the coefficient of \(z\) is taken
modulo \(P,Q,G\): the two relations over \(S\) from the norm
factor are \(P+zQ\) and \(rQ+zP\). Consequently
\[
B/A=(S/(P,Q,G))(-1),\qquad J_\Delta=(P,Q,G).
\]
Equivalently, the overlap upstairs is cut out by \(P,Q,G\) in
\(X\), with the same equations defining the conductor downstairs.
Since \(B/A\) is nonzero with finite projective support, and
\(P,Q\) have no common component, \(P,Q,G\) form a homogeneous
regular sequence. This determines the **entire** conductor Hilbert
function, not just its low-degree onset:
\[
\delta=m(m-1)b,\qquad
\sum_{d\ge0} \dim_k(S/(P,Q,G))_d\,t^d
=\frac{(1-t^m)(1-t^{m-1})(1-t^b)}{(1-t)^4}.
\]
Its Artinian reduction is Gorenstein of socle degree
\(2m+b-4=a+b-4\); the complementary inequality (7a) is an
equality in every degree by the symmetry of this h-vector.

Even before taking the mate section, the signed factor surface
is finite birational to \(V(F)\). The same two relation columns,
now without \(G\), identify the relative conductor as \((P,Q)\)
downstairs and as \((Q)\) upstairs, using \(P=-zQ\) there.
This is the conductor of the finite partial cover, not necessarily
of the normalization.

Set-theoretically \(V(P,Q,G)\) lies on \(C\), and on \(C\),
\(P=0\) wherever \(Q=0\). Off the two marked endpoints the
cover separates without any conductor. Hence **all** zeros of
\(Q|_C\) must lie at the two marked endpoints. In binary
coordinates on \(C\cong\mathbf P^1\), its restriction must be
a nonzero scalar times a monomial of degree \(4(m-1)\).
There is also an exact local split of the length. If \(h_i\)
is the order of \(Q|_C\) at the marked endpoint \(i\), then
\(\operatorname{length}(A_i/QA_i)=nh_i\), with \(n=ab/4\).
This follows from the determinant of multiplication by \(Q\)
on the free endpoint lattice: generically its reduction is the
scalar \(Q|_C\), and the remaining part is nilpotent. Locally
\(A_i/(Q)\) is cut out by \(P^2,Q,G\), so its length is
twice that of the conductor cut by \(P,Q,G\), by the two-step
filtration by \(P\) and regularity. Therefore
\(\delta_i=nh_i/2\); in particular \(h_i\) is even if \(n\) is odd.

Any zero of \(Q|_C\) gives \(P=Q=0\) there and makes
\(V(F)\) singular. Since \(4(m-1)>0\), an integral
split carrier smooth at both marked endpoints cannot have a mate
in **any** degree. This also covers the omitted case
\(Q|_C\equiv0\) for that smooth-endpoint assertion: then
\(P|_C\equiv0\) and the norm surface is singular along all of
\(C\). For the general split case, the binary-monomial restriction
remains necessary when \(Q|_C\not\equiv0\), not sufficient:
one still needs an actual mate with the prescribed local contact.
When \(Q|_C\equiv0\), both conjugate surfaces contain both
lifts, so cutting one factor surface by \(G\) no longer
isolates the branch. The complete-intersection presentation and
length formula do not extend by this argument.

The excluded locus is nonempty in every even degree \(2m\ge6\).
On \(X\), degree-\(m\) sections through \(D\) have base scheme
\(D\), since \(D\) is a rational normal quartic with ideal
generated by quadrics. Off \(D\) their linear system separates
general points and tangent vectors: on an open where one fixed
quadric through \(D\) does not vanish, it contains that quadric
times the complete degree-\((m-2)\) system. Bertini gives an
integral general divisor (irreducibility and generic smoothness
off \(D\)). The open condition that \(Q|_C\) be nonzero at both
endpoints is also nonempty: choose
\(Q=x_0^{m-1}+x_3^{m-1}\) and lift the prescribed restriction
\(-z|_D\,Q|_D\) to a degree-\(m\) form \(P\) downstairs.
The restriction in that degree is surjective for \(m\ge2\):
the weights of the quartic parameterization realize all binary
monomials of degree \(4m\). At either endpoint \(P=r=0\) and
\(Q\ne0\), so \(dF=-Q^2dr\ne0\) by smoothness of the branch
quadric. The general signed divisor and its
conjugate are distinct, as one contains \(D\) and the other does
not. Their norm defines an integral surface downstairs, because
the two reduced divisors have the same integral image and are
generically outside the branch quadric.

Both equations cannot be integral split carriers of the
nonzero-restriction type. Orient their signed factors so that the
positive factors contain \(D\) but not \(D'\). The positive factor
of \(F\) and the negative factor of \(G\) would cut a proper
intersection of two ample divisors on \(X\), hence a nonempty curve.
It lies in the pullback of \(Y\), but neither \(D\) nor \(D'\)
lies in both of those factors. This is impossible.

### Two-lift split carriers: actual primary pieces control postulation

Keep the norm factorization \(F=P^2-rQ^2\), but assume
\(P|_C=Q|_C=0\). For \(\epsilon=\pm1\) put \(S_\epsilon=P+\epsilon zQ\)
and let \(W_\epsilon\) be the \(D\)-primary piece of the actual
complete intersection \(V_X(S_\epsilon,G)\), defined by contraction
from the generic point of \(D\). The two generic lengths
\(\ell_\epsilon\) are positive and sum to \(n=mb/2\), by additivity
for the product of the two nonzerodivisors modulo \(G\) at that
point. Neither individual factor cuts the full generic branch.

For \(2d+2<b\), set \(k=d-m+1\). The space
\((J_\Delta)_d/(F)_d\) is the union of the two images of
\[
 \bigl(I_{W_\epsilon}/(S_\epsilon)\bigr)_k
 \longrightarrow (S/(F))_d,\qquad zA-\epsilon B\longmapsto AP+BQ.
\]
The source ideals are in the homogeneous coordinate ring of \(X\);
negative degrees are zero. Both maps are injective and at most one
source is nonzero in any given degree.

Indeed a conductor form \(h\) has a descent equation \(zh=P_h\)
on the separated branch. Its norm is zero modulo \((F,G)\), so
\(P_h^2-rh^2\) is in \((F)\) since its degree is below \(b\).
Multiplying by \(Q^2\) gives \(QP_h=\epsilon Ph\) in the carrier
domain for one sign. In the polynomial ring, reducing
\(QP_h-\epsilon Ph=FL\) modulo \(Q\) and using coprimality of
\(P,Q\) gives \(h\in(P,Q)\). Write \(h=AP+BQ\); cancellation
in the domain gives \(P_h\equiv\epsilon(ArQ+BP)\pmod F\).
On \(X\),
\[
 zh-\epsilon(ArQ+BP)=(zA-\epsilon B)S_{-\epsilon}.
\]
At the generic point of \(D\) cancel \(S_{-\epsilon}\) modulo \(G\)
in the ideal generated by \(S_\epsilon S_{-\epsilon}\); the two
factors are nonzerodivisors there. This gives exactly membership
in \(I_{W_\epsilon}\). Conversely such membership gives descent
by the generic calculation and saturation of the locally
Cohen–Macaulay separated branch.

The Koszul change \((A,B)\mapsto(A+QT,B-PT)\) changes the source
by \(\epsilon T S_\epsilon\). A multiple \(h=FL\) comes from
\(zL S_\epsilon\), after which the Koszul change gives the entire
kernel. Conversely multiplication by \(S_\epsilon\) maps to a
multiple of \(F\) by expanding in the basis \(1,z\). If a class
came from both signs, the two values of \(P_h\) would agree
by injectivity of \(A=S/(F,G)\) into the branch ring, and hence
agree modulo \(F\) because their degree is below \(b\).
The signed norm equations give \(2Ph=0\) in the carrier domain,
so the class is zero. The union is a vector space; it cannot
be a union of two proper subspaces. Thus at most one source
contributes.

A contributing degree-\(k\) section cuts a proper divisor on
the integral signed surface, contains \(W_\epsilon\), and has
degree \(2mk\) on \(X\). It follows that \(4\ell_\epsilon\le2mk\).
Since \(k<b/2-m\), the thicker piece never contributes. If
\(|\ell_+-\ell_-|\le m^2\), the thinner piece has length at least
\(mb/4-m^2/2\) and neither contributes in the norm range.
In this nearly balanced sector, \((J_\Delta)_d=(F)_d\) for
\(2d+2<b\), giving the same postulation lower bound as in the
nonsplit case. In general the onset holds for
\(k<2\min(\ell_+,\ell_-)/m\); it also holds for \(k\le1\)
because \(D\) has no linear equation. At equality in the degree
test the proper intersection has no residual and is precisely
\(W_\epsilon\), by purity and equality of generic ideals.
The nonzero source is then one-dimensional: its section is
determined up to scalar modulo the signed equation.

For a split sextic, \(m=3\), the first possible degree is \(d=4\)
in the norm range \(b>10\). The thinner piece must have length
at most three. At length one it is \(D\), and all five quadrics
through \(D\) on \(X\) contribute. At length two the source consists
of quadrics through the actual double structure, of dimension
at most four since the five quadrics generate the ideal of \(D\).
At length three a nonzero source is one-dimensional and requires
an actual degree-\((2,3)\) pair on \(X\) supported only on \(D\).
This is a postulation and contact test, not a capacity bound
or an all-mate exclusion for two-lift carriers.

### Two-lift split carriers: intersection on the signed surface

The two-lift case also has a global exclusion that does not require
estimating the endpoint conductor. Let \(S_+=V_X(P+zQ)\) be one
integral signed surface of degree \(m\) on the covering quadric,
with \(P|_C=Q|_C=0\). If either signed surface is smooth along
\(D\cup D'\), there is **no mate in any degree**. This is smoothness
of the surface upstairs; the original norm carrier downstairs
is singular along \(C\) in this two-lift case.

Indeed, a hypothetical mate of degree \(b\) would cut on
\(S_+\) an effective Cartier divisor with cycle
\(\lambda D+\mu D'\), with \(\lambda,\mu>0\). Its intersection
with the hyperplane class gives
\(4(\lambda+\mu)=2mb\). Along the two curves adjunction
on \(S_+\) gives \(K_{S_+}=(m-3)H\) and
\[
D^2=(D')^2=10-4m.
\]
The scheme intersection of the two lifts has length two at each
marked point and is empty elsewhere: on the pullback of \(C\)
the local equation is \(z^2=t^4\), and the two ideals
\((z-t^2)\) and \((z+t^2)\) sum to \((z,t^2)\).
Their common scheme does not change when computed inside a
surface containing both curves. Since the curves are Cartier
on the smooth neighborhood of their support, \(D\cdot D'=4\).
Intersecting the mate with \(D+D'\) would therefore give
\[
8b=(\lambda+\mu)(14-4m),\qquad
8-\tfrac m2(14-4m)=2m^2-7m+8>0,
\]
a contradiction. The same argument applies to the other signed
surface by conjugation. Singularities away from the two curves
play no role.

There are actual integral split carriers in this locus in every
even degree \(2m\ge6\), in characteristic zero. The flat
pullback of \(C\) is the reduced union \(D\cup D'\): its algebra
is free over \(C\) locally and generically reduced, so any
nilpotent would be torsion and hence zero. The quartic ideal is
generated in degrees two and three. Thus the system of degree-\(m\)
sections vanishing on the union generates the union's ideal
sheaf for \(m\ge3\), by pulling back those generators and padding
degrees with forms that are nonzero at the point. At a smooth
point of the union, the condition that the section be singular
there imposes two independent linear conditions. As the point
varies in a curve, their incidence cannot dominate the parameter
space. At either of the two marked points the union has a
two-dimensional tangent space in the smooth threefold: locally
the union is cut by a transverse coordinate and \(z^2-t^4\).
So singularity imposes one nontrivial linear condition at each
of these fixed points, also avoidable. Off the union the system
has no base points, and its image has dimension three: multiplying
the fixed containing quadric of \(C\) by all degree-\((m-2)\)
forms downstairs gives a subsystem with three-dimensional image.
Bertini gives an integral general surface. The conditions
\(P\ne0\) and \(Q\ne0\) define a nonempty open since both
\(I_C(m)\) and \(I_C(m-1)\) are nonzero. The signed surfaces
are then distinct, with the same integral image; their norm
is an integral carrier, since over its generic point the cover
is étale and the two factors have multiplicity one.

#### Required correction at Du Val points

For a normal signed surface with at worst Du Val singularities
along the two lifts, the same argument quantifies the exact
correction a mate would need. On a resolution crepant near the
lifts, let \(\widetilde D,\widetilde D'\) be their strict
transforms. Each is isomorphic to the corresponding smooth
quartic: the restricted map is proper, birational and has
finite fibers, hence is an isomorphism over a normal curve.
Their self-intersections are still \(10-4m\) by crepancy.
Put \(k=\widetilde D\cdot\widetilde D'\). At a point of the
second strict transform the pullback of the ideal of \(D\)
is contained in the ideal of \(\widetilde D\); restricting
to \(\widetilde D'\cong D'\) therefore gives \(k\le4\).
Write the total pullback of the actual mate divisor as
\(\lambda\widetilde D+\mu\widetilde D'+E_G\).
Intersecting with \(\widetilde D+\widetilde D'\) gives the
required budget
\[
E_G\cdot(\widetilde D+\widetilde D')
=8b-(\lambda+\mu)(10-4m+k)
\ \ge\ b(2m^2-7m+8).
\]
For a signed cubic this is at least \(5b\).
More precisely, at each resolved point let \(A_p\) be the
negative of the exceptional intersection matrix and let
\(x_p,y_p\) be the actual intersection vectors of the two
strict transforms with the exceptional curves. The contribution
is
\[
(x_p+y_p)^\mathsf{T}A_p^{-1}(\lambda x_p+\mu y_p);
\]
this follows by intersecting the total pullback with the
exceptional curves, on which it has degree zero. It is the
[numerical pullback mechanism](../carriers/numerical_surface_pullback.md)
on the actual signed surface, with the local incidence of both
lifts retained. The next test is which incidence vectors and
correction budgets the signed cubic equations really allow.
The ADE type alone does not determine these vectors, and this
calculation does not yet supply an incompatible upper bound.

#### Nodal signed cubics: the correction is insufficient

In degree six downstairs (\(m=3\)), suppose the signed cubic
is normal and all its singularities along \(D\cup D'\)
are ordinary double points. Then there is no mate in any degree.
This follows by evaluating the correction on the actual nodal
incidence, not by assuming the two curves avoid the singularities.

At a node the resolution is the blowup and each smooth curve
through it meets its unique exceptional \((-2)\)-curve with
multiplicity one: the maximal ideal has order one on the
smooth curve. If both lifts pass through that node, it is a
marked endpoint. Their local intersection on the resolution
has length one, rather than two downstairs. Indeed around
such an endpoint take smooth ambient coordinates \(t,z,w\),
with the lifts \(w=0,\ z=\pm t^2\). In the blowup chart
containing both strict transforms the coordinates are
\(t,z/t,w/t\), and the common ideal of their strict transforms
is \((t,z/t,w/t)\). The strict transform of the surface
contains both, so it has the same common scheme. If there
are \(s\) shared nodes, this gives \(k=4-s\). The matrix
correction from each shared node is \(\lambda+\mu\) and
exactly offsets the loss of one mutual intersection.
Let \(u,v\) count nodes belonging only to \(D\) or only to
\(D'\), respectively. The correction equation reduces to
\[
\frac{u\lambda+v\mu}{2}=5b .
\]

To count unshared nodes, use the unique containing quadric
\(q=0\) of \(C\) downstairs. In a two-lift sextic norm the
coefficient \(Q\) is a nonzero scalar multiple of \(q\).
The restriction of \(P\) to the smooth quadric is nonzero
(otherwise \(F\) would have the factor \(q^2\)). It cuts
\(C\) plus a residual divisor of ruling class \((2,0)\),
up to exchange of the rulings, since \(C\) has class
\((1,3)\) up to the same exchange. This residual divisor
meets \(C\) in length six. Off the two marked points the
cover is étale over \(C\), and the pulled-back containing
quadric is smooth there. Away from the residual intersection
the signed cubic is smooth along the marked lift, because its
restriction to the pulled-back quadric cuts the lift simply.
At a residual point the two first derivatives on the two
sheets differ, after transport to the base, by a nonzero
multiple of \(2z\,dq\). Thus at most one lift over each such
point can be singular on a given signed cubic. It follows
that \(u+v\le6\), even for coincident residual rulings.
Consequently the left-hand side of the correction equation
is at most \(3(\lambda+\mu)=9b/2<5b\), a contradiction.

The cancellation at shared nodes does not classify other Du
Val singularities. For them the incidences of the strict
transforms and the change in their mutual intersection must
still be tracked together.

#### Transverse residual sextics: higher \(A_n\) do not suffice

Work in characteristic zero with a two-lift split sextic, so
\(m=3\) and \(Q\) is a nonzero scalar multiple of the fixed
containing quadric equation \(q\). Suppose the signed cubic is
normal, and the residual ruling divisor in \(P|_{V(q)}\) meets \(C\) in six
distinct unmarked points. Then there is no mate in any degree.

The two marked endpoints are smooth on the signed surface in
this sector. At either endpoint the image of the differential
of the quadratic cover is the tangent plane of its branch
quadric; there that plane is also the tangent plane to
\(V(q)\). This follows from the linear terms of \(r\) and
\(q\) in the endpoint affine charts. Since \(P|_{V(q)}\)
cuts \(C\) simply there, \(dP\) is nonzero on that tangent
plane. Along the lift \(d(P+zQ)=dP\) at the endpoint,
with \(dP\) understood as pulled back, so the signed
surface is smooth there.

Off the endpoints the cover is étale along \(C\); the only
possible marked singularities lie over the six residual hits,
with at most one singular lift over any hit by the signed
derivative comparison above. At a singular hit the fixed
slice \(q=0\) has two transverse branches, one the marked
quartic and the other the residual ruling. Choose local
coordinates so this slice equation is \(uv=0\). The formal
splitting lemma over \(k[[q]]\) puts the signed equation in
the form \(xy+f(q)\). After normalizing the equation on the slice,
the subsequent changes preserve \(q\) and are the identity on the slice. The
transverse Hessian is invertible, so one first solves for
the critical point in \(u,v\) over \(k[[q]]\), shifts by
multiples of \(q\), and removes the remaining higher
transverse terms by formal changes. In particular the marked
axis remains one of the two axes on \(q=0\). Normality
excludes \(f=0\), and the point is an \(A_n\) with
\(\operatorname{ord}_q f=n+1\). On the toric resolution of
\(xy=q^{n+1}\) the marked axis meets the end of the exceptional
chain transversely (it is the strict transform of a boundary
divisor of the defining cone). The end diagonal of the inverse
chain matrix is \(n/(n+1)\), as follows by solving the linear
recurrence on the chain with zero boundary values. This is its
self-correction in the numerical pullback.

Let \(A,B\) be the sums of these end corrections on \(D,D'\),
respectively. The two lifts meet only at their smooth marked
endpoints, hence their strict transforms still meet in length
four. With \(\lambda+\mu=3b/2\), intersecting the pulled-back
mate separately with the two strict transforms gives
\[
(6-A)\lambda=(6-B)\mu=2b,
\qquad
\frac1{6-A}+\frac1{6-B}=\frac34.
\]
To bound the rank needed at the marked hits, spread the finite
equation data to a subfield of \(\mathbf C\) and smooth the
signed cubic in its full linear system on \(X\). Choose a
general perturbing section nonzero at all marked singular
points, so its pencil has smooth general member. Inside
disjoint analytic Milnor balls around those points, the
nearby fibers are the Milnor fibers of the \(A_n\) germs:
locally the pencil is a level set of the signed equation
divided by the nonvanishing perturbing section. The local
2-cycles have the negative definite \(A_n\) intersection
matrices. Their pairings are unchanged in the global fiber,
and cycles in different balls have zero mutual pairing.
Thus the direct sum of their rational spans injects into
the homology of the smooth fiber: a kernel vector would
pair to zero with the entire local sum, which is nondegenerate.
The smooth \((2,3)\) complete intersection is a K3 surface
with intersection signature \((3,19)\). Hence the sum of the
\(n\) at the marked hits is at most 19. This use of a smoothing
requires no Du Val assumption away from the two lifts;
the resolution used to intersect the mate needs to be crepant
only along the two lifts.

The equality is incompatible with that rank bound. Count only
singular hits and exchange the lifts so their counts are
\(i\ge j\) with \(i+j\le6\). If \(i\le4\), each correction
is strictly below one. The left-hand side is strictly less
than \(3/4\): the largest candidate bounds are at allocations
\((4,2)\) and \((3,3)\), where they are \(1/2+1/4\) and
\(2/3\), respectively. If \(i=5\), then \(j\le1\), and
Cauchy–Schwarz gives
\[
6-A=1+\sum_{s=1}^5\frac1{n_s+1}
\ \ge\ 1+\frac{25}{19+5}=\frac{49}{24}.
\]
The left-hand side is at most \(24/49+1/5<3/4\).
Finally if \(i=6\) then \(B=0\), forcing
\(\sum_{s=1}^6 1/d_s=12/7\), where \(d_s=n_s+1\ge2\)
and \(\sum d_s\le25\). Among the denominators divisible by
seven the only possibilities are one seven, two sevens,
or one fourteen (or none). After multiplying by seven,
reduce in \(\mathbf Z_{(7)}\) modulo seven. The corresponding
left residues are \(1,2,1/2,0\), none equal to
\(12\equiv5\). Thus no allocation is possible.

This uses the transverse unmarked slice to fix the exceptional
incidence, not just the Du Val type. Repeated or tangent
residual intersections, residual hits at the endpoints, and
nonnormal signed surfaces are not covered by this argument.

#### Doubled unmarked ruling: a conic bounds the correction

For the two-lift split sextic, the degree-three ruling map of
\(C\) on \(V(q)\) is \([s^3:t^3]\), so a reduced unmarked
ruling meets \(C\) at three distinct points in characteristic
zero. The only possibility not covered by the transverse
result when the residual divisor avoids the endpoints is
a doubled unmarked ruling \(2L\). In this case too there is
no mate in any degree if the signed cubic is normal.
No Du Val hypothesis is needed, including along the lifts.

Write \(T\subset X\) for the pullback of \(V(q)\). On a ruling
\(L\) away from the endpoints, Segre coordinates have the form
\((\alpha u,\alpha v,\beta u,\beta v)\) with \(\alpha\beta\ne0\).
The branch section restricts to \(\alpha\beta uv\). Thus the
pullback \(R\) of \(L\) is a smooth conic, and \(T\) is smooth
along it: at its two branch points the branch equation has
a simple zero on \(L\), so it cuts the downstairs quadric
transversely there, and elsewhere the cover is étale.
The signed cubic cuts \(D+D'+2R\) on \(T\) near \(R\).
Its derivative along \(R\) is therefore zero in the
cotangent bundle of \(T\), and its derivative normal to \(T\)
defines a section of
\[
N^*_{T/X}|_R\otimes\mathcal O_R(3)=\mathcal O_R(1).
\]
This line bundle has degree two on the conic. The zeros
are exactly the singular points of the signed cubic along
\(R\); the section is nonzero by normality. All singularities
along the lifts must lie among these zeros, since away from
\(R\) the signed cubic cuts each lift simply on \(T\) at
unmarked points, and the marked endpoints are smooth by
the tangent-plane argument above.

At a singular point of a lift use \(w=q\) and choose
coordinates \(x,y\) on \(w=0\) in which the lift is \(x=0\)
and the conic is \(y=0\). They meet transversely since
the ruling is unmarked. The cubic has local equation
\(xy^2+wA(x,y,w)\) after multiplication by a unit, and the
conormal section on the conic is represented by \(A(x,0,0)\).
At a simple zero, \(A_x(0)\ne0\); the Hessian has rank two
and the tangent of \(R\) is outside its radical. The point
is therefore of type \(A_{d-1}\), and \(R\) meets an end of the
exceptional chain. Indeed in a rank-two normal form
\(uv=\xi^d\) a smooth curve with tangent outside the radical
has either \(u\) or \(v\) of order one, which gives the end
intersection in the toric resolution. A smooth marked lift
through this point meets exactly one exceptional curve,
transversely: choose a local function restricting to order
one on it; every exceptional component has order at least
one in the pullback of that function. In the chain
discriminant group \(\mathbf Z/d\), incidence at vertex
\(j\) has class \(j\) up to simultaneous sign (the relations
are \(2e_j=e_{j-1}+e_{j+1}\) with zero boundary values).
The Cartier divisor \(w=0\) gives the local relation
\([D]+2[R]=0\), with \(D\) denoting the lift present there.
Thus the marked lift meets vertex \(2\) or \(d-2\), and
its diagonal correction is \(2(d-2)/d<2\).

Let \(A_0,B_0\) denote the correction sums for the two
lifts. Their endpoints are smooth, so the same separate
intersection calculation gives
\(1/(6-A_0)+1/(6-B_0)=3/4\).
Two simple zeros of the conormal section yield total
correction strictly below four. For nonnegative sums
with that budget the left side is at most
\(1/(6-4)+1/6=2/3\), by convexity. If the section
instead has a double zero, it can contribute at only one
marked point, and the required correction there is
\(30/7\). At that zero \(A_x(0)=0\). If \(A_y(0)\ne0\),
the tangent of the marked lift itself is outside the
Hessian radical, so its end correction is below one.
The double-zero case can in fact be closed without the local
Du Val assumption. If \(A_x(0)=A_y(0)=0\) but \(A_w(0)\ne0\),
the singularity is necessarily \(D_5\). Indeed the conormal
section has a zero of order exactly two, so the coefficient
of \(x^2\) in \(A(x,0,0)\) is nonzero. With weights
\((2,3,4)\) on \((x,y,w)\), the initial equation is
\(a w^2+c x^2w+xy^2\), with \(ac\ne0\). Completing the
square gives \(w'^2+xy^2+c'x^4\), \(c'\ne0\). This weighted
initial form determines the formal type: its Jacobian
quotient has basis \(1,x,x^2,x^3,y\), all of weight at
most six, so terms of weight above eight can be removed
successively by coordinate changes of strictly increasing
weight. The \(D_5\) Cartan determinant is four; the required
fraction \(30/7\) is impossible.

If \(A_x(0)=A_y(0)=A_w(0)=0\), the surface has
multiplicity three. In the blowup chart along the marked
lift, write \(x=yX_1,w=yW_1\). The strict equation is
\[
X_1+W_1\,A(yX_1,y,yW_1)/y^2=0.
\]
It is smooth where the strict lift hits the exceptional
divisor and there \(W_1=0\) cuts out the strict lift,
transversely to the exceptional divisor \(y=0\). The
strict conic lies in a different tangent direction. A
resolution elsewhere on this blowup need not modify this
neighborhood. The discrepancy at the exceptional component
met by the lift is \(-1\): the ambient volume form gains
\(y^2\) in the blowup, while its defining equation loses
\(y^3\), giving the factor \(y^{-1}\) in the residue.
Since the signed cubic has trivial canonical class and
this is the only possible singular point of either lift,
adjunction gives self-intersection \(-1\) for the strict
lift through the point rather than \(-2\).

There is also an upper bound on its numerical-pullback
correction. Locally \(\operatorname{div}(w)=D+2R\).
On a resolution of the normal surface the numerical
pullbacks of these two effective curves have nonnegative
exceptional coefficients: their coefficient vectors solve
the negative definite intersection systems with
nonnegative incidence vectors, and the inverse of the
negative exceptional matrix is nonnegative. The
exceptional part of the actual pullback of \(w\) is their
weighted sum. It meets the strict marked lift with
multiplicity exactly one, since \(w=yW_1\) in the chart
and the strict conic is disjoint there. Thus the marked
curve's own numerical correction is at most one. Together
with the change in adjunction, this gives an effective
self-correction of at most two relative to the smooth
self-intersection \(-2\). The same two separate mate
intersections, using this effective correction on the
singular side and zero on the other, would require
\(30/7\), again impossible.

A residual ruling through a marked endpoint lies in the branch
quadric; the conic derivative argument does not apply. The
[distinct marked rulings](#distinct-residual-rulings-through-marked-points)
instead use the shared endpoint geometry.

#### Distinct residual rulings through marked points

For a two-lift split sextic with normal signed cubic in
characteristic zero, suppose the residual ruling divisor
has two distinct fibers. At a marked point belonging to
one such fiber, use coordinates
\(t=x_1/x_0,\ v=x_2/x_0,\ q=x_3/x_0-tv=tv-z^2\) on the
first chart, and reversed coordinates at the other point.
The signed cubic has equation
\[
v(v-t^3)a(v)+(tv-z^2)\bigl(L(t,v,tv-z^2)+cz\bigr),
\qquad a(0)c\ne0.
\]
Indeed its restriction to the downstairs quadric consists
of \(C\) and the two residual rulings, with just a simple
residual fiber \(v=0\) at this point. The two lifts are
\(v=t^3,\ z=\pm t^2\). If \(L(0)\ne0\), the quadratic
part has rank three, giving the shared node treated above.

If \(L(0)=0\) but \(\ell=L_t(0)\ne0\), the following local
resolution gives both the type and the actual incidences.
In the first blowup chart put \(V=v/t,\ Z=z/t\). The
strict equation is
\[
 V(V-t^2)a(tV)+t(V-Z^2)
    \bigl(\ell+cZ+L_v(0)V+O(t)\bigr).
\]
The reduced exceptional line is \(t=V=0\); its singular
points are \(Z=0\) and \(Z=-\ell/c\), from the derivative
\(-Z^2(\ell+cZ)\). There is no singularity at infinity,
where in the \(z\)-chart the remaining derivative is
\(-c\). The simple root is a node, by its nonzero
\(t,Z\) pairing and squared \(V\) term. At zero the
Hessian in \((V,t)\) is nondegenerate. Splitting over
\(k[[Z]]\) gives critical coordinates starting
\(V=Z^2,t=-2a(0)Z^2/\ell\) and critical value starting
\(a(0)Z^4\), so the point is \(A_3\). The old exceptional
line has both split coordinates of order at least two;
their product has order four, so their orders are exactly
\((2,2)\) and the line meets the middle exceptional curve.
The two marked lifts \((V,t,Z)=(t^2,t,\pm t)\) point to the
same nonkernel isotropic axis. Their order-one split
coordinate divided by \(Z\) has opposite nonzero values,
so they meet the same end of the chain at distinct points.
The first blowup is crepant by multiplicity two, and the
resulting graph is \(D_5\): the old line joins the middle
of the \(A_3\) chain to the additional node exceptional.
The two lifts meet the same short tip. The inverse Cartan
diagonal at that tip is \(5/4\).

In the numerical intersection matrix of the two original
lifts, relative to a smooth marked endpoint, a shared node
adds \(1/2\) to each self-intersection and subtracts
\(1/2\) from their mutual intersection. The shared
\(D_5\) just computed adds \(5/4\) to each self-intersection
and subtracts \(3/4\) from the mutual intersection: their
strict transforms no longer meet over the point, and the
common tip contributes \(5/4\) to their numerical product.

The remaining simple endpoint case, \(L(0)=L_t(0)=0\),
has a different resolution but a controlled numerical
correction. Blow up with weights \((1,2,3)\) on \((t,z,v)\).
The weight-six initial equation, in the weight-one chart
\(z=t^2Z,\ v=t^3V\), is
\[
a(0)V(V-1)+(\gamma+cZ)(V-Z^2)=0.
\]
Here \(\gamma\) is the coefficient of \(t^2\) in \(L(t,0,0)\).
The exceptional curve \(E\) is integral: the quadratic in
\(V\) has discriminant a cubic in \(Z\) with nonzero
cubic coefficient, not a square, and the homogeneous form
has no component in \(t=0\). The partial strict surface is
normal locally over the point: the weighted chart covers
are hypersurfaces, smooth at the generic point of
their reduced exceptional curve, and possible singularities
there are isolated; taking finite chart quotients preserves
normality. The tautological restriction is
\(\mathcal O_E(E)=\mathcal O_E(-1)\) in the rational divisor
sense. The degree of \(\mathcal O_E(1)\) is one: the
weight-one coordinate vanishes at the single point
\(a(0)v^2=cz^3\) of \(\mathbf P(2,3)\), where both
coordinates are nonzero, the stabilizer is trivial,
and the intersection is transverse. Thus \(E^2=-1\).

Both lifts meet \(E\) transversely at distinct smooth
points \((V,Z)=(1,\pm1)\): the \(V,Z\) derivatives are \(a(0)+\gamma\pm c\)
and \(\mp2(\gamma\pm c)\), which cannot both vanish,
and \(t\) is a parameter
on either lift. Resolve any other points without modifying
these neighborhoods. The discrepancy on the component
met by the lifts is \(-1\), since the ambient volume
form in this chart acquires \(t^5\) and the defining
equation contributes \(t^6\) in the residue. Adjunction
therefore adds one to each strict self-intersection.
The numerical pullback over this endpoint adds \(E\) to
either strict lift on the partial surface, since each
meets \(E\) once and \(E^2=-1\); further resolution
does not change the numerical pairing. Thus the
numerical corrections from the initial endpoint,
relative to a smooth endpoint, are **\(+2\) on both
self-intersections and \(-1\) on the mutual intersection**:
the strict transforms do not meet, and the contracted
curve contributes one to their numerical product.

These three local cases suffice for all distinct residual
rulings. If both rulings are marked, the sum of one
numerical self-intersection and the mutual intersection
is at most four: its smooth baseline is two and each
marked contribution adds at most one to that row sum.
The mate would require \(8b\le4(3b/2)\), a contradiction.
If one ruling is marked and one is unmarked, the three
unmarked transverse hits contribute extra self-corrections
\(A,B\ge0\) with \(A+B<3\). Denote by \(u\) the common
numerical self-intersection before those extra corrections
and by \(v_0\) the numerical mutual intersection; the
separate intersections with the mate give
\[
(v_0-u-A)\lambda=(v_0-u-B)\mu=(3v_0/2-4)b.
\]
For a shared node, \((u,v_0)=(-3/2,7/2)\), and this
requires \(1/(5-A)+1/(5-B)=6/5\), whereas the left side
is below \(1/2+1/5\). For the shared \(D_5\),
\((u,v_0)=(-3/4,13/4)\), so the required value of
\(1/(4-A)+1/(4-B)\) is \(12/7\), but the left side is
below \(1+1/4\). Both bounds use convexity and the
total budget three.

In the weight-six case \((u,v_0)=(0,3)\), the reciprocal
sum \(1/(3-A)+1/(3-B)\) would have to be three.
If at most two unmarked singular hits belong to either
lift, the largest allocation is \((2,1)\) and the sum
is below \(1+1/2\). Otherwise all three lie on one
lift and the other has no correction. Writing
\(d_i=n_i+1\) for the three end incidences, the equality
requires \(\sum 1/d_i=3/8\). The K3 smoothing bound
on the three isolated unmarked \(A_{n_i}\) points
alone gives \(\sum d_i\le22\), irrespective of the
marked singularity. Hence \(\sum 1/d_i\ge9/22>3/8\),
again impossible. A [doubled marked ruling](#doubled-marked-ruling-closure-for-normal-signed-cubics)
requires the separate argument below, not a degenerate simple endpoint.

#### Doubled marked ruling: closure for normal signed cubics

The remaining residual divisor is a doubled marked ruling.
In this case too, an integral two-lift split sextic with
normal signed cubic in characteristic zero has no mate
in any degree.

For the marked ruling in the first affine chart, write the
downstairs quadric in Segre form
\[
(x_0,x_1,x_2,x_3)=(A u,A v_0,B u,B v_0).
\]
The quartic is \(B u^3-A v_0^3=0\), and the ruling in
question is \(B=0\). The cubic
\(x_2^3-x_1x_3^2=B^2(Bu^3-Av_0^3)\) restricts to the exact
divisor \(C+2L\) on the quadric. Thus the actual \(P\)
in the norm representation is a nonzero multiple of this
cubic plus \(q\) times a linear form. In cover coordinates
\(t=x_1/x_0,\ v=x_2/x_0,\ q=tv-z^2\), the signed cubic
has equation
\[
a v^2(v-t^3)+(tv-z^2)\bigl(L(t,v,tv-z^2)+cz\bigr),
\qquad ac\ne0,
\]
and along the reduced inverse image of the marked ruling,
\(L(t,0,0)=L_0+\ell t\). Indeed
\(v^3-t(x_3/x_0)^2=v^2(v-t^3)-tq(2tv+q)\);
the added \(q\)-coefficient vanishes on that line.

If \(L_0=\ell=0\), all first derivatives of the signed
equation vanish along \(v=z=0\), a curve, contradicting
normality of the surface. If \(L_0\ne0\), the marked point
is a shared node, since the quadratic is
\(L_0(tv-z^2)\). It adds zero to each numerical row sum
(self plus mutual intersection), as above. It remains to
treat \(L_0=0,\ell\ne0\).

At this point the surface has multiplicity three. In the
ordinary blowup chart \(v=tV,\ z=tZ\), its strict equation is
\[
aV^2(V-t^2)+(V-Z^2)
       \bigl(\ell+L_v(0)V+cZ+O(t)\bigr).
\]
The surface is smooth at the common marked point of the
strict lifts, by the \(V\)-derivative \(\ell\). The two
strict lifts are \(V=t^2, Z=\pm t\); in the local surface
coordinates \(t,Z\) they meet with length one, and each
meets the same exceptional component \(t=0\) transversely
once. Resolve elsewhere without modifying this
neighborhood. The discrepancy at the component met
by the lifts is \(-1\), since the ambient volume in the
ordinary threefold blowup gains \(t^2\) and the equation
contributes \(t^3\) in the residue. Adjunction therefore
adds one to each strict self-intersection, while the
strict mutual intersection loses one at this endpoint.

Let \(e\) be their common exceptional incidence vector
on a resolution over this point. If \(M\) is the negative
of the exceptional intersection matrix, all three
numerical corrections (two self and one mutual) at
this point are \(s=e^{\mathsf T}M^{-1}e\). To bound
\(s\), use the actual Cartier divisor \(q=0\) on the
signed surface, which has \(D,D'\) each with
multiplicity one and an effective residual divisor.
In fact the reduced inverse ruling occurs with
multiplicity four: off the endpoint, \(q=0\) gives
\(v=z^2/t\), and the factor \(v^2\) has order four.
The exceptional part of the pullback of \(q\) is the
sum of the numerical exceptional parts for these
effective curves. All their exceptional coefficients
are nonnegative by inverse-matrix positivity. In
the blowup chart \(q=t^2(V-Z^2)\), and \(V-Z^2\) does
not vanish identically on the local exceptional component:
setting \(V=Z^2\) at \(t=0\) leaves \(aZ^6\) in the strict
equation. Thus the exceptional part of the pullback
meets either strict lift with multiplicity exactly two
there. The two marked curves alone contribute \(2s\)
to that intersection, so \(s\le1\).

The other endpoint is smooth and there are no unmarked
residual hits. Each numerical row sum is therefore
at most its smooth value two plus
\((1+s)+(-1+s)\le2\), hence at most four. Intersecting
the mate with the sum of the two lifts would give
\(8b\le4(3b/2)\), a contradiction. This also covers the
shared node case, whose correction is smaller. The other
marked ruling is the reversed chart.

Combining the two distinct and two doubled patterns, every
integral two-lift split sextic with normal signed cubic is
excluded in all mate degrees. This is not an exclusion of
nonnormal signed cubics, of endpoint-concentrated one-lift
norms, or of higher-degree two-lift carriers.

#### Removing normality: inverse support and the actual normalization

In the preceding sextic argument the normality assumption
can be removed for both distinct residual rulings and
for a doubled unmarked ruling. The substitute is the
presence of an **actual** mate: every relevant local
branch must carry the inverse support of that equation.

Specifically, at an unmarked point the local support of
the mate on the signed surface is the one lifted quartic
there. A power of its ideal is contained in the principal
mate ideal, and the mate ideal is contained in the curve
ideal. These inclusions persist after completion and
restriction to any formal branch. If a formal plane
branch meets the lifted quartic only at the point, the
restriction of the mate has maximal radical on that
plane, impossible for one equation in a two-dimensional
regular local ring. In the transverse fixed-slice
normal form \(xy+f(w)\), the case \(f=0\) has just such
an extra plane, since the marked curve is one of the
axes at \(w=0\). Thus all unmarked transverse singularities
of a hypothetical mate are isolated \(A_n\), without
assuming global normality. In the two-distinct-unmarked
case this already forces global normality: an integral
hypersurface that is not normal has a singular curve,
which must meet the ample divisor \(T\). In this case
\(S\cap T\) consists of two lifts and two residual conics
each with multiplicity one; its sole possible singular
points on \(T\) are the transverse hits, since the
endpoints are smooth. No singular curve can meet those
isolated singularities.

More generally we can perform the intersection comparison
on the **normalization** of the integral signed cubic,
which is smooth along each lift generically. The pullback
of a hypothetical mate is an effective Cartier divisor.
Above each generic lift there is a unique strict inverse
curve, which maps isomorphically to the smooth original
lift by finite birationality. No extra isolated inverse
point can occur in the support: the pullback of a nonzero
single equation on the normal integral surface has
support of pure codimension one. Thus its cycle is the
same combination \(\lambda D+\mu D'\) on these inverse
curves. The hyperplane degree and \(\lambda+\mu=3b/2\)
are unchanged. On any smooth model of this normalization,
the numerical pullback computes their intersections.
For adjunction one may pull back the original rational
canonical generator, which exists globally because
the signed cubic is a \((2,3)\) complete intersection.
The needed discrepancies are determined in the actual
charts along the strict inverse curves, not by
normality elsewhere.

In particular the simple marked-endpoint node and
\(D_5\) calculations remain unchanged. In the weight-six
case of the simple marked endpoint, normalize the
weighted strict surface before resolving. Its integral
exceptional curve \(E\) is generically smooth in the
strict surface, and is Cartier there near its entire
support (the weight-one chart and the free chart at
weighted infinity). Its finite pullback still has
one exceptional prime with multiplicity one, and
preserves \(E^2=-1\) by the projection formula. The
normalization is an isomorphism at the two smooth
marked points on \(E\), so both incidence vectors are
unchanged. The normalized exceptional curve contracts
to one point on the original normalization because
it is connected and that normalization is finite.
The same numerical self and mutual corrections follow.
The K3 smoothing rank estimate for any unmarked hits
also remains valid, since those isolated Milnor balls
only use the original signed equation and a smoothing
in the full linear system. Thus every distinct residual
ruling configuration is excluded without normality.

For the doubled unmarked ruling, first the conormal
derivative on the lifted conic \(R\) must be nonzero
under a hypothetical mate. Otherwise the signed cubic
is singular along \(R\), and its quadratic normal part
is a binary form on \(N_{R/X}=\mathcal O_R(1)^2\)
valued in \(\mathcal O_R(3)\); the conic is the section
of \(X\) by the two hyperplanes defining its plane.
Each entry of the form is therefore a section of
\(\mathcal O_R(1)\), of degree two, and its determinant
has degree four. At any of the six distinct marked
hits a nonzero determinant gives a formal product
of two planes along \(R\), by splitting the two
nondegenerate normal directions over the parameter
of \(R\). The lift is transverse to \(R\), so belongs
to only one of the two sheets. The other sheet is
forbidden by inverse support. The determinant thus
vanishes at all six hits and is identically zero.
At each hit the coefficient obtained by restricting
the normal form to the direction normal to \(R\) in
\(T\) has a simple zero, by the local \(xy^2\) slice.
A rank-one binary form over the local DVR with
any unit coefficient and determinant zero is a unit
times a square (complete a square after choosing a
unit diagonal entry). Its value on that direction
cannot have odd order. Therefore all entries vanish
at all six hits, impossible for their degree unless
the form is zero, contradicting the nonzero generic
slice coefficient. This proves the derivative
section is nonzero and still has just two zeros
counted with multiplicity.

At a rank-two hit of the doubled conic, the (A_n)
calculation applies again: the only alternative is a
formal product, and the lifted quartic cannot be in
the intersection of its two sheets, because it is
generically smooth on the signed surface (in the
slice coordinates the derivative in the \(x\) direction
restricts to \(y^2\) on the lift). Thus one sheet would
again be forbidden. The rank-one \(D_5\) case is already
isolated. In the rank-zero case the ordinary blowup
chart used above is smooth at the point of the strict
marked lift even without normality of the original.
Normalize the blowup and resolve elsewhere, retaining
this chart. It factors through the original
normalization. Along the lift the local pole of the
original canonical form is exactly the factor
\(y^{-1}\) computed in the smooth chart; elsewhere on
that lift the original surface is smooth. The
Cartier divisor \(q=0\) has the same generic
multiplicities on the original normalization, since
the derivative section is generically nonzero on
\(R\). Its exceptional part still meets the marked
strict lift with multiplicity one. The effective
self-correction is therefore still at most two,
rather than \(30/7\). This finishes the doubled
unmarked ruling with no normality assumption.

#### Normalizing the doubled marked ruling

The last case without normality is a doubled marked
residual ruling with \(L_0=\ell=0\) in the actual cubic
representative above. The two-lift support makes its
nonnormality tractable: after the ordinary blowup, both
lifted quartics belong to the same local sheet of the
normalization, although the other sheet is also present.

Keep the ordinary \(t\)-chart \(v=tV,z=tZ\) of the blowup,
and write the strict equation as
\[
aV^2(V-t^2)+(V-Z^2)B(t,V,Z)=0 .
\]
The actual cubic representative gives \(B(t,0,0)=0\)
identically, with transverse linear part at \(t=0\)
equal to \(dV+cZ\), \(c\ne0\). In particular the strict
equation and all its first derivatives vanish all along
\(V=Z=0\). Its transverse Hessian there is nondegenerate,
with quadratic part at \(t=0\) equal to \(V(dV+cZ)\).
Apply the parametric formal splitting lemma over
\(k[[t]]\), retaining that line as the critical section.
The critical value is identically zero; the resulting
equation is a product \(XY\) up to a unit, with
\[
X=V+O((t,V,Z)^2),\qquad
Y=dV+cZ+O((t,V,Z)^2).
\]
The two marked arcs \(V=t^2, Z=\pm t\) have
\(Y=\pm ct+O(t^2)\), nonzero on either arc. Both must
therefore lie in the sheet \(X=0\). Normalization
commutes with completion here (the local rings are
excellent), splitting the two formal sheets into
smooth planes. In the marked sheet with coordinates
\(t,Y\), the two lifts meet each other with length
one, since the slopes of their \(Y\) coordinates
are opposite and nonzero. Each meets the same
exceptional curve \(t=0\) transversely once. Normalize
the blown-up surface and resolve any remaining
points away from this smooth marked neighborhood;
this is a smooth model of the original normalization.

The rational canonical generator of the original
signed cubic pulls back in this sheet, up to a unit, as
\[
\frac{dt\wedge dY}{tY}.
\]
The factor \(t^{-1}\) is the same blowup residue factor
\(t^2/t^3\) as before, from the ordinary ambient blowup
and multiplicity three. The factor \(Y^{-1}\) is the
residue along the sheet \(X=0\) of the product
equation \(XY=0\). Both pole divisors meet each
strict lift once, because \(t\) and \(Y\) have order
one along those lifts. Elsewhere the original surface
is smooth along the lifted quartics. Thus the
canonical intersection with either strict lift is
\(-2\), and its self-intersection by adjunction is
zero, an increase of two from the smooth marked
baseline. The mutual strict intersection has
decreased by one.

Finally, \(q=t^2(V-Z^2)\). The second factor does not
vanish identically on the exceptional component
met by the lifts: at \(t=0,V=Z^2\) the strict equation
would force \(aZ^6=0\), inconsistent with a curve
on that chart. Hence the exceptional multiplicity
of \(q\) along that component is exactly two. The
actual divisor of \(q\) on the original normalization
contains both lifted curves with multiplicity one
and has effective residual support. Their exceptional
incidence vectors agree, so positivity of the
numerical pullback bounds their common self and
mutual correction \(s\) by \(2s\le2\), as in the
normal triple-point case. The total numerical row
sum is at most
\[
2+(2+s)+(-1+s)\le5 .
\]
The other endpoint is smooth, and there are no
unmarked residual hits. Thus \(8b\le5(3b/2)\),
a contradiction.

Combining the residual patterns, **no integral
two-lift split sextic has a mate of any degree in
characteristic zero**, with no normality assumption
on its signed surface. The scope is the two-lift
degree-six norm case. Endpoint-concentrated one-lift
norms, higher degree, and nonsplit carriers are not
excluded by this classification.

### One-lift sextics: the conormal zero budget

Consider instead an integral one-lift split sextic in
characteristic zero. Orient the signed cubic \(S\subset X\)
so it contains \(D\), not \(D'\). The one-lift conductor
formula implies that for any actual mate the nonzero
restriction \(Q|_C\) is a binary monomial of degree eight.
Assume first that \(S\) is generically smooth along \(D\).
The normal derivative of the signed equation then has a
zero divisor on \(D\), supported at the actual singular
points along it. We describe the degree and multiplicity
budget of those zeros before applying numerical pullback.

In the first chart take \(t=x_1/x_0\),
\(u=z/x_0-t^2\), \(v=x_2/x_0-t^3\). The cover equation
gives \(x_3/x_0=t^4+2tv-2t^2u-u^2\). At the other
endpoint take \(T=x_2/x_3\), \(U=z/x_3-T^2\),
\(V=x_1/x_3-T^3\). Modulo the square of the ideal of \(D\),
\[
U=-t^{-4}u,\qquad V=t^{-6}v-4t^{-5}u,
\qquad V-4TU=t^{-6}v .
\]
Thus the conormal splits into degrees \(-4,-6\), with
the indicated generators. Twisting by the cubic degree
adds twelve on \(D\), giving derivative components of
degrees eight and six. If the degree-six component is
nonzero, the common zero divisor has length at most six,
including multiplicities.

If that component vanishes identically, the degree-eight
component has a constrained source. Write
\(Q|_C=s^{8-i}t^i\), up to nonzero scalar, with
\(0\le i\le8\), in binary coordinates. The signed restriction
fixes \(P|_C=-s^{10-i}t^{i+2}\) with the same scalar.
Choose monomial lifts for an initial signed cubic of
weight \(i+2\) under the torus preserving \(D\); the
weights of \(x_0,x_1,x_2,x_3,z\) are \(0,1,3,4,2\).
All variations at fixed restrictions are \(q\) times
the four downstairs coordinates, \(zq\), and the
three cubics
\[
x_0^2x_2-x_1^3,qquad x_0x_2^2-x_1^2x_3,qquad
x_1x_3^2-x_2^3 .
\]
Indeed the seven downstairs variations have distinct weights,
and restriction of cubic forms
downstairs achieves all thirteen binary weights, so
they span its kernel. Degree-two restriction downstairs
has only the kernel spanned by \(q\).
The coefficient of \(v\) for these variations is
\(t,t^2,t^4,t^5\) from the four \(q\) multiples,
\(t^3\) from \(zq\), and \(1,0,t^6\) from the
three cubics. This follows from \(q=tv-2t^2u\) to first
order; the middle cubic has \(u\)-coefficient \(2t^4\).
Thus one can cancel the degree-six component in its
initial weight, and the remaining freedom is only
the middle cubic. The degree-eight component is
of the form \(\alpha t^i+\beta t^4\) on this chart,
homogenized to degree eight. If nonzero, it has
at most five distinct zeros on the parameter line:
when \(i=0,8\) there are at most four torus roots
and one endpoint, and otherwise at most three torus
roots and two endpoints. A monomial has at most two
distinct zeros. This proves the bound of six distinct
singular points in all generically smooth cases,
without assuming that the zeros are simple.

If the singularities along \(D\) are Du Val, intersecting
a hypothetical mate with its inverse curve on the
normalization gives a precise correction demand.
The mate has cycle \(\lambda D\), with
\(\lambda=3b/2\) by hyperplane degree. Adjunction on a
resolution crepant along \(D\) gives
\(\widetilde D^2=-2\), by the canonical form of the
\((2,3)\) complete intersection. Thus numerical pullback
would need
\[
\sum_{p\in D\cap\operatorname{Sing}S}\operatorname{corr}_p
=2+\frac{4b}{\lambda}=\frac{14}{3}.
\]
The calculation is local along \(D\), so no normality
assumption is needed elsewhere. In particular if every
hit is \(A_1\) or \(A_2\), its correction is at most
\(2/3\); six such points give at most four. This rules
out every mate degree in the mild sector, even when
the degree-six component vanishes.

A stronger comparison uses the length rather than the
number of derivative zeros. Suppose all singular points
on \(D\) are \(A_n\) and the degree-six component is nonzero.
At a hit of type \(A_n\) write its local equation
as \(xy=z^{n+1}\). The strict smooth lift meets just one
exceptional component once, as above. If this is vertex
\(j\), let \(r=\min(j,n+1-j)\). Along that component
the orders of \(x,y,z\) are \(j,n+1-j,1\), respectively,
from the toric resolution. Their restrictions to the
lift have at least those orders. The Jacobian ideal
\((x,y,z^n)\) thus vanishes along the lift to order at
least \(r\); this is a lower bound on the common conormal
zero order because differentiation along the lift itself
is zero. Its inverse Cartan correction is
\(r-r^2/(n+1)\). Consequently \(M=\sum r\le6\), and if
there are \(k\) hits then \(k\le M\). The K3 smoothing
bound on the marked \(A_n\) configurations gives
\(\sum n\le19\) without an assumption away from the lift.
Cauchy–Schwarz now bounds the total correction by
\[
M-\sum\frac{r^2}{n+1}\le
M-\frac{M^2}{19+k}\le\frac{114}{25}<\frac{14}{3};
\]
the second bound uses \(k\le M\le6\).
This rules out all \(A_n\) singularity sizes on this
conormal stratum, including multiple derivative zeros.

If the common derivative zeros are reduced, one can
apply the same estimate without assuming the local
types or a nonzero degree-six component. At a simple
zero the Hessian pairs the tangent of \(D\) with a
nonzero normal direction. A singularity with such
rank is a node or has the fixed rank-two splitting
\(xy+f(w)\); if \(f=0\) the lift cannot lie in the
singular curve, since it is generically smooth on
the original surface. The other formal sheet then
violates inverse support on the actual mate,
including at a marked endpoint: the one-lift signed
complete intersection has sole curve support \(D\).
Thus it must be \(A_n\), with the lift outside the
Hessian radical and meeting an end. The at most six
simple hits have \(M=k\le6\) and obey the same bound.

The unresolved one-lift sectors include the multiple
zeros of the degree-eight binomial when the degree-six
component is identically zero, non-\(A_n\) corrections
at multiple zeros, and a signed cubic singular
generically along \(D\). This is separate from the
two-lift sextic exclusion.

### Arithmetic control and comparison of traits

For the actual char-three pair A=x1³−x0²x2, G=x0x3³−x2⁴, both endpoint algebras are O[Y]/Y³. At 0 choose Y=x3−t⁴; r=t⁴−Y. At infinity choose Y=x1−t³; r=t⁴−tY. In either case z=t²+t^(j−2)Y+t^(2j−6)Y² with j=0 or 1 respectively. The multiplication matrix in basis 1,Y,Y² is triangular with these coefficients in its successive lower diagonals. The potential smallest two-minor is zero by equality of the two diagonal/off-diagonal products. The minimum over all minors is −6 or −4, respectively, from the Y² coefficient; hence (δ0,δ∞)=(6,4). This is a calculation for the actual supported char-three pair, not a char-zero lift or its lower-root defect.

If an actual supported mixed-characteristic trait has compatible finite free endpoint lattices over R[[t]], with R its coefficient DVR, 2 invertible and ε uniformly nilpotent, the same finite expansion produces a matrix over R[[t]][1/t]. Reducing modulo the parameter can only increase t-valuations of its minors, so δ_special≤δ_generic. This statement needs the compatible actual lattice hypothesis, not merely specialization of the reduced support or an abstract Artin algebra. It does not require the conductor to commute with base change. It supplies a lower bound in characteristic zero, not the upper bound needed for a contradiction, and does not identify the different endpoint kernel of the prescribed Frobenius-root specialization.

The compatible-lattice hypothesis is automatic for a flat actual projective complete-intersection trait over a complete DVR at odd residue characteristic if both geometric fibers have sole support the fixed relative C. The whole relative ideal of C is then uniformly nilpotent on the trait, by the support equality and Noetherianity. The completed local algebra is finite over R[[t]] by its finite nilpotent filtration. The coefficient uniformizer is regular by flatness, and t is regular modulo that uniformizer by the special-fiber Cohen–Macaulay CI and its sole smooth reduced support. This gives a finite free module over the regular ring R[[t]]. Its two relevant completed fiber lattices are obtained over k[[t]] and Frac(R)[[t]], respectively. This does not apply without further checks to the lower-root closures with embedded endpoint defects.

The comparison uses the conormal moment of the actual generic CI
algebra, as in [the full socle budget](../../results/full_conormal_socle_budget.md),
but the Smith valuations need the actual endpoint lattices. A next
test is to compute both lattices in a declared actual equation family,
then compare these capacities with the onset for the *same*
conductor. Neither the generic algebra nor the arithmetic reduction
alone determines the valuations; this comparison supplies no
incompatible bound for all defining pairs.

### All-minors capacity and a cyclic control

Keep the completed endpoint lattice A over O=k[[t]] and the branch root z as above. At a chosen endpoint suppose ε=r−t^4 belongs to t^u J, u≥0 (the case u=0 always holds). Because A/J=O, divisibility by t^u in A is enough: J is O-saturated. Choose a basis adapted to K_j=ann_A J^j, and give basis vectors in K_(j+1) outside K_j level j. List the levels i_1≤…≤i_n. Put S_k=Σ of the k largest levels minus Σ of the k smallest and S_0=0. Since ε^l/t^(ul) belongs to J^l, it takes level b vectors into the span of levels ≤b−l. Multiplication by z thus has matrix entry from level b to level a of valuation at least 2−(4−u)(b−a) if a≤b and u≤4, and zero if a>b. Every term of a k-minor has the same sum of row levels and column levels. Therefore, for 0≤u≤4,
  δ_i ≤ max_{0≤k≤n} ((4−u) S_k−2k).
For u≥4 the root is integral, giving δ_i=0. The same bound with levels from ann_A(η^j) holds for the specific η=ε/t^u; use its actual ranks, not a generic conormal Hilbert vector without comparison. Summing smaller-level terms removes much of the loss in the column-only bound. As S_k≤k(n−k) (nonzero levels from J have no internal gaps), a level-independent upper bound is max_k ((4−u)k(n−k)−2k). No condition on cancellation of minors is assumed.

For the explicit cyclic control A=O[η]/η^n, ε=t^uη, the latter bound is exact in characteristic zero. In the basis 1,η,…,η^{n−1}, take the bottom-left k×k minor. Its valuation is 2k−(4−u)k(n−k) and its coefficient is
   D_k(m)=det[ binom(1/2,m+i−j) ]_(0≤i,j<k), m=n−k.
Over Q(α), D_k(m) for binom(α,·) equals ∏_(i=0)^(k−1) [(α+i) falling m] i!/(m+i)!, nonzero at α=1/2. For verification the bare determinant satisfies Desnanot–Jacobi
D_k(m)D_(k−2)(m)=D_(k−1)(m)^2−D_(k−1)(m−1)D_(k−1)(m+1).
The product has D_0(m)=1, D_1(m)=binom(α,m), D_k(0)=1, and its cross-neighbor ratio at k−1 is m(α−m)/[(m+k−1)(α+k−1−m)]; subtract from 1 to get the proposed ratio on the left. This proves the formula by induction. In particular δ_i=n(n−1) for u=0. In an actual lattice, the cyclic model applies when η generates A/tA: Nakayama lifts the n powers as a basis, and η^n=0 by generic nilpotence and t-regularity. Otherwise no cyclic assumption is licensed. The char-three control above shows cancellation can invalidate particular extremal minors in residue characteristic without contradicting the upper bound.

There is a direct actual endpoint control. If a member of the
pair is smooth there and its normal linear form is independent of
that of \(\epsilon\), then \(t,F,\epsilon\) are formal coordinates.
On the smooth local surface \(F=0\), sole support means the mate
cuts a unit times \(\epsilon^n\). Thus this actual completed
intersection is the cyclic control with \(u=0\), not a deduction
from an abstract generic normal type. Dependent normal linear
forms do not identify the actual completed lattice.

### A first conditional comparison with actual postulation

Assume the smaller integral characteristic-zero carrier is nonsplit in the fixed quadratic cover. If ε belongs to t³A at BOTH endpoints, then δ≤2 floor((n−2)^2/4) for n≥2 from the uniform level bound. If ε belongs to t⁴A at both endpoints, δ=0, already contrary to the original global lower bound even without nonsplitting. These are endpoint divisibilities of the actual quadratic function, not consequences of generic normal order.

The t³/t³ case contradicts nonsplit postulation in three infinite skew-degree sectors: a=5,b≥16; a=6,b≥36; a=7,b≥92, always with 4|ab. Indeed b=2s, q_b=s−1, so the nonsplit lower bound is 2[binom(s+1,3)−binom(s+1−a,3)]+a−1. Subtract the weaker upper (as/2−2)^2/2. The differences for a=5,6,7 are respectively (15s²−160s+336)/8, (3s²−60s+146)/2, (7s²−336s+928)/8. Each is positive and increasing from s=8,18,46 respectively. No assertion that either divisibility condition holds for every actual pair, or even that any characteristic-zero candidate in these specified degrees passes the antecedent.

Next bounded question: in a declared order-one family, characterize which actual endpoint lattices force any t-divisibility of ε, and whether the same family stays nonsplit. A first-symbol tangent can suggest divisibility modulo J² but does not prove it in A. Use all minors or an independently justified cyclic coordinate model; compare the same endpoint conductor at both ends with the global postulation. A failed divisibility test redirects the route toward exact truncated matrices, not toward strengthening the unrelated Frobenius defect.

### Actual carriers with two divisible endpoint functions

The endpoint divisibility test is not vacuous on actual carrier sources.
Write R=2x_1x_2−x_0x_3, q=x_0x_3−x_1x_2 and
K_0=R x_0²−x_1⁴, K_∞=R x_3²−x_2⁴. These both vanish on the marked C.
For a≥7, m=a−4, set
    A=x_0^m K_0, B=x_3^m K_∞,
    D_7=q² x_0 x_1 x_2,
    D_a=q² x_1² x_2² x_0^(a−8), a≥8.
Take F=λA+μB+νD_a with λμ nonzero.

At p_0, work on x_0=1 with (t,z,w)=(x_1,x_2,x_3).
Modulo t, F is −λw plus a term divisible by w^m, while D_a vanishes.
Thus F is smooth at p_0 and w lies in (t) in its completed local ring:
the remaining coefficient of w is a unit. Then q=w−tz is in (t),
so B is in (t^m) and D_a is in (t³) for a=7 or (t⁴) for a≥8.
Consequently ε_0=(R/x_0²)−t⁴=K_0/x_0⁴ belongs to (t³) or (t⁴),
respectively. At p_∞ exchange coordinates and use t=x_2/x_3.
The role of w is x_0/x_3, again in (t); q is again in (t).
The factor x_0 or x_0^(a−8) in D_a adds no negative order, so the
same divisibility holds at p_∞. These congruences hold in the actual
completed carrier before reducing by any mate, hence also in a
hypothetical full equation lattice.

The family has integral general members in characteristic zero.
A and B have no common surface factor: K_0 is irreducible, seen on
x_0=1 as linear monic in w up to sign, with no component at x_0=0;
K_∞ is its distinct reversed counterpart, and neither shares the
opposite coordinate hyperplane. The linear system is not composed
with a pencil. On K_0=0 it traces a dense subset of the line A=0
in parameter-image coordinates (A:B:D_a). Indeed B/D_a is
nonconstant there: at (t,z,w)=(1,0,−1), B≠0,D_a=0, and D_a is
not identically zero on K_0=0. The image also has points with A≠0.
Thus the image dimension is at least two, and Bertini irreducibility
with no fixed surface applies. The general member is not in the
smooth-along-C sector: on x_0=1 substitute z=t³+v,w=t⁴+h.
The first normal forms of K_0,K_∞ are respectively
2tv−h and −t⁸(2tv−h), while D_a has normal order at least two.
Hence F has first form (λ−μ t^(4m+8))(2tv−h) and is singular at the
nonzero roots of that displayed scalar, though generically regular along C.

For degree seven these actual carriers are nonsplit whenever integral
and \(\lambda\mu\ne0\). On the smooth branch quadric \(R=0\) with
\(x_0=1\) one has \(w=2tz\) and
\[
 F|_{R=0}=t^3(-\lambda t-8\mu z^7+\nu z^3).
\]
The graph of the second factor has a simple generic point on the
dense torus, giving an odd valuation of \(R/x_0^2\) in the carrier
function field. This proves nonsplitting without assuming generic
normalization smoothness away from the endpoints.

The degree-seven endpoint bound improves in the actual pair algebra.
At the first endpoint set \(v=z-t^3\); the smooth carrier has
parameters \((t,v)\), and a sole-support mate is a unit times
\(v^n\) there, since this is a regular local UFD and its divisor
has just that support. Thus the actual lattice is
\(k[[t]][v]/(v^n)\). At the other endpoint use reversed coordinates
and the corresponding normal parameter. From \(w/t\equiv2z\pmod t\)
one obtains at the first endpoint
\[
 (\epsilon_0/t^3)\bmod t=(8\mu z^7-\nu z^3)/\lambda,
\]
and at the reversed endpoint \(8\lambda z^7/\mu\): the \(x_0\) factor
of \(D_7\) contributes one more \(t\) there. Indeed
\(q/t\equiv z\pmod t\), while the reversed mate term contributes
\(-8z^7\) times its scalar. In either case \(\epsilon/t^4\) lies in
\((v)k[[t]][v]/(v^n)+t^{-1}(v^3)k[[t]][v]/(v^n)\).
In the square-root expansion the coefficient of \(v^j\) therefore
has valuation at least \(2-\lfloor j/3\rfloor\). Each negative
power of \(t\) costs at least three powers of \(v\).
The all-minors comparison now gives
\[
 \delta_i\le\max_{0\le\ell\le n}
 \bigl(\lfloor \ell(n-\ell)/3\rfloor-2\ell\bigr).
\]
Here the sum of the shifts in a product in an \(\ell\)-minor is
bounded by \(\ell(n-\ell)\), and rounding down after summation
only weakens the bound.

A degree-seven carrier thus cannot have a sole-support mate.
The mate degree is \(b=4s\) by degree exhaustion, and \(s\ge2\)
by the low-degree exclusions. For \(s=2,3\) nonsplit
postulation gives lower bounds \(26,76\) against upper bounds
\(10,36\). For \(s\ge4\) the lower bound is
\(28s^2-98s+118\), strictly larger than the upper bound
\((7s-6)^2/6\) given by the continuous quadratic maximum.
For \(a\ge8\) both endpoint conductors would vanish by
\(t^4\)-divisibility, contradicting global postulation after ordering
the degrees. Thus every integral member of the indicated
\(\lambda\mu\ne0\) family in degrees \(a\ge7\) is excluded for every
mate degree. This is a statement about actual carrier sources,
not about all carriers in those degrees. The next structural test
is whether other source conditions force enough endpoint
divisibility, or whether exact matrices can replace that assumption.

### A weighted endpoint test on the actual carrier

Work at either standard endpoint, on its affine chart, reverse coordinates at infinity. Let (t,z,w) be chart coordinates with C=(z−t³,w−t⁴) and `e=2tz−t⁴−w`. For an actual carrier F containing C, suppose ∂_w F is a unit at the endpoint. Set v=z−t³ and solve w=w_F(t,v) formally. In the completed carrier, any actual sole-supported mate has equation unit·v^n, n=ab/4, by factorization in the regular power-series ring with support v=0; hence the pair lattice is O[v]/v^n. The value
    F(t,v+t³,2t(v+t³)−t⁴)
equals e|_F times a unit, by subtracting the identically zero F(t,v+t³,w_F) and using the nonzero derivative. Thus the weighted jet condition i+γj≥4 for all t^i v^j occurring in e|_F (γ fixed nonnegative rational) is directly a linear vanishing test on F after this substitution. Unit multiplication preserves the filtration. If γ>0 the prohibited jet region is finite; at γ=0 the substitution itself is still polynomial and tests t^4 divisibility.

Under this condition coefficient j of e/t^4 has t-valuation at least −γj; coefficient zero is absent because e vanishes on C. The finite square-root expansion preserves these bounds by convolution, with +2 from the prefactor t². Therefore every k-minor in the cyclic basis has valuation at least 2k−floor(γ k(n−k)), giving δ_i≤max_k(floor(γ k(n−k))−2k). This is an actual coefficient condition, not a consequence of first normal order. For a smaller integral nonsplit carrier, γ_0+γ_∞<16/a is sufficient to exclude all sufficiently large mate degrees: for fixed a the nonsplit lower bound is (a/4)b²+O_a(b), while the upper bound is at most (γ_0+γ_∞)a²b²/64. The exact finite inequalities remain preferable for individual degrees.

### Degrees five and six in the same constructed family

Use the same A=x_0^(a−4)K_0 and B=x_3^(a−4)K_∞, with D_5=q²x_0 and D_6=q²x_1x_2. Take F=λA+μB+νD_a with λμ nonzero. The completed endpoint has w=tW and q=t(W−z); F modulo t is a unit times w. Set e=t^m E, m=a−4 (the divisibility follows as before), so W=2z−t³−t^(m−1)E.

For a=5, divide the equation by t. On x_0=1 modulo t³,
  (λ+μz⁴)E = 2μ z⁵−νt(z−E)².
Thus the coefficients of E at t-orders 0,1,2 vanish to z-orders at least 5,2,3: solve successively, using that z−E_0 has order one. At infinity exchange λ,μ and replace the final term by −νt² W(W−z)²; there E_1=0, E_0 has order ≥5, and E_2 order ≥3. Replacing z by v+t³ doesn't change these low t-orders. The t-integral remainder of e/t⁴ lies in (v) because e vanishes on C. Thus the weighted test applies with γ_0=1, γ_∞=3/5.

For a=6, the same calculation at either endpoint (swap λ,μ) gives modulo t²
  λE=μ W² z⁴−ν t z(W−z)², W≡2z−tE.
So E_0=4μz⁶/λ and E_1=−16μ² z^11/λ²−νz³/λ. Hence the pole part of e/t⁴ is in t^−2(v⁶)+t^−1(v³); both slopes are 1/3. The remaining integral part lies in (v).

The actual carriers are integral on a nonempty open by the same Bertini argument. For a=6 the ratio B/D on K_0=0 has a pole at t=1,z=0,w=−1, and D is not identically zero there. For a=5, that ratio is −1 there and is zero at t=1 and a root of z²+2z−1 (w=−z², q=z−1 nonzero). Thus the linear system in each degree has image dimension two and no fixed surface. The first normal form is still (λ−μt^(4m+8))(2tv−h), so general members have singular points on C, although endpoints are smooth.

Nonsplitting holds for integral members in the following open. On the smooth branch quadric R=0, set w=2tz. In degree five restriction is t(−λt³+ν t z²−2μ z⁵). The cubic has nonzero constant over k(z), with discriminant not identically zero (z^10 coefficient nonzero since λμ≠0). In degree six restriction is −t²(λt²−νt z³+4μz⁶); require ν²≠16λμ, giving two distinct nonzero torus roots after division by z³. Each has a simple torus component of the branch divisor on the actual integral F, hence r is nonsquare on F.

All mate degrees fail. For a=5 write b=4s with s≥2 (lower excluded). At s=2,3 the lower lengths are 24,74 versus upper at most 22,62 by slopes 1,3/5. For s≥4 even the weaker bound using slope 1 at both gives (5s−2)²/2, less than the lower 20s²−50s+44 (difference (15/2)s²−40s+42 positive and increasing). For a=6 write b=2s, s≥3; s=3,4,5,6 lower lengths are 13,25,45,75 versus upper at most 0,6,12,24. For s≥7 the lower 6s²−36s+75 exceeds (3s−6)²/6 (difference (9/2)s²−30s+69 positive and increasing). These are exclusions on actual carrier families, not assertions covering all quintics or sextics.

### How large is the simultaneous endpoint source?

For this dimension count assume the characteristic is different from two.
For integer U≥2 let L_(a,U)⊂H⁰(I_C(a)) be the linear source whose two substituted polynomials on the quadratic-coordinate graphs are divisible by t^U. Consider its open locus where the solved normal partial is nonzero at both endpoints. This open is nonempty if and only if a≥U+4. On the first chart, give (t,v) weights (1,3). Substitution w=2tv+t⁴,z=v+t³ preserves the homogeneous torus weights. The weight-four piece of any F in this source is
`Ax_0^(a−4)x_1⁴+Bx_0^(a−2)x_1x_2+Cx_0^(a−1)x_3`;
omit unavailable monomials if a<4. Along C, A+B+C=0; in its substituted polynomial the coefficient of tv is B+2C, which must be zero since U≥2. The solved normal partial at p_0 is C≠0. Thus a≥4 and the piece is C times x_0^(a−4) K_0 up to sign. In the reverse graph chart its value has t-adic order exactly a−4: the factor w^(a−4) contributes that order with leading coefficient (2v)^(a−4), and K_0 in that chart has leading term −v⁴. Other weights cannot cancel because reversed torus weights are 4a minus the original ones. Thus a−4≥U. Conversely take A+B from the actual carrier family, with both coefficients nonzero; on each branch graph the marked term vanishes and the opposite one has order ≥a−4, and the solved partials are nonzero.

The source has exact codimension 2Ua inside H⁰(I_C(a)) when a≥2U+2. To count, first work in the full degree-a polynomial space. A monomial x_0^i x_1^j x_2^k x_3^l has first substituted leading term 2^l t^(j+l)v^(k+l) and higher t-orders. Its lowest order in the reverse chart is i+k, and these two orders sum to a. Monomials contributing to the first U jets at the two ends are therefore disjoint sets. In either chart every leading pair (d,r) with 0≤d<U, 0≤r≤a occurs: choose l=min(d,r), k=r−l, j=d−l, and i=a−d−k. Choosing one column for each (d,r) gives an invertible triangular coefficient matrix ordered by the initial t-degree, since higher-order terms still have v-degree ≤a. The rank of simultaneous jets on all forms is thus 2U(a+1). To restrict to forms through C, the curve evaluation rows are single torus-weight evaluation rows. The rows at weights 0,…,U−1 and 4a−U+1,…,4a are already given by the v=0 coefficients of the two jet maps. Every weight from U through 4a−U has a monomial missing from both jet maps: choose d between U and a−U and r between 0 and a with weight d+3r, and use the same exponents above. Such choices exist throughout the interval because d ranges over at least three consecutive integers. Those middle curve rows are independent modulo the two jet maps, as they have distinct weights and independent coefficients on missing columns. Therefore the lost rank on I_C(a) is exactly 2U; this proves the claim.

In characteristic zero the all-mate exclusion from U=4 concerns the whole endpoint-smooth part of this actual linear source, not only the constructed A,B,D pencil. For a≥10 the codimension is 8a. For every a≥8 the constructed integral examples ensure that this source has a nonempty open of integral members regular at the endpoints. A high-dimensional source with this restriction is not coverage of arbitrary carriers; the live gap is which geometric hypotheses force these endpoint jets, or a capacity inequality that does not require them.

## 9. Why the extracted branch need not be Gorenstein

One exact local control suffices to test that possible shortcut; no
classification is proposed. Near \(p_a\), put
\(t=b,x=c-b^3,y=d-b^4\). The curve has ideal \((x,y)\), and the
actual cover equation is \(z^2=t^4+2tx-y\). Choose the local supported CI
\[
A_p=k[[t,x,y]]/(x^3,y-tx)\simeq k[[t,x]]/(x^3).
\]
On its positive primary lift set \(w=z-t^2,u=x-2tw\). The full lift is
\[
B_p=k[[t,u,w]]/(tu-w^2,uw,u^2),\quad
x=u+2tw,\quad z=t^2+w.                                                \tag{8}
\]
It is free over \(k[[t]]\) with basis \(1,w,u\). The equations give
\(x^2=4t^3u,x^3=0,z^2=t^4+tx\). After inverting t this is the
length-three positive generic branch. Freeness removes any embedded
endpoint contribution, proving it is the full primary extraction.
But \(B_p/tB_p=k[u,w]/(u,w)^2\) has socle dimension two, so B_p
is not Gorenstein.

The inclusion with bases \(1,x,x^2\) and \(1,w,u\) has determinant
\(8t^4\), giving \(\delta_p=4\). Direct multiplication gives
\[
\mathfrak c_p=(t^4,x+4t^3)B_p,\quad
A_p/\mathfrak c_p=k[[t]]/(t^4),\quad
B_p/\mathfrak c_p=(A_p/\mathfrak c_p)[z]/(z^2).
\]
Its attachment length is \(2\cdot3+2\cdot4=14\).
Thus even both Gorenstein boundary algebras in (2) coexist with a
non-Gorenstein branch. This is a local mechanism control, not a global
STCI construction or a counterexample to a future global theorem.

Finite duality identifies the conductor with the canonical module of
W, up to the pulled-back dualizing line of Y. It need not be a Cartier
divisor. Consequently the previous Gorenstein-source obstruction cannot
be applied to every hypothetical pair merely by taking its primary lift.

## 10. Automatic descent, and what a construction would have to add

Conversely take **any** saturated pure W in Q3 with reduced support D,
and write \(I=I_W\subset E,J=I\cap S\). The element z is regular on
E/I. The ideal \(I\cap\sigma I\) is invariant; averaging separates
an element \(p+zq\) into p and zq. Both belong to I; z-regularity
then gives \(p,q\in J\). Therefore
\[
I\cap\sigma I=JE,\qquad W\cup\sigma W=\pi^{-1}(\operatorname{Proj}S/J).
                                                                         \tag{9}
\]
The extension \(S/J\to E/JE\) is finite free with Gorenstein fibers,
so its homogeneous ring is Gorenstein if and only if the base ring is.
Thus an **arithmetically Gorenstein conjugate union** gives an AG image
in P3; a codimension-two AG ideal in S is a complete intersection.
There is no extra descent condition to impose after constructing such
a union. Symmetrizing a failed source, however, leaves its image ideal
J unchanged and cannot repair it.

Already \(U_0=D\cup D^-\) has Cartier attachment
\(2p_a+2p_d\) on each branch. Locally on a=1 its ideal is
\((c-b^3,z^2-b^4)\); the endpoints are plane tacnodes. Nevertheless
\[
\omega_{U_0}|_D=\mathcal O_{\mathbf P^1}(2),\qquad
\mathcal O_{U_0}(1)|_D=\mathcal O_{\mathbf P^1}(4),
\]
so it is not subcanonical with an integral hyperplane twist. Also
\(\pi_*\mathcal O_{U_0}=\mathcal O_C\oplus\mathcal O_C(-1)\), whence
\(h^0(\mathcal O_{U_0}(1))=6>5\). It is not ACM; its genus is three.
Local Gorenstein attachment thus does not supply the required global
polarization and section ring.

The checked construction literature supplies no automatic operation
meeting those conditions:

- [Manolache, Theorem 2.10, Lemma 2.11 and Remark 2.12](https://imar.ro/journals/Revue_Mathematique/pdfs/2007/4/manolache.pdf)
  prove Gorensteinness for supplied linkage extensions, identify their
  canonical twists, and distinguish actual embedded extensions from
  their abstract counterparts. Embedded extensions need not exist.
  Canonical-module attachments can accommodate non-Gorenstein branches;
  insisting on Cartier attachment in a Gorenstein union would force
  each CM branch itself to be Gorenstein.
- [Hartshorne, Proposition 3.1](https://arxiv.org/pdf/math/0301163)
  constructs AG divisors of class \(tH-K_X\) on suitable ACM surfaces.
  A locally CM surface in this smooth Q3 is Cartier, of class eH,
  and has \(K_X=(e-3)H\). The required divisor becomes an ordinary
  hypersurface section, whose section lifts to Q3. The missing supported
  section remains a global equation problem; the construction does not
  produce it here.
- [Casanellas–Drozd–Hartshorne, Theorem 6.1 and Remark 6.3](https://arxiv.org/pdf/math/0307378)
  place ACM curves on Q3 in the Gorenstein liaison class of a CI.
  This does not preserve the prescribed support, choose the conjugate
  as the residual partner, or construct the desired union.


## 11. A common graded mechanism: one extra homogeneous module generator

The degree-one bound in §8 is a special case of the following statement. This generalization is characteristic free and does not require the Gorenstein curve ring to be a complete intersection.

**Theorem.** Let A be a two-dimensional standard graded Gorenstein k-algebra, with canonical module \(\omega_A=A(e)\). Let \(A\subset B\) be a nontrivial finite graded extension which is birational on the full total quotient algebras. Assume:

- \(B=A+Aw\) as an A-module, for a homogeneous element w of positive degree d;
- B has no irrelevant torsion, is locally Cohen–Macaulay away from the homogeneous vertex, and B/A has finite projective support.

Let \(\mathfrak c=\operatorname{Hom}_A(B,A)\) in the common total quotient algebra, \(T=A/\mathfrak c\), \(\Delta=\operatorname{Proj}T\), and \(\delta=\ell\Delta\). Then T is a nonzero one-dimensional standard graded CM ring, and
\[
0\longrightarrow T(e-d)\longrightarrow\omega_T
\longrightarrow E(-d)\longrightarrow0, \qquad
E=\operatorname{Ext}^1_A(B,\omega_A),
\tag{10}
\]
where E has finite length. If \(h_0,\ldots,h_s\) is the h-vector of T and \(H_\Delta(n)=\dim_k T_n\), extended by zero for negative n, then
\[
s\ge e-d+1,\qquad
\delta\ge \max\{1,e-d+2\},
\tag{11}
\]
and
\[
H_\Delta(n)+H_\Delta(e-d-n)\le\delta
\quad\text{for every integer }n.
\tag{12}
\]

**Proof.** Since B is generated by 1 and w as a module, an element a of A satisfies aw∈A if and only if aB⊂A. Thus
\[
0\to A\to B\to T(-d)\to0.
\]
Birationality, rather than a domain assumption, identifies \(\operatorname{Hom}_A(B,A)\) with the actual conductor: after total quotient localization, every map is multiplication by its value on 1. The same observation identifies
\(\operatorname{Hom}_A(B,\omega_A)=\mathfrak c(e)\).
No normality or reducedness of A or B is required.

Nontriviality gives T≠0. The quotient has dimension at most one because its projective support is finite. The local-cohomology sequence, \(H^0_{\mathfrak m}(B)=0\), and \(H^1_{\mathfrak m}(A)=0\) give \(H^0_{\mathfrak m}(T)=0\). Consequently T cannot be a nonzero finite-length module; its dimension is exactly one and it is CM.

Apply \(\operatorname{Hom}_A(-,\omega_A)\). A dimension-one module has no nonzero homomorphism into the two-dimensional CM canonical module, whose associated primes are all minimal, and canonical duality for the CM quotient gives \(\operatorname{Ext}^1_A(T,\omega_A)=\omega_T\). The relevant exact sequence is
\[
0\to\mathfrak c(e)\to A(e)\to\omega_T(d)
\to\operatorname{Ext}^1_A(B,\omega_A)\to0.
\]
Taking the quotient of the first inclusion and shifting by −d proves (10). At every nonvertex point B is MCM over the local Gorenstein ring A, so this Ext¹ vanishes there. It therefore has finite length.

After extending the ground field if necessary, choose a regular linear form ℓ on T. The Artinian reduction has h-vector \(h_0,\ldots,h_s\), with every \(h_i\ge1\) for 0≤i≤s, and
\[
T=\bigoplus_i k[\ell]\bigl(-i\bigr)^{h_i},\qquad
\omega_T=\bigoplus_i k[\ell]\bigl(i-1\bigr)^{h_i}.
\]
In particular \(\operatorname{indeg}\omega_T=1-s\). The nonzero unit of T gives an element of degree d−e in the left side of (10), so d−e≥1−s. Summing the h-vector proves (11). Finally
\(\dim_k(\omega_T)_j=\delta-H_\Delta(-j)\).
Apply the injection in (10) at degree j and substitute n=j+e−d to obtain (12). All arguments commute with ground-field extension, so the result descends to the original field. \(\square\)

For a CI of surface degrees α,β in P³, e=α+β−4. Taking d=1 gives precisely \(\delta\ge\alpha+\beta-3\) and the inequality in §8. More generally, an AG curve in any projective space has the same mechanism with its actual canonical twist e. One algebra generator is insufficient: B=A[w] can require independent higher powers of w as module generators, and then B/A need not equal T(−d).

If s=e−d+1, the faithful canonical element in (10) lies in the initial degree of \(\omega_T\); this is the maximal-degree Cayley–Bacharach case in [Kreuzer's canonical-module criterion](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7DC79E96BB5A7CBA61D74E9F5835E927/S0008414X00045843a.pdf/div-class-title-on-the-canonical-module-of-a-0-dimensional-scheme-div.pdf). If the inequality for s is strict, (12) is still proved, but that stronger maximal-degree property is not established.

This isolates the geometric information shared by the projected source and the arbitrary-pair cover. An extra polarized section becomes regular upstairs; the conductor records its failure to descend. Local duality controls the boundary algebra, while the canonical twist controls its global postulation. The non-Cartier obstruction for the explicit characteristic-zero source and the incompatible adjunction in its odd Frobenius powers are additional tests on that source. Neither is automatic for an arbitrary extracted branch, as §9 demonstrates.

The common theorem describes the boundary of an extra polarized section. In the quadratic application, §8.1 adds actual ambient equation information to its Hilbert inequality; §12 adds an independent extremal embedding constraint. These remain necessary conditions. No incompatible upper bound or embedded AG conjugate union with the required polarization follows from the graded theorem alone.

## 12. Embedded-curve exclusion of the minimal boundary

**Independently reviewed refinement.** Reuse the graded conductor theorem in §11. The argument below adds an embedding constraint; it does not change that theorem's hypotheses or establish an unrestricted STCI obstruction.

Let \(S=k[x_0,x_1,x_2,x_3]\), let \(Y=\operatorname{Proj}A\), where \(A=S/(F_a,G_b)\) is a proper complete-intersection curve of positive surface degrees \(a,b\), and suppose \(Y_{\mathrm{red}}=C\) is an irreducible curve which is not a line. Suppose \(A\subset B\) satisfies all hypotheses of the graded conductor theorem, with \(B=A+Aw\) as an **A-module** and \(\deg w=d>0\). Set \(T=A/\mathfrak c\), \(\Delta=\operatorname{Proj}T\), and \(\delta=\deg\Delta\). If

\[
\min(a,b)>d+2,
\]

then

\[
\boxed{\delta\ge a+b-d-1.}
\]

**Proof.** Put \(e=a+b-4\) and \(\delta_0=e-d+2=a+b-d-2\). The reused theorem gives \(\delta\ge\delta_0\) and an h-vector \(h_0,\ldots,h_s\) with \(s\ge e-d+1=\delta_0-1\) and every \(h_i\ge1\). Suppose equality \(\delta=\delta_0\) holds. Since \(\delta=\sum h_i\), necessarily \(s=\delta_0-1\) and every \(h_i=1\). The displayed degree hypothesis ensures \(\delta_0>\max(a,b)\), so in particular \(s\ge1\) and

\[
\dim_kT_1=h_0+h_1=2.
\]

As a standard graded quotient of S, T therefore has two independent linear equations. They define a line \(L\subset\mathbf P^3\), and \(\Delta\subset L\) scheme-theoretically. The dimension-one CM property of T gives \(H^0_{S_+}(T)=0\), so its homogeneous ideal in S is saturated; its quotient ideal on L is saturated as well. A finite subscheme of \(L\simeq\mathbf P^1\) of degree \(\delta_0\) has homogeneous ideal generated by a single binary form of degree \(\delta_0\). This statement includes nonreduced subschemes.

Both F and G vanish on \(\Delta\), since T is a quotient of A. Their restrictions to L thus belong to that principal ideal. Their degrees a and b are strictly less than \(\delta_0\), so both restrictions are zero. Hence \(L\subset Y\). This contradicts \(Y_{\mathrm{red}}=C\), because an irreducible curve different from L cannot contain L. Equality is impossible, and integrality of \(\delta\) proves the bound. \(\square\)

For the separated quadratic lift of any hypothetical supported pair on the fixed quartic C0 in characteristic zero, d=1. The previously established low-degree exclusions give \(\min(a,b)\ge4\) (indeed the carrier theorem gives the stronger \(\min(a,b)\ge5\)). Therefore

\[
\boxed{\delta\ge a+b-2.}
\]

Here the extremal case would create an actual line in the complete intersection downstairs. It is neither a cone-vertex artifact nor merely vertical exceptional support. For the fixed quartic with the stronger premise min(a,b)≥5, the quadratic norm in §8.1 gives a larger scalar lower bound. This extremal proof retains its separate value for the stated degree-d extensions without a quadratic relation. Neither argument supplies an incompatible upper boundary bound.

**Review scope.** Independently reconstructed the extremal h-vector argument, the saturated line-supported scheme step, and the degree restriction contradiction. Nonreduced conductor support causes no exception: a binary form of smaller degree cannot vanish on a divisor of larger scheme length unless it is zero. No computation or literature rerun is required for this refinement. The algebraic implication is characteristic free under the stated extension and degree hypotheses; the specified separated quadratic-lift application retains its characteristic-not-two restriction.

## 13. Canonical conductor, section completion and embedded action

**Independently reviewed deductions.** Keep the actual graded
rings of the hypothetical supported pair in §§6–8, in the stated
characteristic-zero setting. This argument identifies additional structure
on the same embedded branch; it does not produce a new ACM embedding.
Write \(\mathfrak c=\operatorname{Hom}_A(B,A)\) and \(T=A/\mathfrak c\).
The exact sequence
\[
0\longrightarrow\mathfrak c\longrightarrow A\longrightarrow T
\longrightarrow0
\]
has depths two and one in its last two terms. The depth lemma therefore
gives \(\operatorname{depth}_A\mathfrak c=2\). Thus the conductor is MCM
over the two-dimensional ring A. As a module over the four-dimensional
covering ring \(E=S[z]/(z^2-r)\), however, it still has dimension and
depth two and is not MCM. The boundary theorem already implies this depth;
it is not a second restriction on the pair.

Finite duality gives \(\mathfrak c(e)=\omega_B\). Consequently the
canonical-endomorphism construction gives
\[
B^\sharp=\operatorname{End}_B(\mathfrak c)
        =\operatorname{End}_A(\mathfrak c).                    \tag{13}
\]
For the second equality, localize in the common full total quotient
algebra: the conductor has rank one there, so each A-endomorphism is
multiplication by an element of that commutative algebra and commutes
with B. The primary branch is unmixed. The canonical-endomorphism theorem
identifies this finite extension with its \(S_2\)-ification; see
[Hochster–Huneke, §2.2(f,h) and Proposition 2.7](https://arxiv.org/pdf/math/0211172).
Since B is CM away from its cone vertex, the graded section sequence then
gives
\[
B^\sharp=\bigoplus_{n\in\mathbf Z}H^0(W,\mathcal O_W(n)),\qquad
B^\sharp/B=H^1_{\mathfrak m}(B)=M_W.                           \tag{14}
\]
Thus this operation fills the section ring of the same projective scheme
W. It does not change the original ambient restriction maps or turn their
coordinate image B into an ACM quotient. The full graded ring can include
negative-degree nilpotent sections and is not automatically a standard
graded quotient in the same coordinates.

Multiplication by the omitted coordinate is an actual graded action
\[
\mu:\mathfrak c\longrightarrow\mathfrak c(1),\qquad \mu^2=r.
\]
It also acts on \(M_W\). Indeed \(B^\sharp\mathfrak c\subset\mathfrak c\),
so \(\mathfrak c M_W=0\), and the quotient in (14) is a module over
\(T[z]/(z^2-r)\). This does not give a compatible z-action on the two
terms of the canonical injection \(T(e-1)\hookrightarrow\omega_T\):
multiplication by z sends the even copy of T in the quadratic conductor
boundary into the odd summand. That injection alone does not retain such
an action on its separate terms.

The complete action does retain the embedded equation maps. Put
\(R=A[z]/(z^2-r)\). Then
\[
\ker(R\longrightarrow B)
   =\{zh-\mu(h):h\in\mathfrak c\}.                           \tag{15}
\]
Every element of R has the unique form \(p+zq\). It vanishes in B
exactly when \(qz\in A\), equivalently \(q\in\mathfrak c\), and
\(p=-\mu(q)\). Conversely those graph elements vanish. Their stability
under multiplication by z follows from
\[
z(zh-\mu(h))=-\bigl(z\mu(h)-\mu^2(h)\bigr).
\]
This proves (15) as the actual ideal presentation, rather than only a
module count. It records which conductor multiples of the omitted
coordinate descend and the sections to which they descend. Specifying
the allowable embedded conductor and its full action reconstructs the
branch ideal; without a further comparison, that specification is still
an equation-realization problem. Module ranks or twists alone forget
the required maps.

There is a useful presentation distinction on the covering quadric. The
second E-syzygy of \(\mathfrak c\) is MCM: two free syzygy steps raise its
depth from two to four. Its maps back to \(\mathfrak c\), the inclusion
\(\mathfrak c\subset A\), and \(\mu\) are still needed. This does not
make the ordinary E-type module of an arbitrary W MCM. That conclusion
requires the actual curve to be ACM in
[Drozd, Lemma 2 and Theorem 2](https://arxiv.org/pdf/math/0409243).
For non-ACM curves, the presentation in
[Hartshorne–Migliore–Nagel, §5](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
retains a compatible surjection as well as Rao and MCM modules. These
maps can hold information beyond the scalar postulation bounds, but no
checked theorem here makes their required conjugate compatibility
impossible or supplies the desired branch.

## 14. Boundary geometry and the remaining realization problem

The explicit projections above produce genuine supported multiple
structures, with precise local and global section-ring behavior. Their
failures identify features a different embedded construction would have
to change. They are not an exhaustive classification of possible sources.
For an arbitrary supported pair, the separated lift has a full quadratic
conductor boundary, not just two reduced attachment points. Canonical
duality constrains its grading; the ambient norm forces independent
low-degree conditions and complementary later postulation. Neither
length is a count of distinct points or a residual curve downstairs.

These necessary conditions can test a proposed realization. In the fixed
characteristic-zero application, (7c) strengthens the lower boundary
requirement, while §12 retains an independent embedding argument in its
broader setting. No incompatible upper bound on the same full conductor
scheme is available. The canonical endomorphism ring completes sections
of an existing W; it does not construct the missing homogeneous maps or
repair their image in the fixed projective space.

There is also a concrete constructive target: §10 proves that an actual
embedded AG conjugate union with the prescribed support descends to a
complete intersection downstairs. The available local Gorenstein
attachments and abstract canonical modules do not yet supply that union
with its polarization and section ring. An explicit embedded operation
or a defined comparison on the actual conductor action can therefore
pose a meaningful further test, even before its outcome is known. The
results here describe what such a realization must retain, without
presuming either existence or nonexistence of a supported pair.

## Independent review and scope

The degree-\(d\) theorem uses finite birationality, module generation, Cohen–Macaulay and support hypotheses, including the nonreduced setting, exact shifts and Hilbert inequalities. It does not give an incompatible upper boundary bound, an arithmetically Gorenstein conjugate union, or an unrestricted STCI conclusion.

The separately reviewed norm/postulation theorem is retained with its full actual-ring proof, including nilpotent h, nonsquare polynomial norm, parity cutoff, and characteristic boundaries. The conductor-endomorphism application retains its scoped source review: it identifies section completion and the actual quadratic graph presentation, without an embedded ACM repair or a new exclusion. These additions do not re-certify unrelated source material.

The inherited mathematical inputs retain the scope and review evidence of their linked owners. No inherited CAS campaign was broadly rerun, and the unrestricted characteristic-zero STCI question remains open.


### Archived exact certificate: `research/computations/verify_session_quadratic_conductor_power_descent_2026_10_09.py`

Original source preserved verbatim, including its limitations and external dependencies. This is an archival transfer, not a new proof audit.

<details><summary>Historical source</summary>

```python
#!/usr/bin/env python3
"""Exact finite checks accompanying the conic power-descent proof.

These checks do not prove the generic-Artin classification or classify
actual surface carriers. They check the universal odd coefficient,
cyclotomic specialization, and two nilpotent counterexamples to weaker
coefficient conditions over characteristic zero.
"""

import json
import sympy as sp

m, ell, delta, b, zeta, eps = sp.symbols("m ell delta b zeta eps")


def pair_mul(left, right, square):
    a, u = left
    c, v = right
    return (sp.expand(a*c + u*v*square), sp.expand(a*v + u*c))


def pair_pow(pair, n, square):
    answer = (sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        answer = pair_mul(answer, pair, square)
    return answer


def reduce_eps(expr):
    return sp.rem(sp.Poly(sp.expand(expr), eps), sp.Poly(eps**2, eps)).as_expr()


def nilpotent_pair_pow(pair, n, square):
    answer = (sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        answer = tuple(reduce_eps(x) for x in pair_mul(answer, pair, square))
    return answer


odd_checks = []
cyclotomic_checks = []
nilpotent_checks = []
for n in range(1, 25):
    actual_odd = pair_pow((m, ell), n, delta)[1]
    formula = ell * sum(
        sp.binomial(n, 2*j+1) * m**(n-2*j-1) * (delta*ell**2)**j
        for j in range((n-1)//2+1)
    )
    assert sp.expand(actual_odd-formula) == 0
    odd_checks.append(n)

    if n >= 3:
        # lambda=(1+zeta)/(1-zeta) has
        # (lambda-1)/(lambda+1)=zeta. Its two power values coincide.
        lam = (1+zeta)/(1-zeta)
        numerator = sp.together((lam+1)**n-(lam-1)**n).as_numer_denom()[0]
        cyclotomic = sp.cyclotomic_poly(n, zeta)
        assert sp.rem(sp.Poly(numerator, zeta), sp.Poly(cyclotomic, zeta)).is_zero
        cyclotomic_checks.append(n)

    # m=epsilon, ell=1, delta=1: m²=0, but anti correction survives
    # every even power. Thus rho=0 proportionality is not sufficient.
    first_odd = nilpotent_pair_pow((eps, 1), n, 1)[1]
    assert first_odd == (n*eps if n % 2 == 0 else 1)
    # m=1, ell=epsilon, delta=epsilon: reduced ell=0 does not suffice.
    second_odd = nilpotent_pair_pow((1, eps), n, eps)[1]
    assert second_odd == n*eps
    nilpotent_checks.append(n)

# Exact factor checks at the first three nontrivial constants.
d = sp.symbols("d")
s3 = 3*m**2+d
s4 = 4*m*(m**2+d)
s6 = 6*m**5+20*m**3*d+6*m*d**2
assert sp.expand(s6 - 2*m*(3*m**2+d)*(m**2+3*d)) == 0
assert sp.rem(sp.Poly(s3, m), sp.Poly(m**2+d/3, m)).is_zero
assert sp.rem(sp.Poly(s4, m), sp.Poly(m**2+d, m)).is_zero

print(json.dumps({
    "status": "PASS",
    "sympy_version": sp.__version__,
    "universal_odd_coefficients_checked": odd_checks,
    "cyclotomic_power_specializations_checked": cyclotomic_checks,
    "nilpotent_counterexample_powers_checked": nilpotent_checks,
    "smooth_or_double_conic_degree_four_section_dimension": 9,
    "smooth_or_double_conic_required_rank_minors": 36,
    "separate_reduced_line_degree_four_section_dimension": 5,
    "separate_reduced_line_required_rank_minors": 10,
    "scope": "Finite exact identity checks; generic-Artin proof and actual surface geometry are separate."
}, indent=2))
```
</details>
