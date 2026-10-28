# Independent audit: residual capacity through normalization

Date: 2026-10-28. Reviewer: `singular_carrier_construction` research agent,
independent of the root proposer. Source reviewed freshly from disk:
[Residual capacity on a normalization](2026-10-28-residual-degree-normalization.md).

**Outcome: PASS for the singleton inverse-curve inequality, several-branch
linear constraints, first-normal gcd corollary, and general-curve template.**
These are independently reviewed provisional deductions, not canonical
promotions. The gcd corollary is a computable consequence of the inherited
normal-sheaf comparison; the older graph slope inequality supplies a
stronger gcd-only bound, reconstructed in §5 below. An exact numerical
self-intersection can still provide stronger information.

The setup is an actual proper pair in characteristic zero containing the
fixed smooth quartic. The carrier F is integral but may be nonnormal.
Residual degree means ab-4m after removal of the **full** generic
C-primary multiplicity m. No reducedness of the residual, Cartier
condition on inverse curves, or smoothness of those inverse curves is
assumed.

## 1. The two generic normalization length identities

At eta_C, the ambient local ring A is regular of dimension two with
residue field K=k(C). Its quotient B=A/(F) is a one-dimensional
Cohen–Macaulay local domain. Its finite normalization is semilocal with
DVR branches B_i and residue extensions of degrees f_i over K.
Let e_i be the valuation of the maximal ideal of B at branch i.

A general K-linear combination of two regular normal parameters has
valuation exactly e_i at every branch, simultaneously: there are only
finitely many cancellation conditions to avoid, and K is infinite.
It is a minimal reduction parameter of the maximal ideal, so its
quotient length is the multiplicity of B, which equals the normal
order r of F. Computing the same length on the normalization gives

\[
 r=\sum_i e_i f_i.
\]

For the actual G, put n_i=ord_(B_i)(G). Its quotient length in B is
the actual generic intersection multiplicity m. The same comparison
gives

\[
 m=\sum_i n_i f_i.
\]

Here is why the finite normalization introduces no uncounted conductor
length. In 0→B→Bbar→T→0, T has finite B-length. Multiplication by a
nonzero parameter is injective on B and Bbar; its kernel and cokernel
on the finite-length T have equal lengths. The long exact sequence
therefore makes the quotient lengths on B and Bbar equal. This applies
to the general reduction parameter and to G separately. It is not a
claim that the conductor is zero or that it commutes with primary
extraction.

With one branch these give exactly r=ef and m=fn. Applying the same
calculation at every other curve component shows that the residual
Weil divisor upstairs pushes forward, with its valuation and residue-
degree weights, to the actual residual cycle downstairs. Therefore its
hyperplane degree is precisely delta, not a degree of reduced inverse
support.

## 2. Principalization and effectivity with isolated inverse points

On a smooth projective resolution of the normalization which also
principalizes I_C, write I_C O_X=O_X(-Z). In the singleton case,

\[
 Z=e\widetilde\Gamma+Z_{\mathrm{exc}}.
\]

The unique nonexceptional component is the strict inverse curve with
the specified generic ideal valuation. Any isolated inverse point of C
is a point on the normal surface; curves introduced while principalizing
its ideal are exceptional over that normalization. They belong to
Z_exc and have zero intersection with all numerical pullbacks used
below. Thus such points do not invalidate the necessary inequality.
Their separate relevance to a sole-support mate is not discarded.

Global generation of ambient I_C(3) makes L=3H-Z globally generated
after pullback, hence nef. This uses the actual ideal and global
sections; no Cartier divisor 3H-eGamma is silently introduced on the
normalization.

For completeness, numerical pullback of any effective Weil divisor D
is effective. If M=(E_i·E_j) is the negative-definite exceptional matrix
and v_i=Dtilde·E_i>=0, its correction vector q satisfies (-M)q=v.
The matrix -M is positive definite with nonpositive off-diagonal
entries. Pairing this equation with the negative part q_- gives
0<=q_-^t v<=-q_-^t(-M)q_-, so q_-=0. This checks effectivity for the
possibly non-Cartier normalized residual. There is no Q-Cartier
hypothesis hidden in the argument.

