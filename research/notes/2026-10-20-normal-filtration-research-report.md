# Independent continuation: homogeneous generators, defect divisors, and actual carriers

Investigation begun 2026-10-19; closing report 2026-10-20.
Starting main commit: `84dacd99c54915b1bbb224bb01565f01716445de`.
Research branch: `codex/normal-filtration-results-2026-10-19`.

**Status: new mathematical proposals with recorded independent review,
not canonical promotions. The unrestricted characteristic-zero STCI
question for the fixed rational quartic remains open.**

## 1. Exact scope and inherited authority

Throughout the principal applications, the field is algebraically closed
of characteristic zero and

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad N_{C_0/\mathbf P^3}=\mathcal O_{\mathbf P^1}(7)^2.
\]

The investigation followed the repository retrieval protocol and read
the provisional formal-normal synthesis. Promoted
[STCI-R-0001](../results/quartic_carrier_exclusion.md),
[STCI-R-0008](../results/spectral_root_picard_criterion.md),
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md), and
[STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
were used as established premises with their literal hypotheses. In
particular, R0010 and R0011 are **inherited results**, not discoveries of
this continuation. No accepted quartic proof or certificate was rerun.

The main actual-STCI result below assumes that the **full** generic
ordinary normal initial ideal is a coprime binary complete intersection
of degrees `2<=r<s`, and that its actual first relation kernel is a line
subbundle. These assumptions do not hold automatically for arbitrary
STCI equations. A separate contribution records exactly what changes
when the first relation is nonsaturated.

The generator-filtration interface, local planar Hilbert-function
lemma, and first-blowup balance have independently reviewed source
evidence but no separate promoted result ID. The source notes and
audits below state these authority gaps and reconstruct each new use.
No canonical result, question, state, or frontier record is modified.

## 2. Main finding A: actual homogeneous generators force small-movement rigidity

Suppose

\[
Y=V(F_a,G_b),\qquad Y_{\rm red}=C_0,
\]

has the full generic initial-CI and saturated-first-line hypotheses
above. Write `I=I_C0`, `J=I O_Y`, and

\[
R=\ker(\operatorname{Sym}^r N_C^*\to J^r/J^{r+1})
 =\mathcal O(-7r-\epsilon),\qquad\epsilon\ge0.
\]

The associated full root has bidegree `(epsilon,r)` in
`P1_base x P1_direction`. Movement means this integer epsilon; it is
not the degree of either defining equation.

### A1. A nonsplit actual-generator sequence

R0010 gives a uniform graded CI. Its second minimal **quotient** relation
is a line `T` of degree `-7s+s*epsilon/r`. Applying the actual generator
filtration gives

\[
0\longrightarrow T\longrightarrow
\mathcal O(-4a)\oplus\mathcal O(-4b)
\longrightarrow R\longrightarrow0,
\tag{1}
\]

and

\[
ab=4rs,\qquad
4(a+b)=7(r+s)-\frac{\epsilon(s-r)}r,
\qquad r\mid\epsilon s.
\tag{2}
\]

Sequence (1) cannot split. Splitting would imply

\[
16ab=(7r+\epsilon)(7s-s\epsilon/r)
=rs\bigl(49-(\epsilon/r)^2\bigr)\le49rs,
\]

contradicting `16ab=64rs`. Consequently both original equations have
exact generic normal order r, and their degree-r symbols jointly
generate R at every point. This supplies auxiliary original-equation
hypotheses that were previously separate in the smooth-root bridge.
It does not construct a global polynomial lift of T.

Neither equation can have the unique containing quadric as a factor:
its intersection with a mate would require a divisor of class `(b,b)`
on that quadric to be supported on the `(1,3)` curve. Restriction to
the quadric therefore gives `a,b>=3r`, including for reducible or
nonreduced equations. With `t=s/r`, these facts imply

\[
t>\rho=\frac{79+16\sqrt{15}}{49}>\frac{23}{8},
\qquad
(5r-3\epsilon)t\le15r-3\epsilon
\tag{3}
\]

when epsilon is positive, as well as `epsilon*t` integral.

### A2. Movement one is excluded in every equation degree

If `epsilon=1`, integrality makes t an integer. Equation (3) and
`r>=2` give `3<=t<4`, so `s=3r`. Equation (2) then reads

\[
4(a+b)=28r-2,
\]

which is impossible for integer a,b. Thus **no actual STCI in the
specified saturated/full-generic-CI class has movement one**, uniformly
in all equation degrees and normal orders.

### A3. Movement two has exactly six necessary numerical possibilities

For `epsilon=2`, the only possible unordered numerical data are:

| r | s | a | b | gap s-r |
|---:|---:|---:|---:|---:|
| 2 | 8 | 8 | 8 | 6 |
| 2 | 12 | 6 | 16 | 10 |
| 6 | 21 | 18 | 28 | 15 |
| 14 | 42 | 48 | 49 | 28 |
| 15 | 45 | 50 | 54 | 30 |
| 20 | 60 | 64 | 75 | 40 |

This is an exhaustive necessary list, not six constructions and not a
completed exclusion. For `r>=7`, (3) forces `s=3r`. The remaining
discriminant condition factors as

\[
(r-7-d)(r-7+d)=48,
\]

giving exactly `r=14,15,20`. The finitely many `r<=6` strata give the
other three rows. This divisor argument proves exhaustion without a
bounded search. R0011 additionally makes each surviving full root
reduced, while singular integral and two-component roots remain.

### A4. Finiteness for every fixed movement from one through eight

For each `1<=epsilon<=8`, the lattice `epsilon*t` integral and (3)
force `t>=3`. Once

\[
r>3\epsilon(2\epsilon+1)/5,
\]

they force `t=3`. The discriminant then factors into a fixed nonzero
integer. For the remaining small r, put `c=7r-epsilon>0`; the exact
factorization

\[
(ca-16r^2)(cb-16r^2)=4r^2(15r^2+\epsilon^2)
\tag{4}
\]

retains all signed divisor pairs and proves finiteness even when the
denominator `5r-3epsilon` is nonpositive. The exact enumeration of this
necessary arithmetic system has respectively
`0,6,4,11,9,19,9,19` unordered candidates for epsilon `1,...,8`.
These counts do not test Picard descent or ambient realizability.
No finiteness theorem for epsilon at least nine is claimed here.

Proofs: [homogeneous generator and arithmetic note](2026-10-19-global-ci-filtration-investigation.md).
Independent reconstruction: [core audit](2026-10-19-numerical-first-root-independent-audit.md)
and [fixed-movement audit](2026-10-19-global-ci-filtration-independent-audit.md).
Exact finite divisor implementation:
[arithmetic verifier](../computations/global_ci_small_movement_divisor_audit.py).

## 3. Main finding B: a nonsaturated first relation has an effective resultant budget

This contribution works for a smooth projective curve in any smooth
threefold, with any rank-two conormal E. Let Y be an actual lci
thickening with unique reduced support C and full generic initial CI
of degrees `2<=r<s`. Saturate its actual first kernel:

\[
K_r=R(-D),\qquad\delta=\operatorname{length}D,
\qquad g=s-r.
\]

Let `P_i` be the saturation of `J^i`, `B_i=P_i/P_(i+1)`, and
`S=Ann_Y J`. Before the second relation, set

\[
A_j=\operatorname{Sym}^j E/
 (R\operatorname{Sym}^{j-r}E),\qquad
c_j=\operatorname{length}\operatorname{coker}(A_j\to B_j).
\]

At degree s use the same map and its line kernel T; its cokernel
again has finite length `c_s`. Saturated Gorenstein duality yields,
with `h=deg E`, `u=deg R`, `ell=deg S`, and `c=c_(s-1)`,

\[
r\ell=r(s-1)h-(s-r)u+c,
\]

\[
\deg T=sh-\frac{s}{r}u-\frac{r-1}{r}c+c_s.
\]

The quotient resultant is a generically nonzero section of
`(det E)^(rs) R^(-s) T^(-r)`. Its effective divisor Delta satisfies
the exact identity and upper bound

\[
\boxed{\deg\Delta=(r-1)c_{s-1}-r c_s},\qquad
0\le\deg\Delta\le(r-1)\binom{s-r}{2}\delta.
\tag{5}
\]

Delta is supported where the actual first relation fails saturation.
The support assertion uses the separately reviewed local exact-order
normal-flatness lemma. The degree identity itself follows directly
from duality and the resultant weights. In this setting
`c_(s-1)=0` is equivalent to ordinary normal flatness.

On a rational balanced base, the second relation gives a section of
`O_Z(-n,s)` on the full root, with zero length `deg Delta`. If the root
is moving and nonreduced, R0011's doubled-divisor argument forces
`deg Delta>=2`. For a moving pure power with root class `(epsilon,r)`,
the stronger inequality is

\[
\deg\Delta\ge(r-1)\epsilon,
\qquad
\delta\ge\left\lceil
\frac{\epsilon}{\binom{s-r}{2}}\right\rceil
\quad(s-r\ge2).
\tag{6}
\]

These are necessary payments for degeneration. They do not assert
that the paid-for configuration exists or lifts globally.

There is also an exact local threshold: gaps `s-r<=2` force normal
flatness automatically, without a first-saturation assumption. Every
special transverse planar CI has first order q with
`r<=q<=floor(sqrt(rs))`; for those gaps this forces q=r, allowing the
reviewed local normal-flatness lemma. The threshold is sharp: the
actual local lci

\[
k[[t,x,y]]/(txy+x^3+y^4,\;xy^2)
\]

has generic full initial CI `(xy,x^5-ty^5)` of degrees `(2,5)`, but
actual first relation `txy` with defect length one. Its support is the
smooth t-axis. It is a local counterexample, not a projective C0 pair.

Proof and full-root component accounting:
[effective-defect note](2026-10-19-first-relation-defect-investigation.md).
Independent reconstruction:
[defect audit](2026-10-19-first-relation-defect-independent-audit.md).

## 4. Main finding C: actual full-singleton plane carriers can fail first-order descent

Define

\[
f:\mathbf P^2_{s:t:z}\to\mathbf P^3,
\qquad
f=[s^4:s^3t:st^3+z^4:t^4+s^3z].
\tag{7}
\]

This is a finite birational normalization of the integral degree-sixteen
surface

\[
(X_0^3X_3-X_1^4)^4-X_0^{13}(X_0^2X_2-X_1^3)=0.
\]

The line `z=0` maps isomorphically to literal C0, and the full reduced
inverse support of C0 is exactly that line, including at infinity.
Thus this is an actual realization of the full-singleton plane model
in R0002 **before** the mate condition. There are no isolated extra
inverse points.

It has no mate of any positive degree. A hypothetical degree-b mate
pulls back to `lambda z^(4b)`. After rescaling, restriction to `s=0`
forces `G(0,0,Z,T)=Z^b`; differentiating in s there then gives the
impossible polynomial identity

\[
0=b\,t^3z^{4b-4}.
\]

The same proof excludes the entire eleven-parameter family

\[
[s^4:s^3t:st^3+\alpha z^4:t^4+zP_3(s,t,z)],
\quad\alpha\ne0.
\tag{8}
\]

Every member has full inverse support exactly `z=0`. Write
`P_3=A_3(s,t)+zB_2(s,t)+z^2C_1(s,t)+eta z^3`. The map is birational
exactly when `A_3` or `C_1` is nonzero. This nonempty open locus consists
of actual degree-sixteen normalization carriers excluded in all mate
degrees. The other members have map degrees two or four; they are not
additional plane normalizations.

More generally, the proof excludes every basepoint-free full-singleton
projection with the literal first two coordinates `s^4,s^3t` and literal
C0 restriction. The support condition forces the boundary third
coordinate to be `alpha z^4`. Its first transverse derivative retains
a nonzero `t^3` term, giving the same all-degree contradiction. This
coordinate sublane is restrictive and is not asserted to contain all
plane-model projections.

A reusable differential lemma explains the mechanism. If a candidate
Cartier-ray section q on a normalization is nonzero at a smooth point
outside the curve and `dq` is nonzero on a vector in `ker dnu`, no
positive power of q can descend in characteristic zero. In (7), a
first-order calculation at the generic conductor line detects exactly
such an obstruction. Its reduced residue class is already trivial;
the first nilpotent term obstructs every power. This demonstrates why
reduced phase or inverse-support checks alone cannot settle Q0001.

Proof: [singleton-projection note](2026-10-19-singleton-projection-investigation.md).
Independent review, including a closing reconstruction of the broader
coordinate sublane:
[carrier audit](2026-10-19-singleton-plane-projection-independent-audit.md).
The full plane-model projection/descent question remains open.

## 5. Main finding D: a reduced singular movement-two root requires a singular formal surface

Let Z be any reduced finite-flat root divisor of class `(2,r)`, `r>=2`,
on the actual exceptional surface. There is **no all-orders embedded
Cartier lift whose formal surface is regular along all of Z**.
This extends the smooth-root argument to a singular root under an
explicit hypothesis on its lifted surface.

The key new calculation is for `N=O_Z(7,-1)`:

\[
p_*N=\mathcal O_{\mathbf P^1}(5)^r.
\]

Thus N is globally generated and `H^1(Z,N)=0`, including at singular
points and with all component gluing retained. Positivity on every
component allows Bost's singular-lci-center algebraization criterion.
Regularity preserves the selected branch under normalization, giving
a smooth projective surface T containing the original Z. The normal
vanishing and generation then smooth Z **inside T**, preserving
`Z^2=7r-2`, genus `r-1`, and `H.Z=4r`. Applying the accepted ruled-model
argument to that smooth deformation yields `deg S<=r+2`, while the
original Z still forces surface multiplicity at least r along C0 and
the incompatible plane bound
`(deg S-1)(deg S-2)>=4r(r-1)`.

The new use of algebraization was checked against
[Bost, Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=28),
which permits a proper connected lci scheme of definition. The embedded
deformation step uses the singular-lci scope of
[Hartshorne's deformation lectures, Theorems 6.3 and 9.3](https://math.berkeley.edu/~robin/math274root.pdf).
The audits preserve the separate branch-normalization and smoothing
steps rather than assuming that a singular root is smooth.

At a singular point write a lift equation `f_Z+u h_1+...`. Every
surviving all-orders lift must have some singular root point where
`h_1=0`, so the lifted formal surface is singular there. The local
examples `xy+u^2` and `y^2-x^3+u^2` show that Cartier lifting alone
does not force regularity. No singular-root actual-CI bridge, finite
jet cutoff, or actual STCI exclusion follows without additional work.

Proof: [singular-root note](2026-10-19-singular-root-investigation.md).
Independent review:
[smoothing audit](2026-10-19-regular-singular-root-smoothing-audit.md),
with a separate elementary argument for two equal-slope rational
components in [the two-component audit](2026-10-19-regular-reducible-root-independent-audit.md).

## 6. Main finding E: generic Rees data cannot replace the defect sheaves

For any codimension-two lci curve thickening Y in a smooth threefold,
every exceptional prime divisor on the normalized blowup of the full
ideal `I_Y` dominates a support curve. There is no divisorial Rees
valuation centered at a closed point of that curve: before normalization
the exceptional divisor is `P_Y(I_Y/I_Y^2)`, and its point fibers have
dimension one; finite normalization cannot turn them into divisors.
The Rees coefficients and generic residue degrees satisfy

\[
\sum_i a_i f_i=\operatorname{length}(\mathcal O_{Y,\eta_C}).
\]

Nevertheless intrinsic first-relation defects are unbounded with fixed
generic filtered algebra. In

\[
J_N=(u^b,v^a+t^Nu^p),\qquad a,b>p\ge2,
\]

the first actual relation is `t^N u^p`, its saturation is `u^p`, and
the defect length is exactly N. On `N=aL`, the generic filtered
algebras are isomorphic by scaling v. Taking `b=2p` fixes the generic
coprime-CI initial ideal `(u^p,v^(2a))`; taking `b=p+1` fixes the
three-generator non-CI initial ideal `(u^p,uv^a,v^(2a))`.
The latter has two graded socle generators although the actual local
algebra is Gorenstein. These explicit shields prevent transferring
graded one-socle duality to arbitrary tangent algebras.

The family is affine and imposes no fixed global projective degree.
It does not disprove a global defect bound for C0. It shows why such
a bound must retain defect sheaves or special-fiber geometry of the
normalized exceptional surfaces, rather than only generic divisorial
data or ordinary Segre numbers.

Proof: [Rees and intrinsic-defect note](2026-10-19-rees-residual-investigation.md).
Independent reconstruction: [Rees audit](2026-10-19-rees-residual-independent-audit.md).

## 7. Recommended continuation and exact remaining obstacles

The highest immediate leverage is now in the six movement-two numerical
rows, rather than an unbounded degree search within that saturated
class. For each row, the necessary full-root Picard relation and its
finite ambient jets must be tested together. The existing smooth-root
all-orders obstruction has a nonexplicit finite cutoff; it cannot be
compared with the six finite gaps without further mathematics.

For the broader generic-CI class, equation (5) isolates a useful target:
bound the actual first defect D and the generation defects `c_j` using
the homogeneous two-generator module and the ambient normal jets.
Generic local or Rees data alone cannot supply that bound, by finding E.
For moving powers, (6) gives a concrete necessary lower payment that
such a global upper bound could contradict.

The non-CI full generic initial-ideal case remains separate. Its
ordinary tangent algebra can have more than one graded socle generator,
so the symmetric saturated-power pairing used here has no automatic
replacement. A dual annihilator filtration is a plausible next object,
but no theorem for it is claimed.

For carrier normalization, the first-order differential obstruction can
be tested on plane projections outside the fixed-coordinate sublane
and on the two degree-eight models. The existence of full singleton
inverse support is now demonstrated in an actual plane family; the
remaining issue is descent, with nilpotent data retained.

For singular formal roots, the precise residual problem is the singular
formal surface. An argument through normalization or resolution must
track its change in root normal degree; applying the regular-branch
formula unchanged would be invalid.

None of these results proves that arbitrary defining surfaces share a
singular point on C0. No vertical exceptional component has been
identified with a residual curve downstairs. The unrestricted fixed-C0
and universal STCI questions remain open.

## 8. Review, provenance, and reproduction

Separate agents reconstructed the principal new proofs, tested omitted
special points and hypotheses, and wrote the linked audit files. The
root investigator also recomputed the arithmetic and the plane-coordinate
support argument. A k=10 arithmetic slip in the core audit was corrected
at closing: the required sum is 19, product 80, and discriminant 41;
the row remains excluded. The correction is recorded in that audit.

Reproduction commands from the research worktree are:

```sh
python3 research/computations/global_ci_small_movement_divisor_audit.py
python3 research/computations/global_ci_small_movement_divisor_audit.py 1 2 --show-tuples
python3 research/computations/validate_records.py
git diff --check
```

The arithmetic script enumerates a proved finite divisor reduction.
It verifies a necessary arithmetic system, not Picard descent, formal
lifting, or STCI existence. Canonical validation and link checks are
integrity checks, not proofs of the new mathematics. Closing checks passed: the exact divisor script produced the stated eight
counts and literal six movement-two rows; canonical validation checked 12
records with zero errors; all 83 local links in the 14 new files resolved;
and `git diff --cached --check` reported no whitespace errors. These
checks do not replace the proof and independent review records.

The final package is isolated from unrelated edits in the original
checkout and contains only this continuation's new source notes,
independent audits, exact arithmetic script, and this report. Proposed
extensions of small-movement finiteness beyond epsilon eight were not
completed or included in the stated results.
