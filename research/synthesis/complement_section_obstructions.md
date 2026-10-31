# Sections on space-curve complements and their primary obstructions

Let \(C\subset\mathbf P^3_k\) be a smooth connected curve of degree
\(d>0\) and genus \(g\), and put \(U=\mathbf P^3_k\setminus C\).
The statements below concern arbitrary such curves. The topological
and holomorphic assertions require \(k=\mathbf C\); Chow–Witt assertions
require algebraically closed \(k\) of characteristic different from two.
The remaining algebraic assertions hold over any algebraically closed
field. These are provisional mathematical deductions, with the precise
claims and proofs recorded here; no canonical STCI promotion follows.

For the fixed characteristic-zero quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), the unrestricted STCI question remains open.
The exact complement-pencil equivalence and its graph construction belong
to [global equations](global_equations_and_constructions.md#complement-pencils-and-positive-line-bundles).
This chapter determines what the classical section test and the ordinary
and primary quadratic characteristic classes can decide.

## 1. Complete continuous-section criterion

**Theorem.** For every topological complex vector bundle \(V\) of rank two
on \(U(\mathbf C)\),
\[
 V\text{ has a continuous nowhere-zero section}
 \quad\Longleftrightarrow\quad c_2(V)=0\in H^4(U,\mathbf Z).
 \tag{1}
\]
In particular,
\[
 \mathcal O_U(a)\oplus\mathcal O_U(b)
 \text{ has such a section}\quad\Longleftrightarrow\quad d\mid ab.
 \tag{2}
\]
Here \(a,b\) may be arbitrary integers; positivity is needed later for
the homogeneous-equation interpretation.

**Proof.** The complex normal bundle of \(C\) has oriented real rank four.
Thom isomorphism gives the integral Gysin sequence
\[
 \cdots\to H^{i-4}(C,\mathbf Z)\to H^i(\mathbf P^3,\mathbf Z)
 \to H^i(U,\mathbf Z)\to H^{i-3}(C,\mathbf Z)\to\cdots.
\]
The map \(H^0(C)\to H^4(\mathbf P^3)\) multiplies by \(d\), whereas
\(H^2(C)\to H^6(\mathbf P^3)\) is an isomorphism: a point maps to a
point, independently of \(d\). Hence
\[
 H^0(U,\mathbf Z)=\mathbf Z,\qquad H^2(U,\mathbf Z)=\mathbf Z h,
\]
\[
 0\to\mathbf Z/d\xrightarrow{1\mapsto h^2}H^4(U,\mathbf Z)
 \to\mathbf Z^{2g}\to0,
 \tag{3}
\]
and all other positive-degree integral cohomology vanishes. The last
sequence splits as abelian groups, without a preferred splitting.

General position gives \(\pi_1(U)=0\): a disk spanning a loop in
\(\mathbf P^3\) can be perturbed away from the real codimension-four
submanifold \(C\). Removing an open tubular neighborhood of \(C\) gives
a compact six-manifold with boundary homotopy equivalent to \(U\).
Thus \(U\) has finite CW type of dimension at most six.

The unit sphere bundle of \(V\) has fiber \(S^3\). Its first section
obstruction is the Euler class \(c_2(V)\). Once it vanishes, the only
remaining possible obstructions lie in
\[
 H^5(U,\pi_4(S^3))=H^5(U,\mathbf Z/2),\qquad
 H^6(U,\pi_5(S^3))=H^6(U,\mathbf Z/2).
\]
Local coefficients are trivial. Both groups vanish by the coefficient
Bockstein sequence and the integral vanishings in degrees five, six and
seven. There are no higher-dimensional cells. This proves sufficiency;
necessity follows from the Euler class. Finally,
\(c_2(\mathcal O(a)\oplus\mathcal O(b))=ab h^2\), whose vanishing is
exactly \(d\mid ab\) by (3). This proves (1)–(2).

The standard sphere-bundle obstruction framework and Euler-class
identification are in [Hatcher, *Vector Bundles and K-Theory*, §3.3,
Proposition 3.22](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf);
the two sphere homotopy groups occur in [*Algebraic Topology*, Chapter 4,
p. 339](https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf).
The vanishing of the higher obstruction groups is part of the proof
above, rather than an inference from rational cohomology.

## 2. Algebraic and holomorphic realization and necessary nonsplitting

Fix \(a,b>0\). Every algebraic section of
\(\mathcal O_U(a)\oplus\mathcal O_U(b)\) extends uniquely to
\(\mathbf P^3\), by extension of sections of locally free sheaves across
a codimension-two subset of a normal variety. Over \(\mathbf C\),
analytic Hartogs extension in local trivializations gives the identical
conclusion for holomorphic sections. Global holomorphic sections on
\(\mathbf P^3\) are the homogeneous polynomials of the indicated degrees.

Thus an algebraic or holomorphic nowhere-zero section on \(U\) is exactly
a degree-\((a,b)\) homogeneous pair with common-zero support \(C\).
Indeed, no surface component of its common zero set can lie in \(C\).
The two positive-degree hypersurfaces have nonempty proper intersection,
pure of dimension one, and its support is a one-dimensional closed subset
of the irreducible \(C\), hence all of \(C\). Conversely a supported pair
is nowhere zero on \(U\). Smooth connectedness implies irreducibility here.

For an actual supported pair \(F,G\), there is an exact sequence
\[
 0\to\mathcal O_U\xrightarrow{(F,G)}
 \mathcal O_U(a)\oplus\mathcal O_U(b)
 \xrightarrow{(-G,F)}\mathcal O_U(a+b)\to0.
 \tag{4}
\]
It is necessarily nonsplit algebraically and, over \(\mathbf C\),
holomorphically. A retraction would belong to
\[
 H^0(U,\mathcal O_U(-a))\oplus H^0(U,\mathcal O_U(-b))=0,
\]
again by Hartogs extension and positivity. In contrast, a continuous
Hermitian metric splits (4) continuously.

The affine cover \(D_+(F)\cup D_+(G)=U\) has local right inverses
\((0,1/F)\) and \((-1/G,0)\) for the final map in (4). Their difference
is \((F,G)/(FG)\), so up to sign the extension class is
\[
 \xi_{F,G}=[1/(FG)]\in H^1(U,\mathcal O_U(-a-b)),\qquad \xi_{F,G}\ne0.
 \tag{5}
\]
Nonvanishing is required by successful equations. A trivial line
subbundle with locally free quotient need not be an algebraic direct
summand on this nonaffine base. An arbitrary extension class constructs
a middle bundle, but identifying that bundle with the prescribed
\(\mathcal O_U(a)\oplus\mathcal O_U(b)\) remains substantive.

## 3. Chow and virtual-bundle conditions

Chow localization gives
\[
 CH^2(U)=\mathbf Z h^2/(d h^2),\qquad CH^3(U)=0.
 \tag{6}
\]
The fundamental class of \(C\) maps to \(d h^2\), and a point of \(C\)
maps to the point generator \(h^3\). These calculations use no supported
pair.

The integral algebraic K-theory calculation is already proved, in the
more general integral-curve setting, in
[the ordinary K-theory account](global_equations_and_constructions.md#ordinary-k-theory-and-its-precise-limitation).
With \(t=1-[\mathcal O(-1)]\), its conclusion is
\[
 K_0(U)=\mathbf Z[t]/(t^3,d t^2).
 \tag{7}
\]
The pushforward image is generated by \(dt^2,t^3\); neither genus nor
degree-zero Picard classes add a contribution. We use that existing
calculation here to compare the necessary virtual middle-bundle class.

Sequence (4), if it exists, forces
\[
 [\mathcal O_U(a)]+[\mathcal O_U(b)]-[\mathcal O_U]
 -[\mathcal O_U(a+b)]=-ab t^2=0.
 \tag{8}
\]
Expand \([\mathcal O(n)]=(1-t)^{-n}\) modulo \(t^3\) to obtain the
equality. Thus this virtual condition is exactly \(d\mid ab\).
A K-class equality supplies neither a middle-bundle isomorphism nor
maps realizing (4).

## 4. Twisted Chow–Witt groups add no primary information

Assume now that \(k\) is algebraically closed and \(\operatorname{char}k\ne2\).
For every line bundle \(L\) on \(U\), the forgetful map is an isomorphism
\[
 \widetilde{CH}^{\,2}(U,L)\xrightarrow{\sim} CH^2(U)=\mathbf Z/d.
 \tag{9}
\]
For any rank-two algebraic bundle \(V\), its characteristic Euler class
with twist \(\det V^\vee\) therefore vanishes exactly when \(c_2(V)\)
vanishes. For the split bundle of (2), this is again \(d\mid ab\).
This is a statement about characteristic classes, without asserting
section existence on \(U\).

**Proof.** Write \(\mathbf I^j(L)\) for the twisted unramified sheaves
of fundamental-ideal powers. The field has 2-cohomological dimension
zero, and the smooth base has dimension three. Thus
\[
 \mathbf I^4(L)=0,\qquad
 \mathbf I^3(L)\simeq\mathbf K^M_3/2
 \simeq\mathcal H^3_{\mathrm{et}}(\mu_2^{\otimes3}).
 \tag{10}
\]
The first assertion is [Asok–Fasel, Proposition 5.1](https://arxiv.org/pdf/1204.0770).
The other identifications use the fundamental-ideal quotient and
norm-residue comparison; twisting is trivial modulo the next ideal
power, so no square root or orientation of \(L\) is needed.

The Bloch–Ogus spectral sequence
\[
 E_2^{p,q}=H^p_{\mathrm{Nis}}
 (U,\mathcal H^q_{\mathrm{et}}(\mu_2^{\otimes3}))
 \Longrightarrow H^{p+q}_{\mathrm{et}}(U,\mu_2^{\otimes3})
\]
has no rows \(q>3\), by cohomological dimension, and no columns \(p>3\).
Its terms \((2,3),(3,3)\) have no incoming or outgoing differentials
from \(E_2\) onward. The upper edge gives
\[
 H^6_{\mathrm{et}}(U,\mu_2^{\otimes3})
 \simeq H^3_{\mathrm{Nis}}(U,\mathbf I^3(L)),
\]
\[
 H^5_{\mathrm{et}}(U,\mu_2^{\otimes3})
 \twoheadrightarrow H^2_{\mathrm{Nis}}(U,\mathbf I^3(L)).
 \tag{11}
\]
These are the same upper-edge arguments as in the proof of
[Asok–Fasel, Proposition 5.2](https://arxiv.org/pdf/1204.0770);
its final affine vanishing argument is replaced here by a direct
calculation on this nonaffine complement.

Purity and Gysin give
\[
 0\to H^5_{\mathrm{et}}(U,\mu_2^{\otimes3})
 \to H^2_{\mathrm{et}}(C,\mu_2)
 \xrightarrow{i_*}H^6_{\mathrm{et}}(\mathbf P^3,\mu_2^{\otimes3})
 \to H^6_{\mathrm{et}}(U,\mu_2^{\otimes3})\to0.
 \tag{12}
\]
The middle groups both have order two and the map is an isomorphism:
a point pushes to a point. This map multiplies by one, whereas the
distinct \(H^0(C)\to H^4(\mathbf P^3)\) map measures \(d\).
See [Milne, Theorems 16.1 and 24.1, Remark 24.2](https://www.jmilne.org/math/CourseNotes/LEC.pdf)
for the purity and trace conventions. Equations (10)–(12) yield
\[
 H^2_{\mathrm{Nis}}(U,\mathbf I^3(L))=
 H^3_{\mathrm{Nis}}(U,\mathbf I^3(L))=0.
\]
The exact sequence
\[
 0\to\mathbf I^3(L)\to\mathbf K^{MW}_2(L)
 \to\mathbf K^M_2\to0
\]
now proves (9). The characteristic Euler class forgets to \(c_2\) and
vanishes in the presence of a nowhere-zero section; these are
[Asok–Fasel, *Comparing Euler classes*, §§2–3 and Proposition 5.4.1](https://arxiv.org/pdf/1306.5250).
An affine splitting theorem or an oriented comparison theorem is
unnecessary for this deduction.

## 5. Precise limits of realization theorems

Algebraic and analytic Hartogs give \(H^0(U,\mathcal O_U)=k\), or
\(\mathbf C\) analytically. Thus \(U\) is nonaffine. Analytically it
is also not 1-convex: a proper Remmert reduction to a Stein space
would have constant functions, hence point image, forcing \(U\) compact.
The following source requirements prevent several standard theorems
from furnishing the missing sections automatically.

| Primary theorem | Applicable conclusion and boundary here |
| --- | --- |
| [Asok–Bachmann–Hopkins, Theorem 7.1.1](https://arxiv.org/html/2306.04631#S7.SS1) | Over an algebraically closed characteristic-zero field, a rank-\(r\) bundle on a smooth affine \((r+1)\)-fold splits off a trivial summand iff its top Chow Chern class vanishes. This \(U\) is nonaffine; its desired sequence (4) must be nonsplit. |
| [Asok–Hoyois–Wendt, Theorem 4.2.10](https://msp.org/gt/2018/22-2/gt-v22-n2-p11-s.pdf) | For an infinite field and the stated isotropic reductive group/parabolic hypotheses, naive \(\mathbf A^1\)-homotopy classes of maps from a smooth affine source agree with motivic classes. This does not produce an actual section over \(U\). |
| [Stopar, Corollary 8.2](https://arxiv.org/pdf/1305.4256) | A section Oka principle has a 1-convex base and further domain/submersion hypotheses. This base fails 1-convexity. |
| [Fornæss–Sibony–Wold, Theorems 1.6–1.8](https://arxiv.org/pdf/1105.5408) | Their convention counts positive Levi eigenvalues. The complement has an exhaustion with corners with two positive directions. Their line-bundle extension theorem needs three in dimension three, and extends line bundles from an end rather than constructing the desired section. |
| [Forstnerič, Proposition 1.2(a), Theorem 1.1](https://arxiv.org/pdf/math/0110201) | The complement is a subelliptic target for maps from Stein sources. This does not make \(U\) a Stein source for a theorem about sections over \(U\). |

A positive-rank Jouanolou affine-space torsor over \(U\) raises dimension
above three while retaining bundle rank two. The rank-\(r\), dimension-\(r+1\)
splitting theorem cannot simply be reapplied, and any separately produced
section needs strict descent to \(U\).

There is a direct control against an unrestricted realization assertion.
If \(C\) is nonplanar, the positive split bundle
\(\mathcal O_U(1)\oplus\mathcal O_U(d)\) passes (2), (8) and (9),
yet has no algebraic or holomorphic nowhere-zero section. Such a section
would extend to a supported pair with a linear equation, forcing \(C\)
into a plane. Its linear component cannot be identically zero: the other
positive-degree form has a hypersurface of zeros outside \(C\).
Thus these primary conditions are demonstrably insufficient.

## 6. Consequence and remaining mathematical interface

For \(C_0\), every degree pair satisfying \(4\mid ab\) passes the full
continuous-section test and the ordinary Chow, K-theory and twisted
characteristic Euler tests. These invariants give no further degree
restriction or positive residual-degree bound. Their calculations apply
uniformly in the degrees; no further classical section obstruction
remains for these bundles.

The live construction problem is an actual section, or a strict descent
mechanism yielding it with the prescribed middle bundle. The live
obstruction problem requires a specified invariant retaining algebraic
or carrier data beyond the classes computed above. The results do not
exhaust enriched motivic information, nor do they construct equations.
Higher motivic or actual-surface invariants are distinct uncomputed
interfaces, without an inferred obstruction value or section theorem.

## Independent review and scope

Independent reconstruction checked the complete continuous rank-two section criterion, the nonaffine twisted Chow-Witt comparison, characteristic Euler consequence, K-theory comparison, Hartogs realization and nonsplitting. The affine, analytic and motivic theorem boundaries were checked against the cited primary sources. These primary tests do not produce an algebraic or holomorphic section on the nonaffine complement.

The inherited mathematical inputs retain the scope and review evidence of their linked owners. No inherited CAS campaign was broadly rerun, and the unrestricted characteristic-zero STCI question remains open.
