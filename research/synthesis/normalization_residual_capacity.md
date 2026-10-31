# Residual capacity on normalizations

For an actual proper pair on the fixed quartic, write [Y]=m[C]+R and delta=deg R=ab-4m. This chapter contains reviewed provisional necessary inequalities, not a new canonical promotion. Its input is the nef line bundle obtained by principalizing the actual marked ideal. Marked attachment and full attachment belong to [the attachment chapter](residual_capacity_and_constructions.md).

## 4. A uniform residual floor when a carrier is smooth along C

**Proposition.** Let \(S=V(F_a)\) now be any **integral** surface smooth at every
point of \(C\), possibly singular away from \(C\). Let \(G_b\) give a proper
intersection, and let \(m\) be its exact generic multiplicity along \(C\).
Write the effective Cartier divisor on \(S\) as

\[
V(G_b|_S)=mC+D,
\]

where \(D\) has no component \(C\). Then

\[
m\le\frac{b(3a-4)}{4a-2},
\qquad
\frac{4m}{ab}\le
\frac{4(3a-4)}{a(4a-2)}\le\frac23,
\qquad
\boxed{\deg D=ab-4m\ge\frac{ab}{3}.}
\tag{3}
\]

**Proof.** Because \(S\) is smooth along \(C\), the curve is Cartier there;
off \(C\) its ideal is the unit ideal. Hence it is a global Cartier divisor
on \(S\), regardless of singularities away from it. The line bundle
\(L=3H-C\) remains globally generated, as above. It consequently has
nonnegative degree on every integral curve, and \(L\cdot D\ge0\).

The normal sequence along \(C\) gives

\[
\deg N_{C/S}
=\deg N_{C/\mathbf P^3}-\deg\mathcal O_C(a)
=14-4a.
\]

Here \(\deg N_{C/\mathbf P^3}=4\deg C+2g(C)-2=14\) follows from the Euler and
tangent sequences; no splitting hypothesis is used. This is \(C^2\), since
\(C\) is Cartier. With \(H^2=a\) and \(H\cdot C=4\),

\[
0\le(3H-C)\cdot(bH-mC)
=b(3a-4)-m(4a-2).
\]

This proves the first inequality. The curve is nonplanar, so \(a\ge2\).
For integer \(a\ge2\),

\[
\frac23-\frac{4(3a-4)}{a(4a-2)}
=\frac{8(a-2)(a-3)}{3a(4a-2)}\ge0.
\]

The remaining assertions follow. Intersection degrees of Cartier line
bundles and effective curves are well-defined on the possibly singular
projective \(S\); smoothness away from \(C\) is not required. ∎

The constant \(1/3\) is sharp as a uniform bound. On the unique smooth
quadric \(Q\), put \(A=x_0^2x_2-x_1^3\). Its divisor on \(Q\) is \(C+2\ell\)
for a ruling line \(\ell\): in Segre coordinates
\((x_0,x_1,x_2,x_3)=(su,sv,tu,tv)\) one has
\(A=s^2(tu^3-sv^3)\), where \(tu^3-sv^3\) cuts out \(C\) and \(s=0\)
cuts out \(\ell\). This factorization, rather than divisor classes alone,
specifies the double line. The actual pairs \((q,A^n)\) of degrees \((2,3n)\) have cycle
\(n[C]+2n[\ell]\); residual degree \(2n=(2\cdot3n)/3\).
This elementary powering control tests sharpness and is not claimed as a
new construction or a separate low-degree research program.

More generally, for a smooth connected curve of degree \(e\), genus \(g\),
and globally generated \(I_C(\delta)\), the same carrier calculation gives

\[
0\le b(\delta a-e)
-m\bigl(e(a+\delta-4)-(2g-2)\bigr).                 \tag{4}
\]

One can solve (4) for an upper bound on \(m\) only when its displayed
coefficient of \(m\) is positive. No universal residual fraction is claimed
for arbitrary curves. The fixed quartic yields (3) upon substituting
\((e,g,\delta)=(4,0,3)\).



