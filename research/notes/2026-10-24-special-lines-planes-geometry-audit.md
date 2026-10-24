# Independent geometry audit: special lines and planes

Date: 2026-10-24. Reviewer: independent agent geometry_final_audit.
Scope: Sections 2–6 and the geometric conormal input of Section 10 of the
[research note](2026-10-24-special-lines-planes-research-note.md).

**Outcome:** one substantive omitted-components error was found in the
initial dual-surface statement. The corrected reduced singular locus has
four components, not two. The correction is proved below. The other
reviewed geometric statements and normal-direction count are verified
with their stated hypotheses. This is independent review of provisional
research evidence, not canonical promotion or an STCI obstruction.

## 1. Method and retained input

The reviewer read the research index first, then reconstructed the
arguments from the embedding and binary quartic system. The only accepted
bundle input used was
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md), namely
$E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2$ in characteristic zero.
Its proof and the degree-four carrier exclusion were not rerun.

The reviewer independently expanded the restricted quartic discriminant,
its derivatives, and the local intersection of the two dual quartics with
SymPy 1.14.0. The new identity verifier was also executed successfully.
Those computations support the proofs below; its initial passing version
did not detect the omitted components in the prose and therefore could
not be treated as evidence of completeness.

## 2. Quadric, line lengths, and endpoint tangents

The quadratic coordinate monomials have pullback exponents
$0,1,2,3,4,4,5,6,7,8$. Hence their kernel is exactly
$q=x_0x_3-x_1x_2$. On the smooth Segre quadric,

\[
(x_0,x_1,x_2,x_3)=(ac,ad,bc,bd),\qquad
C=V(bc^3-ad^3)\sim(1,3).
\]

The cubic projection to $[a:b]$ has fibers of length three and exactly
two totally ramified fibers. The other ruling projection is the identity
on the parameter line. If a line is not contained in $Q$, its nonzero
quadratic restriction bounds its intersection length with $C$ by two.
Consequently all lines meeting $C$ in length greater than two are
exactly the cubic ruling fibers, with length three. This proof includes
nonreduced line sections, not just three distinct contact points.

The endpoint tangent lines are those totally ramified ruling fibers.
For $u\ne0,\infty$, substituting the tangent parametrization in $q$
gives $-3u^2\mu^2$, so the tangent is not on $Q$ and has length exactly
two. Two distinct finite points lie on a ruling precisely when their
cubes agree. No line has length four on $C$, and no cubic-ruling fiber
has partition $[2,1]$.

## 3. Osculation, involution, bitangency, and incidences

In the incomplete hyperplane system with missing quadratic coefficient,
a section $(z-u)^3(z-r)$ belongs to the system at nonzero finite $u$
exactly when $r=-u$. This yields

\[
H_u=[-u^4:2u^3:-2u:1],\qquad H_u|_C=3u+(-u).
\]

At each endpoint, every plane through the tangent line has contact at
least three, and the unique contact-four member is the limit of generic
osculating planes. The distinction between this limiting plane and the
rank-deficient ordinary second jet is necessary and is correctly made.
The residual involution and its extension
$\operatorname{diag}(1,-1,-1,1)$ are correct.

For two double roots, expansion gives $u^2+4uv+v^2=0$.
Thus the two partner ratios are $-2\pm\sqrt3$, not $-1$.
The conic $\beta^2+2\alpha\gamma=0$ parametrizes the bitangent
quadratics, and its intersection with the diagonal conic
$\beta^2-4\alpha\gamma=0$ is two tangent intersections of length two.
Both limiting bitangent planes are the hyperosculating planes.

Paired osculating planes contain the same two distinct contact points,
so their intersection is the paired secant. The common-divisor
description of $C\cap(H\cap K)$ follows from the local DVR minimum
formula. A bitangent and osculating plane sharing a nonendpoint contact
meet in its tangent line. A plane containing two distinct tangent lines
has two double zeros in its section, proving the bitangent criterion.
If one contact were an endpoint, its order would be at least three,
excluding a second distinct tangency. This verifies the endpoint cases
of that incidence claim.

## 4. Paired-secant cubic, singularities, and polarity

The family $[A:B:zB:z^2A]$ lies on
$R=x_0x_2^2-x_1^2x_3$. Conversely $z=x_2/x_1$ recovers a general
point of this irreducible cubic. Its singular locus is
$E_+=V(x_1,x_2)$, and the map from ruling parameter to it is
$z\mapsto z^2$. Its two branch values give the pinch points. The
affine equation at the first is $x_2^2=x_1^2x_3$.

At $c(u)$ the gradient is $-u^2H_u$, and on $Q$ the equation is
$ab(bc^3-ad^3)$. Hence the tangent-plane identity and the actual
residual divisor $R|_Q=C+L_0+L_\infty$ are correct. The surface is
not developable, since its gradient varies along a general ruling.
At the singular endpoints its tangent-plane field must be interpreted
after saturation, as done in Section 10.

The polarity of $q$ sends plane coefficients
$[h_0:h_1:h_2:h_3]$ to $[h_3:-h_2:-h_1:h_0]$.
It gives the stated pole $[1:2u:-2u^3:-u^4]$ and polar line
$V(x_3+u^4x_0,x_2+u^2x_1)$. The latter differs from the paired
secant for nonendpoint $u$.

