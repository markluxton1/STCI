# Residual-degree capacity on normal carriers

Date: 2026-10-28. Author: `singular_carrier_construction` research agent.
**Status: provisional quantitative deductions, independent review requested;
no canonical promotion.** The result bounds the genuine residual cycle of
an actual proper intersection. It neither presumes nor proves that a
characteristic-zero sole-support intersection is impossible.

## 1. Exact question and relation to earlier work

Fix

\[
 C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_{\mathbf C}.
\]

Let S=V(F_a) be a **normal integral** degree-a surface containing C,
let G_b give a proper intersection, and write its actual cycle as

\[
 [V(F_a,G_b)]=m[C]+R,\qquad C\not\subset\operatorname{Supp}R.
                                                               \tag{1}
\]

Here m is the full generic intersection multiplicity along C. The
residual R is effective, may have weighted or nonreduced components, and
has degree ab-4m. It is not the residual after removing an arbitrary
smaller witness thickening.

The [reviewed smooth-carrier capacity
argument](2026-10-27-absorption-deformation-interface.md), §4, gives
deg R>=ab/3 when an integral carrier is smooth along every point of C.
The present note extends its supporting-nef argument to normal carriers
with isolated on-curve singularities, using an intrinsic intersection
number rather than substituting a local Cartier index for missing
geometry.

Repository checks also located the [October 5 numerical-pullback versus
normal-sheaf comparison](2026-10-05-mumford-normal-bound.md), independently
covered by the [October 6 normal-bound
audit](2026-10-06-normal-bound-independent-audit.md), and the [October 17
extremal-ray synthesis](2026-10-17-generalization-normal-carrier-extremal-ray-synthesis.md).
The latter already names a normal Hodge gap under Q-Cartier hypotheses,
but labels its endpoint sufficiency proof pending independent audit.
We do not rely on that sufficiency assertion, promote it, or rerun its
accepted inputs. The new point here is a **quantitative residual-degree
inequality requiring no Q-Cartier assumption**, together with explicit
marked singularity corrections.

## 2. The normal-carrier residual bound

Use Mumford's numerical self-intersection

\[
 c_S^2=(f^{\mathrm{num}*}C)^2,
\]

computed on any smooth projective resolution f:X→S. Numerical pullback
means strict transform plus the unique rational exceptional divisor
making the result orthogonal to every f-exceptional curve. It is defined
for Weil divisors even when C has no Cartier multiple.

**Proposition.** Under (1),

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
construction](2026-10-28-singular-carrier-construction.md), independently
reviewed in its [audit](2026-10-28-singular-carrier-audit.md). Assume S is
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
  benchmark](2026-10-27-char0-torsion-benchmark-audit.md) has an actual
  (2,3) pair with cycle 2T and no residual. Here c=3, delta=2,
  a=2, c_S^2=9/2, so (18) correctly gives zero. The normal-carrier
  inequality is compatible with an actual characteristic-zero
  sole-support construction. This supplies no fixed-quartic example.

In particular this work proves positive lower bounds in geometric
families where the Hodge gap can be computed or bounded below. It
does not prove a strictly positive fraction for every normal quartic
carrier, much less every nonnormal or generically singular carrier.

## 6. Primary literature, verification, and next use

Freshly inspected on 2026-10-28:

* Mumford, [*The topology of normal singularities of an algebraic
  surface and a criterion for simplicity*, IHES 9 (1961),
  5–22](https://www.numdam.org/item/10.1007/BF02698717.pdf): exceptional
  negative definiteness on printed p. 6 and numerical intersection in
  §II. This is the classical foundation, not a new construction.
* Schröer, [*A higher-dimensional generalization of Mumford's rational
  pullback for Weil divisors*, J. Singularities 19 (2019),
  53–60](https://www.journalofsing.org/volume19/schroer.pdf), introduction
  and §1, explicitly records linearity, effectivity and the projection
  formula for normal surfaces. We use only that surface theory.
* Langer, [*Bridgeland stability conditions on normal surfaces*,
  Annali di Matematica 203 (2024),
  2653–2664](https://doi.org/10.1007/s10231-024-01460-0), §§2.1–2.2:
  numerical pullback, effectivity via the exceptional matrix, and Hodge
  index on the normal surface are stated with their proper scope.
  The derived-category results of that paper are not inputs here.

All displayed inequalities rest on the proofs above, not finite
sampling. An independent reviewer should check effectivity of the
numerical residual, principalization and exceptional orthogonality,
the sign of each division, the inverse-Cartan correction in (10) and
(15), and the absence of a fixed-quartic universal-positive inference.

The practical next use is to compute or constrain the marked correction
delta_(S,C), or equivalently the normal Hodge gap, for an actual carrier
family. This produces a quantitative lower bound on genuine residual
degree. If the gap approaches zero, that is a precise instruction to
inspect the global divisor-class and equation data near that potential
construction boundary; it is not a reason to discard the family.
