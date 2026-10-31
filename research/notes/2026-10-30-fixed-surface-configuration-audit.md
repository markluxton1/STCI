# Independent audit of the fixed-surface configuration

Date: 2026-10-30. Reviewer: `fixed_surfaces_audit` subagent.
Disposition: **the propositions and stated limitations in §§1–6 pass independent
hand review; reviewed provisional work, with no canonical promotion.** No
material correction is required for those sections.

## 1. State, scope, and review method

The reviewed source is
[What the two hyperosculating planes and the quadric retain](2026-10-30-fixed-surface-configuration.md),
§§1–6, lines 1–310 in the state read for this review. The SHA-256 of that
310-line file state, including its final newline, is
`3fb18c3a7878423d76ef09e3d7a472d19a9662854e830549c7a11ad0d41e551d`.
An appended trace investigation, or subsequent mathematical changes, is outside
this audit unless separately reviewed. The source's statement that independent
review is pending describes its pre-audit state.

The exact setting is an algebraically closed field of characteristic zero,
the fixed smooth quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad q=x_0x_3-x_1x_2,
\]
and the reduced degree-four divisor
\[
D=V(qx_0x_3)=Q\cup H^{(0)}\cup H^{(3)}.
\]
The three factors are distinct irreducible equations, so this product defines
the scheme-theoretic reduced union. The audit tests the complete restrictions
on this union, the explicit controls, every proper CI satisfying the stated
endpoint hypotheses, and the support criterion with its additional quadric
support hypothesis. It does not assume sole support when testing the controls.

I reconstructed the identities, local ideals, degrees, finite projection,
graded module argument, twisted characteristic polynomial, and generic Jordan
interpretation. I checked the relevant inherited endpoint and quadric
interfaces in the two linked source notes. `research/INDEX.md` and
`research/MAP.md` were used for scope and authority orientation only.
There was no computer algebra calculation, inherited certificate rerun,
numerical search, or new computational reduction.

## 2. The boundary configuration and cubic control

At \(p_\infty\), use \(t=1\), with parameter \(s\). The coordinate orders are
\((4,3,1,0)\). Hence the restrictions of the ideals
\((x_0,x_1)\) and \((x_0,x_2)\) to \(C\) have colengths three and one.
The equation \(x_0\) has order four. Reversing the coordinates gives the
corresponding assertion at \(p_0\). The gradient of \(q\) gives the tangent
planes \(x_0=0\) at \(p_\infty\) and \(x_3=0\) at \(p_0\).
These are intersections of actual fixed surfaces with the embedded curve;
the line lengths and hyperplane length have not been conflated.

Set \(c_0=x_1^3-x_0^2x_2\), \(c_2=x_2^3-x_1x_3^2\).
On \(x_0=1\), eliminating \(x_2\) gives the squarefree equation
\[
x_1(x_1^4-x_3)(x_1^4+x_3)=0.
\]
Its components close to \(L,C,C^-\), of degrees one, four, and four.
On \(x_0=0\), the only point of the intersection is \(p_\infty\).
The pair has no common surface factor. Therefore it is a pure
Cohen–Macaulay CI curve, every generic point is in the displayed reduced
affine chart, and there are no embedded associated primes. This proves the
global reduced scheme assertion, rather than only its set-theoretic version.
Its component degrees also sum to the Bézout degree nine.

On \(Q\), the Segre substitution gives directly
\[
c_0=A^2(AV^3-BU^3),\qquad
c_2=-B^2(AV^3-BU^3).
\]
Since \(A,B\) cannot both vanish on the first \(\mathbf P^1\), the
generated ideal sheaf is the ideal of \(C\). There is no extra punctual
scheme on \(Q\). On \(H^{(0)}\), the common support of
\(x_1^3\) and \(x_2^3-x_1x_3^2\) is exactly \(p_\infty\); the two plane
cubics have no common component, so the length is nine. The other plane
is symmetric.

The direct pullbacks
\[
q|_{C^-}=-2s^4t^4,\qquad q|_L=x_0x_3
\]
prove the endpoint-only intersection assertion for the two genuine
residual curves. The first has quadric intersection divisor
\(4p_0+4p_\infty\) on its normalization; the line has one intersection
at each endpoint. Thus the example really exhibits curves downstairs
which the reduced fixed-surface tests cannot distinguish from endpoint
attachments. It does not infer them from exceptional vertical components.
The numerical failure \(4\nmid9\) correctly prevents this first example
from being a candidate supported degree row.

