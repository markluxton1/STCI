# Ambient transport and a scheme-changing projection source

Date: 2026-10-31. Status: **independently reviewed provisional results**;
see the [scoped audits](2026-10-31-ambient-transport-and-projection-audit.md).
The fixed curve is C=[s4:s3t:st3:t4] in P3 over an algebraically closed
field of characteristic zero. Unrestricted STCI remains open.
The [preceding assessment](2026-10-31-unrestricted-strategy-assessment.md#19-actual-matrix-columns-normal-action-defects-and-the-limit-of-operation-invariants)
closed the multiple-quadric bookkeeping round. This note records the
completed source selection and the particular projection test selected
after an independent challenge. It does not prescribe further families.

## 1. What the natural birational transport can and cannot do

Write B=Bl_C(P3), with H the pullback of a plane and E exceptional.
The second contraction identifies B with the blowup of a conic in V5;
its hyperplane class is L=3H−E. This precise quartic is covered by
[Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).
The [existing blowup note](2026-10-28-blowup-residual-geometry.md) and
[audit](2026-10-28-blowup-residual-audit.md) retain the equation dictionary.

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
ideal to be homogeneous. This verifies a historical question, not its
current resolution status; the focused search found no later solution.

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

## 3. A selected operation that automatically retains the reduced support

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

This is a structural interface for an explicit construction. It is not
the assertion that arbitrary ACM thickenings arise this way. The
independent strategy reviewer recommended a uniform test of (4), rather
than exponent enumeration. That recommendation and its stopping
conditions were reported before the test began: an ACM case would be
checked for Gorenstein type; a uniform failure would close this source;
case-dependent calculations without a general mechanism would stop the
test. There is no automatic expansion to an exponent on h.

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

## 5. Geometric extraction and stopping decision

The operation constructs actual thickenings with reduced support C
throughout. It introduces no residual curve. For every nontrivial
power, however, the conductor subscheme at a marked endpoint is not
Cartier on the Gorenstein source: its ideal retains two independent
generators. Finite duality then prevents the image from being
Gorenstein. This controls a specific passage in the user's compatibility
picture, from a genuine ambient AG source to its actual embedded image.

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
makes this precise endpoint non-Cartier obstruction disappear. This
does not establish that the image is locally Gorenstein, ACM, AG or
a CI; invertibility of the conductor was used as a necessary condition,
not a sufficient one. No new positive-characteristic experiment is
selected by this comparison.

The uniform ACM question for u,v other than (1,1) remains unresolved
here. It is unnecessary for closing this source as a direct construction
of an actual CI scheme. No sequence of further exponents, additional
equations or neighboring projection centers is selected. Nor does this
theorem rule out finding a different complete-intersection thickening
with the same radical, including a thicker scheme containing Y_uv.
A new proposal needs an operation that overcomes the identified
non-Cartier conductor while retaining the full embedded support.
The unrestricted characteristic-zero STCI question remains open.
