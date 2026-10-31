# Horizontal blowup paths: resultants, bundles, and missing higher jets

Let C be a smooth integral curve of degree d in projective three-space,
and let an actual proper pair F_a,G_b have sole reduced support C. Write
p,q for its generic normal orders and m=ab/d for its transverse length.
The general [contact-depth theorem](generic_contact_depth.md) retains the
whole common infinitely-near tree. Here a much narrower path has additional
global line-bundle data. These are provisional deductions, not an unrestricted
STCI obstruction.

## A single common section and the second resultant

Blow up C in the ambient threefold, obtaining X_1 with exceptional E.
Use the quotient convention E=P(nu), nu=N^*_(C/P3), so O_E(1)=O_X1(-E)|E.
Assume the intersection of the two strict surfaces has just one reduced
curve component Gamma, that Gamma is a smooth section over C, and that
there are no other curve components, including vertical exceptional curves.
The section corresponds to a quotient nu→T, with T=O_E(1)|Gamma.

Let r,s be the generic normal orders of the strict surfaces along Gamma,
and suppose their generic first normal forms are coprime. The strict
surfaces form a regular-sequence CI, since they have no common surface
component. Under the sole-smooth-Gamma support hypothesis, generic
coprimality automatically holds fiberwise, as proved below. Plane-curve
multiplicity sequences give 1≤r≤p and 1≤s≤q: restriction of a strict
equation to the first exceptional line has a root of multiplicity at most
the degree p or q of its original tangent form.

Noether's generic local blowup formula gives
\[
m=pq+rs,\qquad ab=d(pq+rs).
\]
There are no other generic normal directions, and the coprime forms at the
second center have length rs.

## Automatic fiberwise coprimality for the retained full support

The nowhere-zero condition follows from generic coprimality under the stronger
support hypothesis already imposed here. At a closed P of Gamma, complete
smooth ambient coordinates as k[[t,x,y]], with Gamma=(x,y) and t a parameter
on Gamma. The strict equations form a regular sequence. Their CI algebra B=k[[t,x,y]]/(F_1,G_1) is finite over
k[[t]], because its radical is (x,y). It is Cohen–Macaulay of dimension
one with that sole minimal prime, so t is a nonzerodivisor. Thus B is finite
free over k[[t]]. Its rank is its generic length rs, computed from the
coprime generic normal forms.

The powers of the regular prime (x,y) are primary, so generic normal order
r of F_1 implies F_1 belongs to (x,y)^r at P; similarly G_1 belongs to
(x,y)^s. After setting t=0, their orders are at least r,s. Neither specialized equation is zero: otherwise the fiber would have infinite colength, contradicting freeness. Their plane
intersection has length rs by freeness. The local inequality
length≥ord(F_1|t=0)ord(G_1|t=0)≥rs therefore has equality throughout.
Both orders are exactly r,s and their initial forms are coprime. This holds
at every P, so the resultant is nowhere zero.

Hence the original single-section, no-other-curve CI hypothesis plus
generic coprimality suffices for the line-bundle identity; no extra uniform
transversality assumption is needed. This is a chosen-generator CI argument,
not a claim that an arbitrary full generic initial CI forces normal flatness.
The later defect-divisor variant applies once the sole-smooth-support or
finite-flat/minimal-length hypotheses are relaxed.


The strict equations restrict to line bundles
\[
M_F=O_C(a)T^p,\qquad M_G=O_C(b)T^q.
\]
Put K=ker(nu→T). The normal sequence of Gamma in E⊂X_1 gives
\[
N_{\Gamma/E}=K^*T=T^2(\det\nu)^{-1},\qquad
N_{E/X_1}|_\Gamma=T^{-1},
\]
so
\[
\det N^*_{\Gamma/X_1}=(\det\nu)T^{-1}.
\]

For clarity, the binary resultant fact used here is intrinsic. If V is a
rank-two conormal bundle and homogeneous equations of orders r,s are
sections of Sym^r(V)⊗M and Sym^s(V)⊗N, their resultant is a section of
\[
(\det V)^{rs}M^sN^r.
\]
The determinant of the Sylvester map has degree s in the coefficients of
the first form and r in those of the second; changing the conormal frame
multiplies it by det(frame)^(rs). This proves the transition law and the
line bundle. Its value vanishes exactly when the two binary forms share a
projective root over the residue field's algebraic closure. Thus fiberwise
coprimality makes this line bundle trivial, not merely generically trivial.

Apply this with V=N^*_(Gamma/X1). With
lambda=ps+qr-rs≥rs>0, the resulting triviality is
\[
(\det\nu)^{rs}O_C(as+br)T^{\lambda}=O_C.
\]
The determinant normal sequence in projective space gives
\(\det\nu=\omega_C^{-1}O_C(-4)\). Consequently
\[
\boxed{T^{ps+qr-rs}=\omega_C^{rs}O_C(4rs-as-br).}
\]
This is an equality of line bundles on the actual marked curve, conditional
on the full global hypotheses above.

## The effective resultant correction

If the sole-smooth-support/finite-flat hypothesis is relaxed and only generic
coprimality is known, the resultant of the two leading forms may have
a nonzero effective zero divisor D_res. The same transition calculation gives
\[
\boxed{T^{ps+qr-rs}=\omega_C^{rs}O_C(4rs-as-br)(D_{\rm res}).}
\]
The generic equality m=pq+rs still requires Gamma to be the only generic
common direction; additional horizontal directions add their own local lengths. The exact trivial-resultant argument and its numerical
exclusion cannot be reused after discarding D_res. In particular, sole
support before the first blowup does not assert absence of vertical
exceptional components on a later model.