## 3. Identical full restrictions and different transverse lengths

For every \(r\ge2\), the second equations of \(J_r,J'_r\) differ by
\[
qx_0^{3r-3}x_3=(qx_0x_3)x_0^{3r-4}.
\]
The exponent \(3r-4\) is nonnegative. The two ordered equation sections
are consequently identical modulo the ideal of the entire scheme \(D\).
This establishes equality with all component overlaps retained, without
an inference from separate reduced restrictions.

The quadric ideals are both \((h^r)\) as ideal sheaves, where
\(h=AV^3-BU^3\), so their intersection with \(Q\) is exactly the Cartier
divisor \(rC\). On each endpoint plane, the restricted equations are the
\(r\)-th powers of the same two cubics. They have the same sole common
point and no common component. The full plane CI schemes are identical,
with length \((3r)^2=9r^2\), including their nonreduced structure.

Properness is essential and also checks. Over
\(k[x_0,x_1,x_3]\), the two coefficients of the degree-one polynomial
\(c_0\) in \(x_2\) are coprime. Gauss's lemma and degree one over the
fraction field make \(c_0\) irreducible. It does not divide \(c_2\), for
example by evaluating on \([1:1:1:0]\). It does not divide
\(c_2^r+qx_0^{3r-3}x_3\), by evaluating on \([1:0:0:1]\).
These facts also exclude a common factor with \(c_0^r\). Both displayed
pairs are proper homogeneous CIs containing \(C\).

For an independent local reconstruction, work on \(x_0=1\), write
\(z=x_1\), and use \(K=k(z)=k(C)\) at the generic point of \(C\).
The transverse local ring is
\[
A=K[x_2,x_3]_{(x_2-z^3,x_3-z^4)}.
\]
With \(h=c_0=z^3-x_2\) and \(q=x_3-zx_2\), the change of parameters
has determinant a unit. Direct expansion verifies the source identity
\[
x_0^2c_2=-x_2^2c_0-(2x_1^2x_2+x_1q)q.
\]
It gives \(c_2=\alpha h+\beta q\), with both coefficients units in
\(A\); in particular \(\beta\bmod(h,q)=-2z^5\ne0\).
Thus \(h,c_2\) are regular parameters as well, and
\[
\operatorname{length} A/(h^r,c_2^r)=r^2.
\]
Modulo \(h^r\), expansion of \((\alpha h+\beta q)^r\) gives \(qv\)
with \(v\) in the maximal ideal: every remaining term has total
parameter order at least \(r\). The added term is \(uq\), with \(u\)
a unit. Hence
\[
(h^r,c_2^r+uq)=(h^r,q(v+u))=(h^r,q),
\qquad \operatorname{length} A/(h^r,q)=r.
\]
This equality is in the actual local ring, not merely an equality of
initial forms. It covers \(r=2\) and all larger integers.

Subtracting the \(C\)-cycle from the degree \(9r^2\) CI gives residual
degrees \(5r^2\) and \(9r^2-4r\), both positive. Even \(r\) meets the
divisibility condition, so the ambiguity is not explained away by that
condition. No equality of residual schemes, or existence of an STCI lift
of these same restrictions, follows or is claimed.

Geometrically, the correction lies in the ideal of the full boundary
but changes the action of a normal coordinate to \(Q\) at the generic
point of \(C\). The shared Cartier divisor \(rC\) measures the quotient
by that coordinate. It cannot determine the length before taking that
quotient. This is precisely the proved barrier to recovering thickness
from these fixed restrictions.

## 4. Every pair under the endpoint hypotheses: projection and splitting

The endpoint hypotheses imply \(Y\cap M=\varnothing\), since neither
endpoint lies on \(M=V(x_0,x_3)\). Thus the pencil defines a morphism on
the full scheme \(Y\), with \(\mathcal O_Y(1)=\pi^*\mathcal O(1)\).
A positive-dimensional fiber would contain a projective curve in one
plane of the pencil. Every such curve meets the line \(M\), a
contradiction. Properness and zero-dimensional fibers make \(\pi\)
finite. Since a CI curve is Cohen–Macaulay and pure, the pullback of any
local base uniformizer is a nonzerodivisor: no curve component is a
fiber. The finite module is torsion-free over each base DVR, hence free.
Every fiber is the plane hyperplane section and has length \(ab\).
This proves finite flatness and the degree with nonreduced fibers allowed.

For the splitting, put \(B=k[x_0,x_3]\) and
\(R=k[x_0,x_1,x_2,x_3]/(F_a,G_b)\). Empty projective intersection with
\(M\) means
\[
A_0=R/(x_0,x_3)
=k[x_1,x_2]/(\overline F_a,\overline G_b)
\]
is finite-dimensional. The two binary forms have no projective common
zero, so are a regular sequence. Moreover \(x_0,x_3\) is a homogeneous
system of parameters for the two-dimensional Cohen–Macaulay ring \(R\),
hence a regular sequence. Its Artinian Hilbert series is
\[
H_{A_0}(z)=(1+\cdots+z^{a-1})(1+\cdots+z^{b-1}).
\]
Lifting a homogeneous vector-space basis gives a surjection
\(\bigoplus_{i<a,j<b}B(-i-j)\twoheadrightarrow R\). It is surjective
by graded Nakayama, or by induction on degree. Regularity gives
\(H_R=H_{A_0}/(1-z)^2\), which equals the source Hilbert series.
The kernel has every graded dimension zero. Sheafifying this isomorphism
over \(\operatorname{Proj} B\) gives exactly the asserted splitting of
\(\pi_*\mathcal O_Y\).

This proof uses arbitrary coprime top binary forms. The indices \(i,j\)
record the **multiplicity of each basis degree**, not a claim that the
monomials \(x_1^ix_2^j\) themselves form a basis. For example the binary
CI \((x_1^2+x_2^2,x_1x_2)\) has the expected Hilbert series, but that
rectangular monomial set contains the zero class \(x_1x_2\). This tests
a tempting stronger claim; that stronger claim is not needed or made
in the source. The actual multiplication and coordinate operators
remain extra data. The vector-bundle splitting alone supplies no
algebra realization and no nilpotence obstruction.

## 5. Quadric operator, support criterion, spectrum, and Jordan blocks

Finite pushforward is exact. Applying it to the quotient by the ideal
generated by \(q\) gives
\[
E(-2)\xrightarrow{q}E\longrightarrow
\pi_*\mathcal O_{Y\cap Q}\longrightarrow0.
\]
No injectivity on the left is asserted; it would fail on the component
\(C\). The cokernel retains its induced quotient algebra structure.
As with the endpoint fibers, the ambient embedding also uses the
coordinate multiplication operators; an abstract module cokernel by
itself is not an embedded scheme.

For \(N:E\to E\otimes\mathcal O(2)\), the characteristic coefficients
are sections of \(\mathcal O(2j)\). This follows by changing the local
frame of the twisting line bundle and taking exterior powers. Twisted
powers and their traces have precisely the displayed degrees.

If \(Y_{\mathrm{red}}=C\), the section \(q\) lies locally in the
nilradical. Noetherian quasi-compactness supplies a uniform nilpotence
exponent. Conversely, nilpotence puts every reduced component and point
of \(Y\) in \(Q\). Under the additional hypothesis
\((Y\cap Q)_{\mathrm{red}}=C\), this is equivalent to sole support.
The extra hypothesis is used exactly here and has not been dropped.

Because the base is reduced and integral and \(E\) is locally free,
nilpotence generically forces all characteristic coefficients to vanish
identically. Conversely the local Cayley–Hamilton identity glues to
give \(N^n=0\) when all coefficients vanish. Newton identities over the
characteristic-zero field equate vanishing of the first \(n\) power
traces with those coefficient conditions. The criterion therefore holds
for every pair in its stated source, with no bound on \(a,b\).
The characteristic-zero trace qualification is essential; it is not a
claim for arbitrary characteristic.

Each endpoint fiber is supported at a point of \(Q\), so its local
Artinian algebra makes multiplication by \(q\) nilpotent. Consequently
each coefficient vanishes at both marked base points. That condition
does not make a section of \(\mathcal O(2j)\) identically zero.

For an independent spectrum check, pass on \(x_0=1\) to the generic
base field \(k(\lambda)\), \(\lambda=x_3\), then to an algebraic closure.
The cubic control has four reduced points with \(x_1^4=\lambda\) from
\(C\), four with \(x_1^4=-\lambda\) from \(C^-\), and one from \(L\).
Their \(q\)-values are \(0,2\lambda,\lambda\). At each point, the powers
of the two transverse parameters give local length \(r^2\).
Filtering each Artinian algebra by powers of its maximal ideal shows
that multiplication has its residue value on every successive factor.
Thus, including all nilpotent multiplicities,
\[
\chi_N(T)=T^{4r^2}(T-2\lambda)^{4r^2}(T-\lambda)^{r^2}.
\]
Its trace is \(9r^2\lambda\), which homogenizes to
\(9r^2x_0x_3\). This verifies the sign, all exponents, total rank
\(9r^2\), and the global twist of the displayed trace.

At the generic point of \(C\), the transverse local algebra has residue
field \(K=k(C)\) and finite length \(m\). One may use the explicit
coefficient field \(K=k(x_1/x_0)\) on the chart above, so that
multiplication by \(q\) is a nilpotent \(K\)-linear map. Its number of
Jordan blocks equals
\(\dim_K(A_Y/qA_Y)\), and their total size equals \(m\).
For both controls the quotient is \(A/(q,h^r)\), of dimension \(r\).
The first has dimension \(r^2\); the second has dimension \(r\), with
\(q=0\) and all \(r\) blocks of size one. This verifies the source's
generic interpretation without asserting a uniform Jordan type at the
endpoints. The generic field of the base instead sees four conjugate
sheets of \(C\); these two field conventions have not been confused.

## 6. Primary checks, disposition, and effect on STCI

The primary reference
[Stacks Project, Lemma 10.16.1](https://stacks.math.columbia.edu/tag/00DX)
states the matrix Cayley–Hamilton identity over an arbitrary commutative
ring, supporting its local application and gluing above.
[Stacks Project, Lemma 15.122.1](https://stacks.math.columbia.edu/tag/0GSY)
records multiplicativity of characteristic polynomials and additivity
of traces along finite-length filtrations. The explicit residue-value
filtration above independently supplies the application needed here.
I also checked the scope and hyperosculation discussion in
[Craighero–Gattazzo (1986)](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf),
particularly the introduction and §3: its exclusion concerns two
quartic surfaces. The audit does not use that paper as an arbitrary-degree
exclusion or re-audit its full proof.

The core conclusions pass: identical full restrictions on the fixed
degree-four union can hide different generic thickness; every CI with
the endpoint support conditions gives the specified finite flat cover
and module splitting; and, with the full quadric support condition,
sole support is equivalent to nilpotence of the actual quadric operator.
The control's characteristic polynomial and the generic Jordan/cokernel
interpretation also pass. The cautions about basis degrees and retained
algebra structure above spell out existing distinctions; they are not
unresolved material findings.

The geometric gain is a common ambient interface for arbitrary degrees:
the planes are marked fibers of a finite cover, the quadric is a
twisted multiplication operator, and its quotient records only part of
the transverse thickness. For a supported CI all \(ab\) generic sheets
lie over the degree-four map from \(C\), so its generic transverse
length is necessarily \(ab/4\). None of the reviewed arguments prevents
an actual homogeneous pair from realizing the required nilpotent
algebra, and none constructs one. A claimed obstruction from the fixed
data would still have to exclude all permissible lifts or control the
missing normal action. The unrestricted characteristic-zero STCI
question remains open. No canonical record, source note, navigation
file, or Git state was edited by this reviewer.

## 7. Supplement: reviewed state and general two-layer trace formula

The parent subsequently requested review of the completed additions in
source §§7–8. This supplement covers lines 317–539 of the 539-line source
state with full-file SHA-256
`e362f60aabd1386783a0a8889aeeb5b34ec6fd557494e41a913f448f30f1af29`.
The SHA-256 of those trace-section bytes alone, retaining newlines, is
`fd4fafdc76979f5a4be6503b0b51046466a45d0d44490a95f859f0155391d2a5`.
The changed closeout paragraph in §6 reports the earlier audit; it
does not change its mathematical claims. **The additions also pass
independent hand review, without a material correction.**

First, multiplication by \(xy\) has a homogeneous degree-two trace
\(T(u,v)\). Since \(q=uv-xy\), its trace is \(abuv-T(u,v)\).
Endpoint nilpotence makes this quadratic vanish at \([1:0]\) and
\([0:1]\), giving the claimed forms \(T=\tau uv\) and
\(\operatorname{tr}(q)=(ab-\tau)uv\). Evaluation at \((1,1)\) recovers
\(\tau\) with no loss of a scaling factor.

The finite-free claim used for the deformation is valid over the whole
polynomial coefficient ring \(S=k[u,v,\epsilon]\), not only at generic
parameters. Filter \(S[x,y]\) by fiber degree. Its two fixed leading
forms \(f_0,g_0\) are a regular sequence with finite-dimensional
quotient over \(k\). Any leading cancellation between multiples of
the deformed equations is reduced using the Koszul syzygy of
\(f_0,g_0\). Consequently the associated graded quotient is
\(S\otimes_k k[x,y]/(f_0,g_0)\). Homogeneous basis lifts therefore give
an \(S\)-basis of the deformed algebra, of rank \(ab\). This also
proves freeness after reduction modulo \(\epsilon^3\); no division
by \(\epsilon\) is used to assert flatness at zero.

After inverting \(\epsilon\), substitute \(x=\epsilon X\),
\(y=\epsilon Y\). Homogeneity gives
\[
F_\epsilon(u,v;\epsilon X,\epsilon Y)
=\epsilon^a F(u,v;X,Y),
\quad
G_\epsilon(u,v;\epsilon X,\epsilon Y)
=\epsilon^b G(u,v;X,Y).
\]
Hence the trace of \(xy\) is exactly \(\epsilon^2T(u,v)\).
Both sides are polynomials over the reduced ring \(S\), so equality
after inversion extends to all of \(S\). Taking its second coefficient
after reduction modulo \(\epsilon^3\) proves (12). Layers with index
at least three cannot affect this quotient algebra or its trace.

For the residue formula, the coefficient of \(\epsilon^2\) in the
inverse denominator product is
\[
\frac{f_1^2}{f_0^3g_0}
+\frac{f_1g_1}{f_0^2g_0^2}
+\frac{g_1^2}{f_0g_0^3}
-\frac{f_2}{f_0^2g_0}
-\frac{g_2}{f_0g_0^2}.
\]
The first coefficient is
\(-f_1/(f_0^2g_0)-g_1/(f_0g_0^2)\), and the zeroth coefficient is
\(1/(f_0g_0)\). Multiplication by
\(J_0+\epsilon J_1+\epsilon^2J_2\), then by \(xy\), gives every term
and sign in (14). In particular the mixed term with \(f_1g_1\) has
coefficient one, and the Jacobian's own mixed term is separately
present in \(J_2\).

The analytic residue justification has its hypotheses here: the fixed
leading forms have only the origin as common affine zero, and scaling
brings every deformed root into its neighborhood as \(\epsilon\to0\).
A fixed sufficiently small residue cycle admits the denominator
expansion, whose coefficients are the local residues for the indicated
ordered powers of \((f_0,g_0)\). Algebraic rationality of these residues,
with the leading resultant inverted, transfers the identity from
\(\mathbf C\) to characteristic zero. This includes any field in the
stated setting, since only finitely many coefficients enter an individual
identity and their finitely generated characteristic-zero field embeds
in \(\mathbf C\).

I checked the primary source
[Cattani–Dickenstein–Sturmfels, *Computing Multidimensional Residues*](https://arxiv.org/pdf/alg-geom/9404011),
especially §1's leading-form condition and equation (4.7), which includes
the Jacobian and root multiplicities in the trace identity. It supports
the operation used, including multiple roots. The source correctly
rejects applying a low-degree residue-numerator vanishing statement
directly to \(xy\) as though it were a trace numerator.

Thus the asserted dependence is linear in \(f_2,g_2\) and quadratic in
\(f_1,g_1\) for fixed \(f_0,g_0\). It is not an assertion of polynomial
dependence on freely varying leading forms without inverting their
resultant. Geometrically, this first spectral moment samples the full
fiber algebra but only retains an aggregate already determined by these
two lower layers. It cannot recover the full distribution of quadric
values on the residual sheets.

## 8. Supplement: zero trace with genuine residual sheets

For the displayed quartics, containment of \(C\) follows by substitution,
since \(q|_C=0\) and both remaining binomials vanish on \(C\).
On either endpoint plane, the restrictions are precisely
\[
x_1^2(x_1^2-\alpha x_2^2),\qquad
x_2^2(x_2^2-\beta x_1^2).
\]
A common projective root with both coordinates nonzero would require
\(x_1^2=\alpha x_2^2\) and \(x_2^2=\beta x_1^2\), hence
\(\alpha\beta=1\). If either coordinate is zero, both must be zero,
which is not a point of that projective line. Thus for
\(\alpha\beta\ne1\), these restrictions give just the designated
plane point, with length sixteen. This reasoning covers zero values
of \(\alpha\) or \(\beta\) as well. A common surface factor would meet
the center line \(M\), contrary to this empty intersection; the pair
is therefore proper.

On \(Q\), direct Segre substitution gives \(A^3Vh,-B^3Uh\).
The simultaneous zeros of the residual coefficients occur only at
\(A=U=0\) or \(B=V=0\). These are the two marked endpoints on \(C\).
This proves equality of reduced quadric support with \(C\); it does
not assert that the common scheme is the reduced curve at those points.

For an independent elimination using the actual quadric coordinate,
put \(K=k(\lambda)\), \(w=q\), and \(z=x_1x_2=\lambda-w\). The
equations imply
\[
x_1^4=\lambda-\alpha w(\lambda-w),\qquad
x_2^4=\lambda^3-\beta w(\lambda-w).
\]
Their product yields
\[
P(w)=(\lambda-w)^4
-(\lambda-\alpha w(\lambda-w))
 (\lambda^3-\beta w(\lambda-w))=0.
\]
Its leading coefficient is \(1-\alpha\beta\), and its cubic
coefficient is \(2(\alpha\beta-2)\lambda\). The algebra is free
of rank four over \(K[w]/(P)\), by the monic equation for \(x_1\).
Indeed \(z\) is a unit because the equivalent polynomial for \(z\)
has constant coefficient \(-\lambda^4\). The product relation then
makes \(x_1\) a unit and reconstructs \(x_2=z/x_1\). This supplies
an isomorphism of the full algebras, including their nilpotent parts;
it is not merely a bijection on distinct roots.

Consequently the characteristic polynomial of \(q\) is
\((P(T)/(1-\alpha\beta))^4\). Taking its cubic coefficient and
counting the fourfold extension gives
\[
\operatorname{tr}(q)
=8\frac{\alpha\beta-2}{\alpha\beta-1}\lambda.
\]
Homogenization gives exactly (16). Expanding instead in \(z\) gives
all five coefficients of (18), with the stated signs. This independently
checks its normalization and multiplicity factor.

At \(\alpha=1,\beta=2,\lambda=1\), the monic polynomial of \(w\)
is \(T^4-T^2+T\). Newton identities give the first power sum zero
and the second power sum two in the four-dimensional algebra. Their
values in the full fiber are therefore zero and eight. The quartic
is \(T(T^3-T+1)\), with nonzero roots, so there are actual points
outside \(Q\) on this fiber, not just a nontrivial formal operator.
In particular a globally nilpotent \(q\) is impossible for this pair.

The derivative of the normalized \(z\)-polynomial at its root
\(z=\lambda\) is
\(\lambda^2(\lambda^2-4\lambda+2)\). It is nonzero over \(K\).
The four points over this root are distinct generically, since
\(x_1^4=\lambda\) is separable, and form precisely the four generic
points of the degree-four projection of \(C\). Their simplicity
proves transverse multiplicity one on \(C\), hence residual cycle
degree \(16-4=12\). This is a generic statement, not a claim of
transversality at every attachment or endpoint.

The counterexample therefore invalidates the proposed universal
nonzero-first-trace principle under exactly the endpoint support and
quadric support hypotheses. Its vanishing trace is cancellation among
quadric values on genuine residual sheets. The second moment detects
those sheets in the exhibited pair. No inconsistency of all higher
moment equations for arbitrary defining pairs has been established.
Together with the two-layer formula, this is a precise limitation of
the first invariant, not an unrestricted STCI obstruction. The work
remains reviewed provisional mathematics. No numerical experiment,
source change, navigation update, or canonical promotion was performed
for this supplemental review.
