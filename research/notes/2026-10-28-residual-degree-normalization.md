# Residual capacity on a normalization: one inverse curve and several branches

Date: 2026-10-28. Author: root integration agent. **Provisional contribution,
independently reviewed in the [separate audit](2026-10-28-residual-degree-normalization-audit.md);
no canonical promotion.** Work over an
algebraically closed field of characteristic zero with the fixed smooth
quartic \(C=[s^4:s^3t:st^3:t^4]\).

The question is quantitative: for an actual proper pair
\([V(F_a,G_b)]=m[C]+R\), what geometric data force a lower bound on
\(\delta=\deg R=ab-4m\)? The bound here allows an integral **nonnormal**
carrier and does not require its inverse curve to be Cartier or smooth.
It extends the [normal-carrier capacity calculation](2026-10-28-residual-degree-singular-carriers.md).

## 1. Hypotheses and prior scope

Let \(S=V(F_a)\) be integral, let \(G_b\) not vanish identically on \(S\),
and assume both contain \(C\). Let \(\nu:\bar S\to S\) be the finite
normalization. First assume there is exactly one divisorial component
\(\Gamma\) above \(C\). Isolated inverse points are allowed. Put

\[
f=[k(\Gamma):k(C)],\qquad
e=\operatorname{ord}_\Gamma(I_C O_{\bar S}),\qquad
\sigma=(\Gamma^{\rm num})^2.
\]

Here \(\Gamma^{\rm num}\) is Mumford's numerical pullback to a smooth
resolution of \(\bar S\). Its square is independent of that resolution.
There is no assumption that \(\Gamma\) is \(\mathbf Q\)-Cartier.

Retrieval followed INDEX and MAP, then the reviewed
[smooth-carrier capacity proof](2026-10-27-absorption-deformation-interface.md),
the [all-degree equation-space dictionary](2026-10-28-blowup-residual-geometry.md),
and the [new normal-carrier note](2026-10-28-residual-degree-singular-carriers.md).
The older [Mumford normal-sheaf note](2026-10-05-mumford-normal-bound.md)
and [October 17 Hodge-gap proposal](2026-10-17-generalization-normal-carrier-extremal-ray-synthesis.md)
were located. The latter's pending sufficiency theorem is **not** an input.
This is a necessary residual-capacity inequality, with no claim that its
zero-gap boundary supplies conductor descent or a mate.

## 2. A bound with a single divisorial inverse

**Proposition.** In the above setting, the exact generic normal order of
\(F_a\) along \(C\) is \(r=ef\), and

\[
\boxed{
\delta\ \ge\
\frac{b e(16f^2-a\sigma)}{12f-e\sigma}.
}\tag{1}
\]

The denominator is strictly positive; the numerator is nonnegative. The
right side is positive if the inverse curve is not numerically proportional
to the hyperplane class. The sharper integer version is

\[
\boxed{
\delta\ge ab-4f\left\lfloor
\frac{b(3a-4ef)}{12f-e\sigma}
\right\rfloor,
\qquad \delta\equiv ab\pmod{4f}.
}\tag{2}
\]

This applies to the genuine residual cycle after the full \(C\)-primary
component is removed. No reducedness of \(R\) is assumed.

**Proof.** Choose a smooth projective resolution \(X\to\bar S\) also
principalizing the pulled-back ideal of \(C\). Write \(H\) for the
hyperplane pullback and

\[
I_C O_X=O_X(-Z),\qquad
Z=e\widetilde\Gamma+Z_{\rm exc}.
\]

All components of \(Z_{\rm exc}\) map to points on \(\bar S\), including
those coming from isolated inverse points of \(C\). The inherited global
generation of \(I_C(3)\) makes
\(L=3H-Z\) globally generated, hence nef. Put \(M=\Gamma^{\rm num}\).
Numerical pullback is effective, is orthogonal to exceptional curves and
agrees with ordinary pullback on Cartier divisors. Consequently

\[
H^2=a,\quad H\cdot M=4f,\quad
Z\cdot M=e\sigma,\quad H\cdot Z=4ef. \tag{3}
\]

For clarity, the two multiplicity assertions need normalization length
formulas, not just intersection classes. At \(\eta_C\), the local ring
of \(S\) is the one-dimensional hypersurface in the two-dimensional
regular local ring \(O_{\mathbf P^3,\eta_C}\). Its multiplicity is the
normal order \(r\) of \(F\). Normalize this ring. A general local normal
linear form has valuation \(e\) on its sole normalization branch, whose
residue extension has degree \(f\). Thus \(r=ef\). If
\(n=\operatorname{ord}_\Gamma G\), the same length formula gives
\(m=fn\). One direct justification is to compare the ring and its finite
normalization: multiplication by the chosen parameter on their finite-
length quotient has kernel and cokernel of equal length, so the quotient
lengths in the ring and normalization agree.