### Effective-cone interpretation and construction limits

There is an effective-cone interpretation with no degree enumeration. On a
fixed carrier write
\[
\tau_{\mathrm{eff}}(S,C)=
\sup\{t\ge0:[H-tC]\text{ is pseudo-effective}\}.
\]
For the general-curve hypotheses of (4), global generation of
\(\delta H-C\) gives \(\tau_{\mathrm{eff}}\ge1/\delta\).
When \(e(a+\delta-4)-(2g-2)>0\), intersecting a pseudo-effective class
with the nef \(\delta H-C\) gives
\[
\frac1\delta\le\tau_{\mathrm{eff}}(S,C)
\le\frac{\delta a-e}{e(a+\delta-4)-(2g-2)}.
\]
The actual threshold need not equal this supporting-nef upper bound. The [partial-transfer construction](marked_deformation_and_absorption.md) works safely in a very ample range and can absorb arbitrary finite amounts on a fixed carrier; the residual floor here supplies its separate capacity limitation. In particular, moving more than two thirds of the CI degree onto C requires every integral carrier of the pair to fail smoothness somewhere along C. Smoothness along C is the exact hypothesis for this floor; smoothness elsewhere is unnecessary. Singular or nonnormal carriers remain outside that smooth-carrier assertion.

## Normal carriers: numerical pullback and the Hodge gap

Let S=V(F_a) be a **normal integral** surface containing C=C0, and let G_b give a proper intersection with actual cycle [V(F_a,G_b)]=m[C]+R. Here m is the full generic length and R is the effective weighted residual cycle with no C-component. No reducedness of R or Q-Cartier hypothesis on C is imposed.

## 2. The normal-carrier residual bound

Use Mumford's numerical self-intersection

\[
 c_S^2=(f^{\mathrm{num}*}C)^2,
\]

computed on any smooth projective resolution f:X→S. Numerical pullback
means strict transform plus the unique rational exceptional divisor
making the result orthogonal to every f-exceptional curve. It is defined
for Weil divisors even when C has no Cartier multiple.

**Proposition.** Under these normal-carrier hypotheses,

\[
 c_S^2\le\frac{16}{a}<12,
\qquad
 m\le\frac{b(3a-4)}{12-c_S^2},                           \tag{2}
\]

and consequently

\[
 \boxed{\deg R\ge
 \frac{b(16-a c_S^2)}{12-c_S^2}.}                         \tag{3}
\]

The right side is strictly positive whenever c_S^2<16/a. If the Hodge
gap is zero, this estimate is zero. No positive lower bound is inferred
there. Since m is an integer, the stronger directly usable form is

\[
 \deg R\ge ab-4\left\lfloor
 \frac{b(3a-4)}{12-c_S^2}\right\rfloor.                   \tag{4}
\]

Thus the bound automatically respects deg R congruent to ab modulo four.

### Proof: effective residual upstairs, with no Q-Cartier shortcut

Choose a smooth projective f:X→S which also principalizes the actual
ideal I_(C/S). Write

\[
 I_{C/S}\mathcal O_X=\mathcal O_X(-Z),\qquad
 Z=\widetilde C+Z_{\mathrm{exc}}.                         \tag{5}
\]

The coefficient of the strict transform is one because a normal surface
is regular at the generic point of C. Every other component is
exceptional. Global generation of I_C(3) in P3 descends to I_(C/S)(3)
and then pulls back to the invertible ideal in (5). Hence, with
H=f^*O_S(1),

\[
 L=3H-Z
\]

is globally generated and nef.

We must also justify effectivity of the numerical pullback of **R**,
which need not be Cartier. Let E_i be the exceptional curves,
M=(E_i·E_j), and v_i=\widetilde R·E_i>=0. For

\[
 R^{\mathrm{num}}=\widetilde R+\sum q_i E_i,
\]

