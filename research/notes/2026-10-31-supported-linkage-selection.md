# Supported linkage operations and the limit of numerical liaison comparisons

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
the [companion audit](2026-10-31-supported-linkage-selection-audit.md)
records exact coverage. Work over an algebraically closed field of
characteristic zero with the fixed quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\).
The unrestricted STCI question remains open.

This is the bounded selection following the
[quadratic-boundary theorem](2026-10-31-quadratic-cover-boundary.md).
It compares a prospective second global constraint with an actual
embedded operation. A short uniform viability check closes the latter;
no degree search, finite-chain classification, or larger experiment
is selected. No claim of literature novelty is made.

## 1. The Rao dimensions are already the boundary inequality

For a hypothetical supported CI \(Y=V(F_\alpha,G_\beta)\), retain
the quadratic cover \(E=S[z]/(z^2-2bc+ad)\), the full D-primary
branch W, and the graded rings and boundary from the preceding note:
\[
0\to A\to B\to T(-1)\to0,\quad
e=\alpha+\beta-4,\quad H_\Delta(n)=\dim_k T_n,\quad\ell\Delta=\delta.
\]
No ACM or Gorenstein hypothesis on B is added. The canonical sequence
of that note, together with graded local duality, is
\[
0\to T(e-1)\to\omega_T\to M_W^\vee(-1)\to0,
\quad M_W=H^1_*(Q_3,\mathcal I_{W/Q_3})=H^1_{\mathfrak m}(B).
\]
Taking its degree \(1-n\) part gives
\[
\boxed{\dim_k M_W(n)=
\delta-H_\Delta(n-1)-H_\Delta(e-n).}                                  \tag{1}
\]
Here \(M^\vee_j=\operatorname{Hom}_k(M_{-j},k)\).
The numerical linkage symmetry under
\(n\leftrightarrow\alpha+\beta-3-n\) is automatic, and
nonnegativity is precisely the previous restriction-function inequality.
It is not an independent second budget.