On \(\bar S\), the effective Cartier divisor of \(G\) has Weil cycle
\(n\Gamma+\bar R\). Its numerical pullback satisfies

\[
bH=nM+\bar R^{\rm num},\qquad \bar R^{\rm num}\ge0.
\]

The latter includes all normalized residual contributions. Its pushforward
has exactly the actual cycle \(R\), and its \(H\)-degree is \(\delta\).
Intersecting with the nef \(L\), using (3), gives

\[
n(12f-e\sigma)\le b(3a-4ef). \tag{4}
\]

To check division is legitimate, Hodge index for the nef and big \(H\)
gives \(\sigma\le16f^2/a\). Also \(a\ge2r=2ef\): a form of generic
order \(r\) belongs to the ideal sheaf power \(I_C^r(a)\), whose first
possible degree is \(2r\), as in the inherited equation-space calculation.
Therefore

\[
12f-e\sigma\ge\frac{4f}{a}(3a-4ef)>0.
\]

Finally \(\delta=ab-4fn\). Substituting (4) gives (1), and integrality
of \(n\) gives (2). Hodge equality is precisely numerical proportionality
of \(M\) to \(H\) on the resolution. This completes the proof. □

## 3. Relation to the normal and smooth carrier bounds

For a normal \(S\), \(f=e=1\). Equation (1) becomes

\[
\delta\ge b\frac{16-a C_{\rm num}^2}{12-C_{\rm num}^2},
\]

the new normal-carrier bound. If \(S\) is smooth along \(C\),
\(C^2=14-4a\); it becomes the inherited sharp capacity estimate

\[
\delta\ge b\frac{4a^2-14a+16}{4a-2}\ge\frac{ab}{3}.
\]

Thus the smooth bound is one explicit self-intersection computation inside
a larger geometric inequality. For a nonnormal singleton inverse, a zero
Hodge gap only makes this numerical bound vanish. It does not test the full
conductor or guarantee the required section descends. The exact conductor
criterion remains [R-0003](../results/fixed_carrier_conductor_criterion.md).

## 4. Several inverse curves give a finite collection of linear constraints

If the divisorial inverse consists of \(\Gamma_1,\ldots,\Gamma_t\), put
\(e_i=\operatorname{ord}_{\Gamma_i}I_C\),
\(f_i=[k(\Gamma_i):k(C)]\), \(M_i=\Gamma_i^{\rm num}\), and
\(Z^{\rm num}=\sum e_iM_i\). The same argument gives

\[
r=\sum_i e_i f_i,\qquad
m=\sum_i n_i f_i,\qquad
n_i=\operatorname{ord}_{\Gamma_i}G.
\]

Define the nonnegative rational numbers

\[
\ell_i=(3H-Z)\cdot M_i
=12f_i-\sum_j e_j(M_j\cdot M_i)\ge0.
\]

Then the actual valuation vector satisfies

\[
\boxed{\sum_i n_i\ell_i\le b(3a-4r).}\tag{5}
\]

If \(s\) is the exact generic normal order of the mate, then also
\(n_i\ge s e_i\). Thus intersection data on the normalization provide
an explicit linear bound on \(m=\sum n_i f_i\). If
\(\kappa=\min_i\ell_i/f_i>0\), a scalar consequence is

\[
m\le\frac{b(3a-4r)}\kappa,
\]

and the normal-order refinement is

\[
m\le rs+
\frac{b(3a-4r)-s(12r-(Z^{\rm num})^2)}\kappa. \tag{6}
\]

All inequalities can be combined with \(\delta=ab-4m\), integrality
and the inherited graph bounds. A branch with \(\ell_i=0\) prevents
this minimum-slope scalar argument from controlling arbitrary \(n_i\).
Additional conductor relations may constrain those vectors, but have not
been computed here. No classification of multi-branch realizability is
asserted.

## 5. A directly computable bound from first-normal zeros

There is a useful specialization needing neither normality of \(S\) nor
a computation of its whole resolution. Assume that the integral carrier
\(S=V(F_a)\) is regular at \(\eta_C\), equivalently its generic normal
order is one. The divisorial inverse then has \(e=f=1\). Let \(d_F\)
be the degree of the common-zero divisor of the first-normal section of
\(F\) on \(C\). This is the finite singularity divisor of the actual
equation along \(C\), counted with its first-symbol vanishing orders.