the orthogonality equations are Mq=-v. The matrix A=-M is positive
definite with nonpositive off-diagonal entries. To see q>=0, write
q=q_+-q_- with disjoint nonnegative parts. Then

\[
 0\le q_-^t v=q_-^t A q_+-q_-^t A q_-
 \le -q_-^t A q_-.
\]

Positive definiteness forces q_-=0. Thus R^num is an effective rational
divisor. This argument works for arbitrary effective weighted R, not
only a reduced or locally Cartier residual.

Linearity of numerical pullback and agreement with Cartier pullback give

\[
 R^{\mathrm{num}}=bH-m C^{\mathrm{num}},\qquad
 C^{\mathrm{num}}=f^{\mathrm{num}*}C.                     \tag{6}
\]

Both Z-C^num and Z-\widetilde C are exceptional. Since every numerical
pullback is orthogonal to the exceptional curves,

\[
 \begin{aligned}
 0\le L\cdot R^{\mathrm{num}}
 &=(3H-Z)\cdot(bH-m C^{\mathrm{num}})\\
 &=b(3a-4)-m(12-c_S^2).                                  \tag{7}
 \end{aligned}
\]

This is where retaining the numerical pullback, rather than an
unjustified Cartier divisor 3H-C on S, is essential.

Finally H is nef and big, H^2=a, and H·C^num=4. Hodge index on the
smooth X gives

\[
 (C^{\mathrm{num}}-\tfrac4aH)^2=c_S^2-\tfrac{16}{a}\le0.
\]

Since C is nonplanar, a>=2, so c_S^2<=8<12. Division in (7) is therefore
legitimate, proving (2). Substitute deg R=ab-4m to obtain (3) and use
integrality for (4). No exceptional component in this proof is asserted
to be an additional residual curve downstairs. ∎

The dimensionless version makes the role of carrier geometry transparent:
with Gamma_S(C)=16/a-c_S^2,

\[
 \frac{\deg R}{ab}\ge
 \frac{\Gamma_S(C)}{12-c_S^2}.                            \tag{8}
\]

This measures how a supporting-nef constraint converts a Hodge gap into
residual capacity. A vanishing gap is a potential endpoint that this
inequality leaves available, rather than a contradiction.

## 3. Explicit correction on the prescribed A-type carriers

Consider the actual carriers from the [prescribed-singularity
construction](prescribed_singular_carriers.md), independently
reviewed in its [audit](prescribed_singular_carriers.md). Assume S is
smooth along C except at one marked point with completed pair

\[
 S:\ ty-z^r=0,\qquad C=(y,z),\qquad r>=2.                 \tag{9}
\]

Singularities away from C do not contribute to the following calculation.
On the minimal resolution of this A_(r-1) point the strict C meets one
end of the chain transversely. The exceptional matrix has -2 on its
diagonal and 1 between neighbors. Its numerical pullback coefficients,
oriented from the end met by C, are (r-i)/r for 1<=i<r. The correction
to strict self-intersection is therefore (r-1)/r.

The resolution is crepant near C. Since K_S=(a-4)H and C is rational,
adjunction gives \widetilde C^2=14-4a. Consequently

\[
 \boxed{c_S^2=14-4a+\frac{r-1}{r}
              =15-4a-\frac1r.}                          \tag{10}
\]

For **every** actual proper mate on this fixed carrier, not just the
sufficiently-high-degree examples constructed earlier, (2)–(3) become

\[
 m\le\frac{b(3a-4)}{4a-3+1/r},
\qquad
 \boxed{\deg R\ge
 b\,\frac{4a^2-15a+16+a/r}{4a-3+1/r}.}                  \tag{11}
\]

For a>=4 there is even the coarse uniform consequence

\[
 \deg R\ge\frac5{13}ab>\frac13ab.                       \tag{12}
\]

Indeed increasing r only decreases the denominator in the multiplicity
fraction, and