Put M_Gamma=Gamma^num. Orthogonality to exceptionals gives independently

\[
 H^2=a,\quad H\cdot M_\Gamma=4f,\quad
 Z\cdot M_\Gamma=e\sigma,\quad H\cdot Z=4ef.
\]

The pullback of the actual Cartier divisor of G is
bH=nM_Gamma+Rbar^num with Rbar^num effective. Consequently

\[
 n(12f-e\sigma)\le b(3a-4ef).
\]

This is the singleton supporting-nef inequality claimed in the source.

## 3. Division, integer strengthening, and Hodge equality

The generic normal order r does imply global membership in the ideal
**sheaf** power I_C^r. Locally C is the regular embedding (u,v) in a
regular threefold. The associated graded of this ideal is a polynomial
ring over the domain O_C, so its powers are I_C-primary and agree with
their generic symbolic order. There is no unsaturated homogeneous-power
claim here.

The inherited all-degree dictionary gives first possible degree 2r.
One can also see this restriction on the containing quadric: if a<2r,
then the restriction vanishing on rC has a negative ruling degree and
is zero, so q divides F. Removing q reduces degree by two and normal
order by one; induction gives the contradiction. Thus a>=2r=2ef.

Hodge index for the nef and big H gives sigma<=(4f)^2/a. Therefore

\[
 12f-e\sigma\ge\frac{4f}{a}(3a-4ef)>0,
\]

since a>=2ef. The source's division is valid even for an inverse curve
which is not Q-Cartier. Substituting m=fn into delta=ab-4fn yields

\[
 \delta\ge\frac{be(16f^2-a\sigma)}{12f-e\sigma}.
\]

Integrality of n gives the displayed floor formula and delta congruent
to ab modulo 4f. Both are stronger than merely rounding the real bound
to an arbitrary integer. The Hodge numerator is nonnegative; equality
is numerical proportionality of M_Gamma and H on the resolution. A
zero numerator yields zero from this bound, not a descending equation
on the original nonnormal carrier. The source retains R-0003's
conductor obligation explicitly.

Normal and smooth specializations have e=f=1 and give exactly the
earlier normal capacity and smooth-along-C capacity expressions.

## 4. Several branches and the mate-order refinement

Let M_i=Gamma_i^num and Z^num=sum e_i M_i. The difference Z-Z^num is
exceptional. Therefore

\[
 \ell_i=L\cdot M_i
 =12f_i-\sum_j e_j(M_j\cdot M_i)\ge0.
\]

Nonnegativity uses nefness of L and effectivity of M_i, including its
exceptional correction. Pulling back the actual G divisor now gives
sum n_i ell_i<=b(3a-4r), with m=sum n_i f_i. These are constraints on
the actual integer valuation vector, not on arbitrary formal branch
weights that have already been globally realized.

If the ambient mate has exact generic normal order s, then membership
in I_C^s gives n_i>=s e_i. Write x_i=n_i-s e_i>=0. Independently,

\[
 \sum_i e_i\ell_i=12r-(Z^{\mathrm{num}})^2.
\]

Thus, with kappa=min ell_i/f_i>0,

\[
 \begin{aligned}
 \kappa(m-rs)
 &\le\sum_i x_i\ell_i\\
 &\le b(3a-4r)-s\bigl(12r-(Z^{\mathrm{num}})^2\bigr).
 \end{aligned}
\]

This is exactly the claimed refinement. Dropping the baseline produces
the coarser scalar bound. If a branch has ell_i=0, this particular
minimum-slope argument does not bound all its n_i; conductor or other
relations would need additional work. A negative right side with the
specified s signals incompatible data. No uniform positive residual
fraction follows from these linear constraints alone.

