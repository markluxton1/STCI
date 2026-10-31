# Quadratic covers, projected thickenings and conductor descent

**Scope and status.** Independently reviewed provisional mathematics; no canonical promotion. Fix the smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), over an algebraically closed field. Characteristic zero is the default; every positive-characteristic statement below identifies its extra hypotheses. The conductor controls a finite map on the entire nonreduced schemes. The central distinction is between the explicit projected CI family and the primary lift of an arbitrary hypothetical supported pair: the latter need not be Gorenstein. No family calculation covers every pair. Characteristic-zero STCI remains open.

## 1. What the natural birational transport can and cannot do

Write B=Bl_C(P3), with H the pullback of a plane and E exceptional.
The second contraction identifies B with the blowup of a conic in V5;
its hyperplane class is L=3H−E. This precise quartic is covered by
[Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).
The [blowup residual account](blowup_residual_geometry.md) retains the equation dictionary.

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
cubic exclusion recorded in [R-0001](../results/quartic_carrier_exclusion.md).
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
[positive-characteristic construction record, §3](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md).
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

The remaining unrestricted gaps are concrete: no upper bound incompatible with (11) or (12) is established for the endpoint boundary, and no embedded AG conjugate union with the required polarization has been constructed. Local Gorenstein attachment, an abstract canonical extension, or success of the rank and determinant conditions alone does not fill those gaps. The characteristic-zero STCI question remains open.

## Independent review and scope

Independent reconstruction checked the projected-source and arbitrary-pair distinction, full primary extraction, conductor and attachment formulas, characteristic bounds, and conjugate descent. The degree-d theorem was proved again with full finite-birational, module-generation, CM and support hypotheses, including the nonreduced setting, exact shifts and Hilbert inequalities. No incompatible upper boundary bound, AG conjugate union, or unrestricted STCI conclusion follows.

The inherited mathematical inputs retain the scope and review evidence of their linked owners. No inherited CAS campaign was broadly rerun, and the unrestricted characteristic-zero STCI question remains open.