\[
 \frac8{13}-\frac{4(3a-4)}{a(4a-3)}
 =\frac{4(a-4)(8a-13)}{13a(4a-3)}\ge0.
\]

Formula (12) is a convenient comparison, not an optimality claim: r and
a cannot be varied independently in arbitrary low-degree surfaces, and
the existence proof supplies a sufficiently large a depending on r.
The precise formula (11), with its integer refinement, is preferable
when a carrier is specified. Arbitrarily large local index by itself
does not remove residual capacity in this marked end-curve family.

If instead C meets finitely many disjoint A_(r_i-1) singularities, each
transversely at an end of its resolution chain, and S is smooth at the
other points of C, the corrections add. Put

\[
 \kappa=\sum_i(1-1/r_i).
\]

Then

\[
 c_S^2=14-4a+\kappa,\qquad
 m\le\frac{b(3a-4)}{4a-2-\kappa},                         \tag{13}
\]

and

\[
 \deg R\ge
 b\,\frac{16-a(14-4a+\kappa)}{4a-2-\kappa}.              \tag{14}
\]

For any actual such carrier Hodge index ensures the denominator is
positive and
\(\kappa\le4a-14+16/a\). A strictly smaller correction gives a positive
bound. No numerical choice of indices or correction is claimed to have
been globally realized in a degree where other surface constraints
would prevent it.

## 4. What must replace a naive index-only correction

The preceding coefficient 1-1/r uses the **marked end-curve**, not only
the index. For a smooth curve meeting the i-th exceptional curve of an
A_(r-1) resolution transversely, the inverse Cartan matrix instead gives

\[
 \kappa_i=\frac{i(r-i)}r,
 \qquad\operatorname{index}(C)=\frac r{\gcd(r,i)}.         \tag{15}
\]

Concrete local models are

\[
 xy=z^r,\qquad C_i=(x-z^{r-i},\ y-z^i).
\]

These are smooth curves parametrized by z. The inverse matrix formula
\(A^{-1}_{ij}=\min(i,j)(r-\max(i,j))/r\) verifies (15).
For prime r all these curves have the same local index r, while their
corrections range from (r-1)/r to floor(r^2/4)/r. For example r=13 gives
corrections 12/13 and 42/13 at positions 1 and 6, both with index 13.

This falsifies replacing every singular point of index r by the
end-curve correction 1-1/r. It is a local marked control; it is **not**
an example contradicting a positive residual fraction for the fixed
global quartic. Such a contradiction would require actual global
carriers and mates that are not supplied here.

More generally the required intrinsic correction is computable from a
resolution with smooth strict C. Write M=(E_i·E_j),
v_i=\widetilde C·E_i, and

\[
 K_X=f^*K_S+\sum\alpha_i E_i.
\]

Adjunction and numerical orthogonality give

\[
 c_S^2=14-4a+\delta_{S,C},\qquad
 \boxed{\delta_{S,C}=-\alpha^t v-v^tM^{-1}v.}             \tag{16}
\]

Thus the bound can equivalently be written

\[
 \deg R\ge
 b\,\frac{16-a(14-4a+\delta_{S,C})}{4a-2-\delta_{S,C}}.  \tag{17}
\]

This numerical adjunction correction retains discrepancies and the
marked resolution contacts. It is not the filtered comparison module
Delta, the equation-module torsion, or a full-primary attachment
length. The proof of the bound needs none of those identifications.

## 5. General smooth-curve version and controls

The same argument is not specific to the quartic. Let C be a smooth
integral degree-c curve with I_C(delta) globally generated, lying on a
normal integral degree-a hypersurface. For an actual proper mate of
degree b and generic multiplicity m, let c_S^2 denote its Mumford
self-intersection. If delta*c-c_S^2>0, then

\[
 \begin{aligned}
 0&\le b(\delta a-c)-m(\delta c-c_S^2),\\
 \boxed{\deg R}&\boxed{\ \ge
 \frac{b(c^2-a c_S^2)}{\delta c-c_S^2}.}                  \tag{18}
 \end{aligned}
\]