## The fixed quartic: a restricted two-level exclusion

For C=C0 on its smooth quadric, component exclusion and effectivity give
a≥3p and b≥3q for any hypothetical sole-support pair. Therefore
\[
m=ab/4\ge9pq/4>2pq.
\]
But a one-section path becoming generically transverse at the next center
has m=pq+rs≤2pq, since r≤p and s≤q. This is already a contradiction,
with **no** normal-bundle splitting or fiberwise-resultant hypothesis.
In fact the [generic depth theorem](generic_contact_depth.md) excludes every
contact tree of depth at most one, even with several geometric directions;
closed-point vertical components do not change that generic argument.
This simpler degree-budget proof works in every characteristic.

The conormal identity yields a second, more geometric proof under its
stronger global hypotheses, and remains useful for other curves where the
simple degree budget leaves a two-level path available. The [conormal
splitting](../results/quartic_conormal_characteristic_jump.md) is
O(-7)^2 away from characteristic two and O(-8)⊕O(-6) in characteristic two.
Hence every quotient line T has deg T≥-alpha, where alpha=7 or 8 respectively.
For a section path satisfying the **nowhere-zero second-resultant** hypotheses,
taking degrees above gives
\[
(ps+qr-rs)\deg T=14rs-4(as+br)
\le14rs-12(ps+qr).
\]
It would follow that
\[
(12-\alpha)(ps+qr)\le(14-\alpha)rs.
\]
But ps+qr≥2rs; since alpha<10, twice the left coefficient is larger
than the right coefficient. This is impossible.

Thus the conormal calculation also excludes that narrower globally
transverse section stratum in every characteristic, using the indicated
characteristic-dependent bound. The characteristic-zero calculation is
retained as a distinct geometric argument, not as a prerequisite for the
stronger elementary depth exclusion above. Neither proof
contradicts the [quartic-carrier supported pairs in every positive
characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier):
those pairs must avoid these precise section/transversality hypotheses.
Several directions, multisections, ramification, further contact, vertical
exceptional components and a nonzero resultant defect are distinct escape
interfaces. No exhaustion or actual realization of those alternatives is
claimed.

## Exact bundle bookkeeping along a chosen horizontal path

Let X_i be a smooth threefold, C_i a smooth section, and N_i=N_(C_i/X_i).
Choose a line subbundle K_i⊂N_i giving the next exceptional section, and
write L_i=N_i/K_i. The exceptional normal sequence after blowing up C_i is
\[
0\longrightarrow K_i^*L_i\longrightarrow N_{i+1}
\longrightarrow K_i\longrightarrow0.
\]
Indeed the first term is the relative tangent of the ruled surface along
the section, and the last term is the exceptional divisor's normal line,
O_E(-1)|C_(i+1)=K_i. This proves the exact sequence, without assuming
that it splits.

For a hypersurface of normal multiplicity m_i at C_i, put
M_i^F=O_Xi(F_i)|C_i. Strict transformation gives
\[
F_{i+1}=\pi_i^*F_i-m_iE_i,\qquad
M_{i+1}^F=M_i^F K_i^{-m_i}.
\]
Therefore, along an already specified path and multiplicity sequence,
\[
\deg M_h^F=\deg M_0^F-\sum_{i<h}m_i\deg K_i,\qquad
\deg N_h=\deg N_0-\sum_{i<h}\deg K_i.
\]
The conormal quotient T in the first section corresponds to K_0^{-1};
the two conventions agree after this identification.

## Why tangent data cannot determine the next multiplicity

At the generic point, let p≥2 and consider
\[
f_r=y^p+x^{p+r},\qquad r\ge1.
\]
All these germs have order p, initial form y^p and the same p-fold tangent
root y=0. In that blowup chart y=xv their strict equations are
\[
v^p+x^r,
\]
with next multiplicity min(p,r). Every value from one through p is possible
without changing the initial tangent form. This exact example works in any
characteristic, with scheme multiplicities retained; reducedness is not
being assumed.

Thus the chosen section, its tangent-root multiplicity and the bundle
recurrences do not determine the next state. A useful continuation must
also retain sufficient compatible higher-jet or Rees/proximity data. Newton
information with global coefficient bundles is a possible representation,
provided it retains every cancellation needed at the next stage; a bare
Newton polygon is not asserted equivalent to the full filtered ideal.
The [finite normal-jet theorem](finite_normal_jets.md) supplies an exact
cutoff at fixed degrees; it supersedes the archive's blanket claim that no
finite cutoff is justified. It supplies no cutoff uniform in unbounded
degrees and no automatic homogeneous realization of a local path.

## Review and unresolved scope

Independent consolidation review accepted the resultant transition calculation,
the finite-flat generic-to-fiberwise bridge, the effective-divisor variant,
the bundle recurrences, the higher-jet counterexample and the simpler
all-characteristic quartic depth exclusion. These are reviewed provisional
mathematical statements without a new canonical ID. A ramified multisection
formula, a general higher-depth upper bound and actual global realization of
a surviving contact path remain outside this account. No computation is
required for these proofs and none was rerun.