Geometrically, the failure of ambient forms to supply all sections
on W is the remaining part of the two complementary endpoint
restriction spaces. Formula (1) concerns dimensions; it does not
determine all multiplication maps or the full embedded presentation.
[Hartshorne–Migliore–Nagel, §5](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
retain additional MCM-module and presentation data for CI liaison on
Q3. The Rao module alone does not supply the required direct conjugate
link. This literature identifies real additional data, without giving
a support-specific incompatible bound on it.

There is also no genus lower bound from support and multiplicity alone.
Write \(N^*_{D/Q_3}=\mathcal O(u_0)\oplus\mathcal O(v_0)\) on P1.
For every \(l>\max(u_0,v_0)\), the sections
\(s^{l-u_0},t^{l-v_0}\) give a surjection onto \(\mathcal O(l)\).
The kernel of \(I_D\to N^*_{D/Q_3}\to\mathcal O(l)\) defines a
Ferrand ribbon with
\[
0\to\mathcal O_{\mathbf P^1}(l)\to\mathcal O_{W_l}
\to\mathcal O_D\to0,\qquad p_a(W_l)=-l-1.
\]
This is the standard embedded kernel construction recalled in
[Notari–Ojeda–Spreafico, §2](https://arxiv.org/pdf/0812.2578).
For large l these ribbons are not ACM: their global functions have
dimension greater than one. They are not claimed to have AG conjugate
unions and do not disprove an estimate using that actual union or an
ACM hypothesis. They rule out only a lower genus budget based on
fixed support, fixed multiplicity and the smooth ambient quadric.

[Jaffe, Theorem 10.3](https://arxiv.org/pdf/alg-geom/9410008)
gives genuine higher-blowup inequalities under generic smoothness of
both defining surfaces along C. Its stronger global conclusions add
further singularity hypotheses. Those assumptions do not cover the
arbitrary normal orders and common singularities retained here.
No new unrestricted upper bound on conductor or surviving contact
was obtained from the checked sources.

## 2. An actual support-preserving basic double link

Put
\[
h=z^2-2bc+ad,\quad E=k[a,b,c,d,z]/(h),\quad
f=b^2-az,\quad g=c^2-dz,\quad P=I_D\subset E.
\]
The [preceding direct construction](2026-10-31-ambient-transport-and-projection.md#3-a-selected-operation-that-automatically-retains-the-reduced-support)
proves that f,g form a regular sequence in E with reduced zero locus
D and cycle 2D. For all positive u,v, form
\[
I_{u,v}=(f^u)+g^vP.                                                   \tag{2}
\]
This is basic double linkage: a containing section is retained and
the ideal of the starting curve is multiplied by a second section.
Compare the standard definition in
[Migliore–Nagel, Definition 2.1](https://www3.nd.edu/~jmiglior/MN7.pdf).
The needed facts here follow directly in E, without extending that
paper's ambient hypotheses:
\[
0\to(E/P)(-2v)\xrightarrow{\cdot g^v}E/I_{u,v}
\to E/(f^u,g^v)\to0.                                                \tag{3}
\]
Indeed \((f^u):g^v=(f^u)\subset P\), proving the kernel assertion.
Both end terms are CM of dimension two, so the middle term is CM,
and its ideal is saturated and unmixed. Its radical is P, and
\[
[W_{u,v}]=(1+2uv)[D],\qquad\deg W_{u,v}=4+8uv.
\]
The original grading preserves the fixed hyperplane polarization.
Thus (2) is an actual ACM supported construction beyond the previous
complete-intersection power source, not an abstract existence request.

## 3. The entire operation fails its generic or low-degree condition

For u≥2 the generic transverse algebra is not Gorenstein.
On a=1 eliminate \(d=2bc-z^2\) and put \(y=c-bz\). Directly,
\[
g=y^2-z^2 f.
\]
At the generic point of D, z is a unit. In the completed regular
local ring \(R=k(D)[[x,y]]\), take \(x=g\). Then
\[
f=-z^{-2}x+z^{-2}y^2,\qquad
I_{u,v}R=(f^u,x^{v+1},x^v y).                                       \tag{4}
\]
All three generators in (4) are minimal. The first is not divisible
by x. Modulo \(f^u\), x is regular, so redundancy of either other
generator allows cancellation of \(x^v\). It would respectively
imply \(x\in(y,f^u)\) or \(y\in(x,f^u)\). But
\[
R/(y,f^u)\simeq k(D)[[x]]/(x^u),\qquad
R/(x,f^u)\simeq k(D)[[y]]/(y^{2u}),
\]
retain x when u≥2, respectively y. A height-two Artinian Gorenstein
quotient of a regular local ring of dimension two is a CI; this
three-generator ideal is therefore not Gorenstein.

The conjugate branch is absent at this generic point, so adding it
leaves the local algebra unchanged. Thus \(W_{u,v}\cup\sigma W_{u,v}\)
is not AG for u≥2. The distinction from the preceding boundary note
is essential: non-Gorenstein **endpoint** branches can be repaired by
attachment, but a generic defect cannot be repaired at two endpoints.

For u=1, the image ideal contains the nonzero quartic
\[
N(f)=f\sigma(f)=b^4-a^2(2bc-ad).
\]
A CI image would have a minimal defining degree at most four. This
contradicts the accepted factor-reduction consequence of
[STCI-R-0001](../results/quartic_carrier_exclusion.md).
Consequently every positive-(u,v) source in (2) fails to give a CI
image or an AG conjugate union. Swapping f and g gives the same result.
The global ACM property of the source has not solved the generic
canonical compatibility problem.

## 4. Extracted generalization: any quadratic multiplier retains a forbidden sextic

There is a broader obstruction that avoids proposing nearby variants
of (2). First, a scheme with reduced support C whose homogeneous
ideal contains a nonzero sextic all of whose irreducible factors have
degree at most four cannot be a complete intersection.

For proof, suppose its CI degrees are \(5\le\alpha\le\beta\), using
STCI-R-0001 and its factor reduction. Bézout gives \(4\mid\alpha\beta\).
If \(\alpha\ge7\), its ideal has no sextic. If \(\alpha=5\),
divisibility forces \(\beta\ge8\); every sextic is then a linear
multiple of the degree-five generator, which would have a forbidden
factor of degree at most four. If \(\alpha=6<\beta\), the sextic
is a scalar multiple of that generator, again impossible. If both
degrees are six, a constant invertible change of the two generators
makes the sextic one defining equation, with the same contradiction.
These possibilities exhaust the proof; no degree search is involved.

Now let \(I\subset E\) be homogeneous, with reduced scheme image C,
and suppose
\[
GP\subset I\quad\text{for some nonzero }G\in E_2.
\]
The invariant quadric \(q=bc-ad\) belongs to \(P\cap S\). Hence
\[
qN(G)=qG\sigma(G)\in I\cap S.                                      \tag{5}
\]
Since E is a domain, (5) is nonzero. It is a sextic whose factors
all have degree at most four: q has degree two and N(G) degree four.
The preceding argument excludes a CI scheme image. It also applies
to its saturated ideal. No ACM, Gorenstein or purity hypothesis is
needed for this implication once the reduced image is C.

In particular **every** supported basic double link \((F)+GP\) with
quadratic multiplier G fails, irrespective of the degree or choice
of the containing section F. This conclusion does not cover higher
degree multipliers, nor does it apply the quadratic-multiplier lemma
to \(g^v\) when v>1. The generic proof in §3 handles that power family.
Geometrically, multiplication of the branch ideal by a quadric retains
an actual low-degree reducible equation after projection. Its
components are individually excluded as defining carriers.

## 5. Selection and stopping decision

The two selection checks add a useful dependency and a uniform
operation boundary. Numerical Rao nonnegativity and symmetry are
already the conductor condition; they supply no second obstruction.
Basic double linkage genuinely constructs supported ACM schemes,
but the displayed operation cannot make the conjugate union AG.
Its quadratic-multiplier generalization closes nearby changes of the
containing section at once.

No finite BDL-chain, endpoint-type, multiplicity or higher-multiplier
classification follows. A future constructive proposal must supply
actual sections and a mechanism that retains a generic CI transverse
algebra, escapes the descended low-degree factor obstruction, and
permits testing the conjugate attachment and global section ring.
These are conditions on a proposed operation, not a demand that its
success be proved before investigation. For an obstruction proposal,
substitute (1) before treating a liaison dimension as an independent
bound; stop if the proposed comparison reduces to the existing
canonical inequality or an attachment identity.

No new technical experiment is selected from this check. The result
does not exclude arbitrary supported W, arbitrary STCI pairs, higher
degree multipliers, or explicitly specified different finite chains.
The possibility that C is STCI remains live.