In the promoted characteristic-zero splitting
\(N^*_{C/\mathbf P^3}=O_{\mathbf P^1}(-7)^2\), the two coefficient
sections have degree \(4a-7\). Thus \(d_F\) can be obtained by taking
their binary-form gcd; it is independent of a constant change of balanced
frame. The saturated first-normal image has degree \(-4a+d_F\), so

\[
\deg N_{C/S}=14-4a+d_F.
\]

The inherited [numerical-pullback versus normal-sheaf theorem](2026-10-05-mumford-normal-bound.md),
with its [independent audit](2026-10-06-normal-bound-independent-audit.md),
applies to this generically regular integral carrier and gives
\(\sigma\le14-4a+d_F\). Its hypotheses do not require normality at
every point of \(C\). The accepted comparison is used as a premise,
not rerun here.

The function \(b(16-at)/(12-t)\) is decreasing for \(t<12\), since
its derivative is \(b(16-12a)/(12-t)^2<0\). Since
\(d_F\le4a-7\), the comparison value \(14-4a+d_F\le7<12\)
and its denominator is always at least five. The following bound is
therefore valid for every such order-one carrier; it is positive when

\[
d_F<4a-14+16/a,
\]

and has the explicit form

\[
\boxed{
\deg R\ge
b\frac{4a^2-14a+16-a d_F}{4a-2-d_F}.
}\tag{7}
\]

Its integer version is

\[
\deg R\ge ab-4\left\lfloor
\frac{b(3a-4)}{4a-2-d_F}\right\rfloor. \tag{8}
\]

The strict displayed inequality characterizes positivity of the numerator;
outside that region the lower bound can be zero or negative and should be
combined with \(\deg R\ge0\). If \(d_F=0\), (7) is exactly the smooth-along-\(C\)
bound. For a degree-five carrier, \(d_F\le9\) already gives a positive
bound; for example \(d_F\le5\) gives \(\deg R\ge21b/13\), strengthened
by the integer/congruence version. These are conditional statements about
any actual carrier with those data, not existence claims for every gcd.

This gives an accessible intermediate target: control the common-zero
divisor of an actual first-order carrier, before trying to bound every
marked resolution correction. The divisor is neither the full-primary
equation-module torsion nor an assertion that the two carriers have a
common singular point. A carrier singular generically along \(C\) has
identically zero first-normal section and is outside this corollary; use
the normalization valuations or the order-dependent graph bound there.

There is an essential comparison with older work. The saturated normal
direction has degree \(h=4a-7-d_F\). Applying the October 19 root-slope
refinement, as made explicit in the
[graph source, §7](2026-10-28-residual-degree-blowup-bounds.md), gives

\[
\delta\ge
\frac{b(4a^2-14a+16-a d_F)+4s d_F}{4a-2-d_F}, \tag{9}
\]

where \(s\) is the mate's actual generic normal order. Its denominator
is again positive. This strengthens the coarse corollary (7) and also
works without normality. Thus (7) is a convenient consequence of the
retrieved normal-sheaf comparison, not a new independently stronger
restriction than the existing graph machinery. The exact normalization
bound uses \(\sigma\), which may be strictly smaller than
\(14-4a+d_F\); it can give a stronger bound than either gcd-only
formula. Compare the actual inputs rather than imposing one ranking.

## 6. General template and literature boundary

For a smooth degree-\(c\) curve with \(I_C(d_0)\) globally generated,
the singleton calculation gives

\[
\deg R\ge
\frac{be(c^2f^2-a\sigma)}{d_0 c f-e\sigma},
\]

provided \(d_0a>cef\), which ensures a positive denominator by Hodge
index. This displays exactly which input uses the fixed quartic.

The proof applies standard surface intersection theory. Primary sources
inspected on 2026-10-28 include
[Mumford, *The topology of normal singularities of an algebraic surface and
a criterion for simplicity*](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1961a--TopSingSurface-NumDam.pdf)
and [Schröer, *A higher-dimensional generalization of Mumford's rational
pullback for Weil divisors*, introduction and §1](https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/MumfordsRationalPullback.pdf).
These provide the numerical pullback and its effectivity/exceptional
orthogonality. The residual-capacity application is proved above; no
literature novelty is claimed. No finite sample or inherited verifier is
used in place of the argument.