## 5. Substantive correction: two extra dual singular lines

The initial Section 6 asserted that the singular set of the restricted
discriminant was just the osculating quartic and bitangent quartic.
That is false: the closure of generic osculating planes is smaller
than the locus of all triple-root sections at the endpoint jet drops.

Write plane coefficients as $[A:B:C:D]$, with affine binary section
$f(z)=A+Bz+Cz^3+Dz^4$. Every member of

\[
\ell_0=\{[0:0:C:D]\}
\]

has a triple root at zero, since $f=z^3(C+Dz)$. Likewise

\[
\ell_\infty=\{[A:B:0:0]\}
\]

consists of sections with a triple root at infinity. These are the
pencils of planes through the endpoint tangent lines. Except at their
contact-four members, they are not in the osculating quartic.
Both lines nevertheless lie in the singular locus, because the full
discriminant differential vanishes at triple-root sections.

The exact restricted discriminant is

\[
\begin{aligned}
\Delta={}&256A^3D^3-192A^2BCD^2-27A^2C^4\\
&-6AB^2C^2D-27B^4D^2-4B^3C^3.
\end{aligned}
\]

Direct differentiation gives $\Delta=\nabla\Delta=0$ on both lines.
The complete reduced singular locus is

\[
\operatorname{Sing}(C^\vee)_{\mathrm{red}}
=\mathcal O_{\mathrm{dual}}\cup\mathcal B_{\mathrm{dual}}
 \cup\ell_0\cup\ell_\infty.
\]

Here the first two components are the rational quartics in the note.
For completeness, a quartic with exactly one double root and other
roots distinct is a smooth point of the full discriminant; its
differential is a nonzero multiple of evaluation at that root.
Restriction to the basepoint-free system $W$ cannot annihilate it.
All remaining discriminant sections have a triple root or two double
roots. Nonendpoint triple roots give the osculating quartic; endpoint
triple roots give the two lines; two double roots give the bitangent
quartic. This classifies the reduced set, not the nilpotent structure
of the singular subscheme.

The dual surface is still reduced irreducible of degree six. Its
tangent-plane incidence is an irreducible projective-line bundle over
$C$, and a general simple double root is smooth on the restricted
discriminant. The homogeneous degree-six equation has no extra factor
or repeated component.

The intersection statement for the two quartics remains correct:
near $H_0$, their affine parametrizations give the ideal
$(w-u,u^3)$, of length three; infinity is symmetric. The added lines
meet these quartics only at the corresponding hyperosculating plane.
Their omission changes the dual singular-set claim, but not the
incidence divisor $3\Delta+\Gamma_\iota$ of the limiting osculating
family.

## 6. Conormal reference line and coincidence count

The degree-four homogeneous osculating plane vector is nowhere zero.
It annihilates the point vector and tangent direction, and hence gives
$\mathcal O(-4)\subset E(4)$ by the Euler and conormal sequences.
Thus $L_{\mathrm{osc}}=\mathcal O(-8)\subset E$ is a subbundle even
at the endpoints. Independently, the scroll's first normal symbol is
$u^2(2uv-w)$ near zero, and the reverse chart gives order two at
infinity. Saturation removes exactly four zeros and gives the same
line.

For a nonzero first normal symbol of a degree-$d$ equation with base
divisor $A_F$, the saturated line has degree $\deg A_F-4d$.
Its wedge with $L_{\mathrm{osc}}$ therefore has degree
$4d-6-\deg A_F$, unless it is identically zero. At a zero first
symbol this compares saturated limiting directions, not an actual
smooth tangent plane.

Euler's relation and differentiation of $F(c(u))=0$ give
$P_F(1,u)=4u^3(F_{x_2}+2uF_{x_3})$, and reversal gives the factor
$s^3$. This proves the homogeneous quotient formula, with the base
divisor removed before counting coincidences.

The explicit cubic has nonzero gradient at every curve point and
$P_F=4s^3t^3(s^6+t^6)$, giving six distinct coincidences.
The equation $x_0F+q^2$ has the same saturated direction, but the
pair's support contains exactly the two residual trisecant lines in
the Segre factorization. It is therefore a valid test of an unscoped
small normal-direction bound, and not an actual-STCI counterexample.

## 7. Review boundary

All reviewed claims concern this fixed embedding in characteristic zero.
The mandatory correction is the four-component reduced dual singular
locus. The audit records the rejected two-component assertion rather
than silently replacing it with a PASS.

The reviewer reread the amended Section 3 endpoint-pencil description,
Section 6 four-component statement and completeness proof, and Section 10
balanced-projective-bundle interpretation. The endpoint pencils are
correctly described, the dual claim is now explicitly about the reduced
singular locus, and the degree-one osculating section can indeed be
identified with a diagonal in the balanced product, giving intersection
number $\mu+1$. The amended identity verifier also passes, including
vanishing of all discriminant derivatives on the extra lines.
The explicit Segre factorization has the scalar sign
$(a^2-b^2)(bc^3-ad^3)$, as in the main note.

**Final corrected outcome:** no remaining discrepancy is identified in
the reviewed geometry. The unrestricted STCI problem and canonical
status are unchanged.