## 5. First-normal gcd corollary and its comparison with the graph

For the integral carrier regular at eta_C, r=1 implies a unique
normalization branch with e=f=1. In the promoted balanced conormal
splitting, the nonzero first-normal map is
O_P1(-4a)→O_P1(-7)^2. If its two binary-form coefficients have a common
divisor of degree d_F, the saturation of its image is
O_P1(-4a+d_F). The torsion-free quotient has degree 4a-14-d_F, so

\[
 \deg N_{C/S}=14-4a+d_F.
\]

This uses the **whole** common-zero divisor of the actual first-normal
section. It is not a common singularity assertion about F and G or
an attachment length to the full thick component.

The source correctly invokes the earlier reviewed numerical-pullback
comparison as a premise in its literal generically regular integral
scope; that theorem does not require S normal everywhere on C. Its
upper bound sigma<=14-4a+d_F and the decreasing function
b(16-at)/(12-t) give the claimed gcd-only formula. The strict condition
d_F<4a-14+16/a makes its numerator positive. Since actual coefficients
have degree 4a-7, one also has d_F<=4a-7 and the denominator
4a-2-d_F>=5 automatically. The degree-five example checks exactly:
d_F<=5 makes the normal-sheaf upper bound at most -1; evaluation of
the decreasing capacity function at -1 gives delta>=21b/13. Integer d_F<=9 meets the
strict positive threshold for a=5.

There is an essential attribution/comparison qualification. The
[graph note, new §7](2026-10-28-residual-degree-blowup-bounds.md) applies
the already reviewed October 19 root-slope inequality. After the gcd
is removed, the first-normal pair defines the **only** horizontal root
graph in E, of degree h=4a-7-d_F. Every horizontal component of the
actual strict-pair intersection must lie on that graph. Thus
u>=h(m-s), even if m=s and this is vacuous. Substitution yields

\[
 \delta\ge
 \frac{b(4a^2-14a+16-a d_F)+4s d_F}{4a-2-d_F}.             \tag{A}
\]

If the actual residual has no component on Q, the denominator is
4a-6-d_F instead. Both are positive by h>=0. Formula (A) is at
least the source's coarse gcd formula and is strictly stronger when
d_F>0. It requires no normality assumption and may even be used without
integrality of F. The gcd corollary must therefore not be advertised as
a new independent stronger mechanism. It is still a useful transparent
route to understanding why singular first-normal data weaken the
smooth capacity computation. The exact singleton bound using sigma
can exceed (A) if the old normal-sheaf comparison is strict. One should
combine these available inequalities, rather than rank them uniformly.

## 6. General smooth-curve template and retained boundary

For smooth degree-c C with I_C(d_0) generated, the same principalization
uses L=d_0 H-Z. In the singleton case its intersection with the
effective residual gives

\[
 n(d_0 c f-e\sigma)\le b(d_0a-cef).
\]

Hodge gives sigma<=c^2f^2/a, and the stated assumption d_0a>cef
therefore makes the denominator positive. Substitution in
deg R=ab-cfn gives exactly

\[
 \deg R\ge\frac{be(c^2f^2-a\sigma)}{d_0cf-e\sigma}.
\]

Thus the general template has the correct factors c,e,f and the correct
division hypothesis. It makes no fixed positive claim when the Hodge
gap is zero.

The standard numerical-pullback inputs were checked live in the primary
texts [Mumford (1961)](https://www.numdam.org/item/10.1007/BF02698717.pdf)
and [Schröer (2019), introduction and §1](https://www.journalofsing.org/volume19/schroer.pdf);
the effectivity matrix argument is independently reconstructed above.
The earlier pending October 17 sufficiency proposal is not used.

No mathematical correction to the singleton or multi-branch formulas
was required. The review adds the explicit comparison in §5 to avoid
presenting the coarse gcd consequence as a new independent restriction.
All assertions remain necessary quantitative constraints with genuine
residual cycles and their full generic multiplicities retained.