Hodge index gives the nonnegative numerator. The proof is exactly the
principalized ideal construction with L=delta*H-Z. No Q-Cartier
hypothesis is introduced. If the denominator is zero, this divided
formula is unavailable; one must retain the undivided nef inequality.

There are two useful consistency controls:

* On a carrier smooth along the fixed quartic, c_S^2=14-4a and (3)
  recovers exactly the earlier smooth-carrier multiplicity inequality.
  The known quadric pair (q,A^n) has cycle nC+2n*ell and degree
  residual=ab/3, giving the inherited sharp control within that scope.
* For the **different curve** given by the twisted cubic on its normal
  quadric cone, the [reviewed classical
  benchmark](global_equations_and_constructions.md) has an actual
  (2,3) pair with cycle 2T and no residual. Here c=3, delta=2,
  a=2, c_S^2=9/2, so (18) correctly gives zero. The normal-carrier
  inequality is compatible with an actual characteristic-zero
  sole-support construction. This supplies no fixed-quartic example.

In particular this work proves positive lower bounds in geometric
families where the Hodge gap can be computed or bounded below. It
does not prove a strictly positive fraction for every normal quartic
carrier, much less every nonnormal or generically singular carrier.



## Nonnormal carriers: one inverse curve and multiple branches

Let S be integral with finite normalization, exactly one divisorial inverse curve Gamma above C (isolated inverse points are allowed), residue degree f=[k(Gamma):k(C)], ideal valuation e=ord_Gamma(I_C), and numerical square sigma=(Gamma^num)^2. No Q-Cartier assumption on Gamma is imposed.

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

the normal-carrier bound. If \(S\) is smooth along \(C\),
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

The inherited [numerical-pullback versus normal-sheaf theorem](numerical_surface_pullback.md),
with its [independent audit](numerical_surface_pullback.md),
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
[graph source, §7](blowup_residual_geometry.md#supporting-nef-bounds-exact-slack-and-equality-controls), gives

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




## Interpretation

The numerical residual is effective even without a Q-Cartier hypothesis. A positive Hodge gap bounds genuine residual degree; a zero gap leaves an endpoint open and supplies no conductor descent or actual mate. Several inverse branches require their valuation vector, not a singleton formula. The first-normal gcd bound is useful but may be weaker than an exact numerical square or the graph slope refinement in [the two-blowup account](blowup_residual_geometry.md).


## Characteristic reach and limitation

The smooth-carrier inequality uses no normal-bundle splitting: its degree
14, Cartier intersection and global generation proofs work in arbitrary
characteristic. Its one-third residual floor therefore persists under the
stated smooth-along-C hypothesis. The normalization proofs use a smooth
principalization, effectivity of numerical pullback and algebraic Hodge index;
the same deductions hold in any characteristic where those stated inputs are
provided. The source applications and general resolution setup here were
reviewed in characteristic zero. The first-normal gcd formulas use the
balanced conormal splitting, valid away from characteristic two; characteristic
two has splitting O(-8)+O(-6), so its gcd-degree formulas need recomputation.
A [positive-characteristic quartic-carrier STCI](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
is consistent: its fixed singular carrier does not satisfy the smooth-along-C
hypothesis, and a zero Hodge gap is not excluded.


## Intersection-theoretic literature input

[Mumford, sections I–II](https://www.numdam.org/item/10.1007/BF02698717.pdf), freshly inspected here, supplies negative definiteness of the exceptional intersection matrix and numerical intersection on a resolution. The effectivity sign argument needed for residual capacity is written out above; no Q-Cartier shortcut is used. The algebraic Hodge-index input is applied on the smooth projective resolution. The separate comparison of the numerical square with the actual normal line is proved in [numerical surface pullback](numerical_surface_pullback.md), with its generically regular integral-carrier hypotheses retained.
