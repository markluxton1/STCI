# Historical mathematical investigations

Complete source texts below, retaining mathematical arguments, hypotheses, counterexamples, corrections and unresolved cases. No new independent audit or theorem promotion.

---

## Source: 2026-10-20-normal-filtration-research-report.md

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


---

## Source: 2026-10-20-z4-local-structure.md

# Exact local and global structure of the prescribed characteristic-two Z4

Status: independently reconstructed computation and proof contribution for the
2026-10-20 lifting investigation; not a promoted canonical result. No accepted
normal-bundle computation is rederived here. This note concerns only

\[
 C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
 \qquad Z_4=V(x_1^4-x_0^3x_3,x_2^4-x_0x_3^3)
\]

over \(k=\mathbf F_2\), together with ambient coordinate identities over
\(\mathbf Z\). It does not on its own decide the mixed-characteristic lifting
question.

## 1. Correct homogeneous ideal

Put

\[
 q=x_0x_3-x_1x_2,\quad
 f=x_1^3-x_0^2x_2,\quad
 h=x_1^2x_3-x_0x_2^2,\quad
 g=x_2^3-x_1x_3^2.
\]

Over both \(\mathbf Q\) and \(\mathbf F_2\), exact kernel elimination gives

\[
 I_C=\ker(k[x_0,x_1,x_2,x_3]\longrightarrow k[s,t])=(q,f,h,g),
\]

for the map specified by the parametrization. The three polynomials \(q,f,g\)
in the question give an unsaturated homogeneous ideal, although their ideal
sheaf is correct:

\[
 (q,f,g)^{\mathrm{sat}}=(q,f,h,g),\qquad h\notin(q,f,g).
\]

The saturation inclusion can also be checked without elimination from

\[
\begin{aligned}
 x_0h&=x_1^2q+x_2f, & x_1h&=x_3f+x_0x_2q,\\
 x_2h&=-x_0g-x_1x_3q, &x_3h&=-x_1g-x_2^2q.
\end{aligned}
\]

The kernel and saturation equalities, including the omitted-generator test,
are checked over both fields by the accompanying script. For a geometric
check of the image and the absence of other projective components, on
\(x_0\ne0\) one obtains \((x_1,x_2,x_3)=(u,u^3,u^4)\); on
\(x_3\ne0\), one obtains \((x_0/x_3,x_1/x_3,x_2/x_3)=(c^4,c^3,c)\).
The equations have no projective point with \(x_0=x_3=0\).
The Hilbert polynomial is \(4d+1\).

## 2. Exact charts and full transition

On \(U=\{x_0\ne0\}\), write

\[
 u=x_1/x_0,\qquad X=x_3/x_0-u^4,\qquad Y=x_2/x_0-u^3.
\]

(The notation \(u=x_1\) in the question is its usual dehomogenized form.)
In characteristic two,

\[
 F=-X,\qquad G=Y^4+u^8X+u^4X^2+X^3,
\]

so \((F,G)=(X,Y^4)\) exactly and

\[
 Z_4\cap U=\operatorname{Spec}k[u,Y]/(Y^4).
\]

On \(V=\{x_3\ne0\}\), use the question's coordinates

\[
 c=x_2/x_3,\qquad A=x_0/x_3-c^4,\qquad B=x_1/x_3-c^3.
\]

There \(G=-A\) and
\(F=B^4+c^8A+c^4A^2+A^3\); hence \((F,G)=(A,B^4)\) and

\[
 Z_4\cap V=\operatorname{Spec}k[c,B]/(B^4).
\]

On the overlap, \(u\) is a unit because \(x_3/x_0=u^4\) on \(Z_4\). The
complete transition, with no suppressed terms of degree at most three, is

\[
\boxed{\quad
 c=u^{-1}+u^{-4}Y,\qquad A=0,\qquad
 B=u^{-6}Y+u^{-9}Y^2+u^{-12}Y^3.\quad}
\]

It follows directly by dividing \(x_2=u^3+Y\) and \(x_1=u\) by
\(x_3=u^4\), and expanding \(c^3\). Its inverse is

\[
 u=c^{-1}+c^{-4}B,\qquad
 Y=c^{-6}B+c^{-9}B^2+c^{-12}B^3.
\]

Both compositions are checked exactly in a Laurent polynomial quotient in
the script. The charts cover all of \(Z_4\): if \(x_0=x_3=0\), its equations
force \(x_1=x_2=0\). Thus these calculations also prove globally that the
reduced support is exactly \(C\), with no further projective component.

## 3. Nilradical filtration and actual multiplication

Let \(J=I_C\mathcal O_{Z_4}\). On \(U\), \(J=(Y)\); on \(V\), \(J=(B)\).
Thus \(J^4=0\), \(J^3\ne0\), and for \(0\le i\le3\),

\[
 J^i/J^{i+1}\simeq\mathcal O_{\mathbf P^1}(-6i),
\]

where the \(i=0\) term is \(\mathcal O_C\). Indeed,

\[
 B\equiv u^{-6}Y\pmod{J^2},\qquad
 B^2=u^{-12}Y^2,\qquad B^3=u^{-18}Y^3.
\]

The multiplication maps between these graded pieces are the isomorphisms

\[
 \mathcal O(-6i)\otimes\mathcal O(-6j)
 \longrightarrow\mathcal O(-6(i+j))\quad(i+j\le3),
\]

sending \(Y^i\otimes Y^j\) to \(Y^{i+j}\), and are zero when \(i+j\ge4\).
Locally the full multiplication is

\[
 (\sum_{i=0}^3a_i(u)Y^i)(\sum_{j=0}^3b_j(u)Y^j)
 =\sum_{n=0}^3\bigl(\sum_{i+j=n}a_i(u)b_j(u)\bigr)Y^n.
\]

This multiplication must be glued by the complete transition above, including
the nilpotent change in the base coordinate \(c\). It is not specified by the
graded pieces alone. More explicitly, if
\(s=\sum_{j=0}^3a_j(c)B^j\), write \(a_j^{[r]}\) for its \(r\)-th Hasse
derivative evaluated at \(u^{-1}\). Its coefficients in the \(U\) chart are

\[
\begin{aligned}
 [1]s={}&a_0^{[0]},\\
 [Y]s={}&u^{-4}a_0^{[1]}+u^{-6}a_1^{[0]},\\
 [Y^2]s={}&u^{-8}a_0^{[2]}+u^{-10}a_1^{[1]}
                  +u^{-9}a_1^{[0]}+u^{-12}a_2^{[0]},\\
 [Y^3]s={}&u^{-12}a_0^{[3]}+u^{-14}a_1^{[2]}
                 +u^{-13}a_1^{[1]}+u^{-12}a_1^{[0]}
                 +u^{-16}a_2^{[1]}+u^{-18}a_3^{[0]}.
\end{aligned}
\]

These formulas follow by substitution and hold for regular functions on the
overlap; Hasse derivatives avoid division by factorials in characteristic two.
The script checks monomials \(c^mB^j\), \(0\le m\le12\), \(0\le j\le3\), as
additional finite identities. The proof for all regular coefficients is the
formal Hasse substitution identity, not an inference from that finite sample.

For an explicit check that the base-coordinate term carries geometric
information, even \(Z_2\) has no retraction to \(C\) inducing the identity on
\(C\). Such a retraction would have coordinates
\(u'=u+a(u)Y\) and \(c'=c+b(c)B\) on the two charts, with \(a,b\) polynomial.
The equality \(c'=(u')^{-1}\) modulo \(Y^2\) would force

\[
 u^2+b(u^{-1})=u^4a(u).
\]

The Laurent coefficient of \(u^2\) makes this impossible: the other terms
have exponents at most zero or at least four. This is a structural observation
inside characteristic two, not a mixed-characteristic obstruction.

## 4. Lower thickenings and global numerical checks

The ideal sheaf of \(Z_n\) in the ambient projective space is
\(\widetilde{(F,G)+I_C^n}\), and its saturated homogeneous ideal is
\(((F,G)+I_C^n)^{\mathrm{sat}}\). The exact chart ideals are
\((X,Y^n)\) and \((A,B^n)\). The script prints all four saturated ideals.
For example,

\[
 I_{Z_2}=(h,F,G,q^2)\quad\text{over }\mathbf F_2.
\]

The full homogeneous \((F,G)\) is already saturated. Exact ideal tests also
verify \(\sqrt{(F,G)}=I_C\), \(I_C^4\subset(F,G)\), and
\(I_C^3\not\subset(F,G)\).
From the filtration and \(\mathcal O_C(1)=\mathcal O_{\mathbf P^1}(4)\),

\[
 P_{Z_n}(d)=\sum_{i=0}^{n-1}(4d-6i+1)
           =4nd+4n-3n^2.
\]

Thus the polynomials are respectively \(4d+1\), \(8d-4\), \(12d-15\), and
\(16d-32\). All agree with independent homogeneous Hilbert-polynomial
computations. Macaulay2 prints its answer in the basis
\(P_{\mathbf P^0}=1\), \(P_{\mathbf P^1}=d+1\); for instance its output
`{0 => -48, 1 => 16}` means \(16(d+1)-48=16d-32\).

## 5. Ambient normal-coordinate expansions over the integers

For any characteristic, on the ambient overlap put
\(d=u^4+X\). The exact rational coordinate identities are

\[
 c=(u^3+Y)/d,\qquad A=d^{-1}-c^4,\qquad B=u/d-c^3.
\]

Modulo total normal degree four, these give

\[
\begin{aligned}
 c={}&u^{-1}+u^{-4}Y-u^{-5}X
       -u^{-8}XY+u^{-9}X^2+u^{-12}X^2Y-u^{-13}X^3,\\
 A={}&3u^{-8}X-4u^{-7}Y
       -9u^{-12}X^2+16u^{-11}XY-6u^{-10}Y^2\\
    &+19u^{-16}X^3-40u^{-15}X^2Y+24u^{-14}XY^2-4u^{-13}Y^3,\\
 B={}&2u^{-7}X-3u^{-6}Y
       -5u^{-11}X^2+9u^{-10}XY-3u^{-9}Y^2\\
    &+9u^{-15}X^3-18u^{-14}X^2Y+9u^{-13}XY^2-u^{-12}Y^3.
\end{aligned}
\]

The script verifies these identities in
\(\mathbf Z[u,u^{-1},X,Y,z]/(z^4)\), replacing \(X,Y\) by \(zX,zY\).
Thus they are integer polynomial identities in a nilpotent quotient, rather
than numerical or analytic approximations. Reducing modulo two and imposing
\(X=0\) recovers exactly the characteristic-two transition in section 2.

## Reproducibility and scope

Run, from the repository root:

```sh
/opt/homebrew/bin/M2 --script research/computations/verify_z4_local_structure_2026_10_20.m2
```

Code: [verify_z4_local_structure_2026_10_20.m2](../computations/verify_z4_local_structure_2026_10_20.m2).
Recorded output: [local-structure.log](../validation/z4-lift-2026-10-20/local-structure.log).
The last line is `ALL LOCAL/GLOBAL STRUCTURE CHECKS PASS`.
The calculations use exact integer, rational, and finite-field arithmetic.
The first failed development invocation attempted M2 through `/dev/stdin`,
which M2 could not resolve on this host; that invocation performed no
mathematical check. An initial multiline-expression parsing error in the
coordinate test was corrected by explicit parentheses before the recorded
successful run. A trial integral `ker` call was unsupported by the installed
M2 ring-map implementation; the final script restricts kernel computations to
QQ and F2 and separately verifies the normal expansions over ZZ.

No obstruction to a characteristic-zero lift is asserted in this note. In
particular, \(J^4=0\) and the displayed conormal line bundles are properties
of the prescribed special fiber; neither is imposed on an arbitrary lift by
this calculation. Establishing the deformation reduction and the eventual
obstruction is a separate contribution to the main lifting report.


---

## Source: 2026-10-21-conditional-2-12-certificate-discrepancy-diagnostic.md

# Diagnostic: failed reconstructed-versus-exported FIRST residual comparison

Date: 2026-10-21. Status: **diagnostic only; no repaired certificate and no theorem promotion**.

The committed `conditional_2_12_certificate_audit_cont2_2026_10_21.json` reports an M2 assertion failure at line 23 of the generated `.m2` script. Line 22 asserts that rows 0–3 and 12–15 of the reconstructed universal FIRST operator vanish; line 23 compares rows 4–11 with the saved eight-polynomial export from `conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2`.

A separate direct arithmetic evaluation of the *recorded expressions* gives:

- Set `w=1, a=0, x=0, h4=h5=h6=h7=0`: the eight differences (reconstruction minus saved export) all vanish.
- Set `w=1, a=1, x=2, h4=h5=h6=h7=0`: the eight differences are `(12, 9/2, 0, -43/8, 175/4, 43/4, -27/4, 3/4)`.

Thus the assertion is not simply a failure to normalize syntactically equivalent polynomial expressions: the recorded expressions have different values at a rational point. The discrepancy affects seven of the eight residual rows at this test point. This is an arithmetic spot check, **not a rerun of Macaulay2**.

Next checks: independently derive the original factor-to-coefficient map, check the ordering of `ff` against the universal FIRST variables, and compare the saved export's coordinate conventions and reduction assumptions. For each of the eight rows, print `actual#(i+4)-exported#i` in Macaulay2 and isolate the earliest divergence. Do not silently replace the saved export with the reconstructed list; the source of the disagreement remains unidentified. In particular, no certificate depending on this equality is a pass until rerun with explicit exact identities.


---

## Source: 2026-10-21-equality-orders-filtration-duality.md

# Equality de=4m: generic orders, Hilbert filtration, duality

Status: WORKING NOTE; mathematical statements separated from proposed directions. No canonical promotion. Characteristic zero unless otherwise indicated.

Setup: C=[s^4:s^3t:st^3:t^4] smooth rational quartic, F,G homogeneous degrees d,e with no common surface component, C contained in their intersection. r=ord_C(F), s=ord_C(G), m=length at generic point of C. If de=4m, the entire reduced intersection is C by the residual-cycle proposition.

## Generic orders and full initial algebra

In R=k(C)[[x,y]], F_r,G_s are nonzero binary homogeneous forms. The plane local intersection inequality m>=rs holds. Equality iff gcd(F_r,G_s)=1 (initial forms a regular sequence). In that case the full m-adic initial ideal is (F_r,G_s), and the Hilbert series of the generic associated graded Artin algebra is (1-z^r)(1-z^s)/(1-z)^2. Hence de=4m forces de>=4rs, and de=4rs precisely in the coprime-initial case. If F_r,G_s have a common factor, m>rs; their full initial ideal needs cancellation generators.

For the fixed curve in characteristic zero, N_C/P3=O(7)^2, so a nonzero r-th conormal symbol of a degree-d form lies in H0(P1,O(4d-7r))^(r+1). Necessarily 4d>=7r, and similarly 4e>=7s. This is a generic-order bound independent of the STCI equality. Stronger restrictions (such as d>=3r) in existing results require their stated hypotheses and must not be silently generalized. In characteristic two the normal bundle splitting differs and the 7r bound must not be transplanted.

## Intrinsic filtration

For Z=V(F,G) with Z_red=C, J=I_C O_Z is nilpotent and Q_i=J^i/J^(i+1) are coherent O_C-modules. The generic ranks h_i=dim_k(C)(Q_i)_eta satisfy Σ_i h_i=m and h_0=1. The generic Hilbert function (h_i) is the Hilbert function of the full initial algebra. The natural maps Sym^i(I_C/I_C²) -> Q_i are surjective, hence h_i<=i+1, but no flatness/local freeness of Q_i is assumed.

The Hilbert polynomial of the (d,e) complete intersection Z is P_Z(n)=de*n - de(d+e-4)/2; with de=4m, χ(O_Z)=-2m(d+e-4). Additivity gives Σ_i χ(Q_i)=-2m(d+e-4). Each Q_i has generic rank h_i and may have torsion; if Q_i is locally free, χ(Q_i)=deg(Q_i)+h_i on C=P1. This is an identity, not an obstruction without control on degrees/torsion.

## Duality

Z is Gorenstein and ω_Z=O_Z(d+e-4). Generic local algebra A=O_{Z,η_C} is an Artinian Gorenstein complete intersection. Its socle has dimension one, but the m-adic associated graded algebra need not be Gorenstein; therefore do not assume perfect pairings between opposite graded layers without an additional hypothesis. Globally, the dualizing sheaf and filtration interact through Ext/duality, but the exact associated-graded duality requires care with torsion and nonsaturated layers.

## Characteristic benchmark

F=x1^4-x0³x3, G=x2^4-x0x3³. On x0=1, local coordinates t=x1,u=x2-t³,v=x3-t⁴ yield (v,(t³+u)^4-t¹²). In char 0 generic m=1, hence residual degree 12. In char 2 generic m=4, hence de=4m and reduced support exactly C. In char 2 first symbols of both equations are proportional (r=s=1 generically); this shows that r=s=1 does not imply m=1.

## Canonical scope references

- [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) proves the characteristic-dependent conormal splitting used in the degree bound.
- [STCI-R-0021](../results/quartic_mu4_degeneration.md) establishes the global characteristic benchmark for the specified quartic pair.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md) concern restricted saturated/nonsaturated first-relation settings; the ordinary filtration and duality observations here do not assert their conclusions without those hypotheses.
- The elementary Bézout residual-cycle identity is distinct from the conditional auxiliary-surface residual zero-cycle theorem [STCI-R-0019](../results/quasiprimitive_residual_cycles.md).

## Investigation priorities

Understand constraints on possible generic Hilbert functions h_i given r,s and the local CI property; relate global degrees of Q_i, torsion, and χ to duality without assuming normal flatness; separate characteristic-sensitive normal bundle arguments. No search for counterexamples or numerical exclusion until these structures are clarified.


---

## Source: 2026-10-21-focused-reconciliation-math-review.md

# Focused mathematical review: forced triple and residual-cycle globalization

Date: 2026-10-21. Scope: fresh line-by-line reasoning on two proof interfaces, independently of their recorded audit verdicts. This is not a re-run of every computational certificate.

## 1. R0012: why a hypothetical full lift forces a flat primitive triple

Let R be Z_(2) or Z_2, and let I be the ideal of a flat embedded lift of the prescribed (4,4) complete intersection. The exact sequence 0 -> I(4) --2--> I(4) -> I_0(4) -> 0 and H^1(I_0(4))=0 make multiplication by 2 surjective on finite H^1(I(4)); Nakayama kills this group. The two special quartics lift to global generators. Their cokernel vanishes on the special fiber; properness over the DVR eliminates a possible generic-only support. Thus the full family remains a (4,4) complete intersection.

If its generic reduced support is C, the generic degree-16 complete intersection has length four along the degree-four C. Cohen--Macaulay purity makes the generic local Artin algebra inject into its generic-point localization, where the fourth power of the maximal ideal is zero. R-flatness then descends I_C^4 subset I and I subset I_C to the total family.

The first conormal matrix has special rank one at every point; properness rules out a rank-zero point upstairs. Its generic rank cannot be two, since that would force multiplicity one. Its determinant vanishes generically and hence identically on the integral relative C, so the matrix has constant rank one. A local quartic combination H with unit normal coefficient cuts out a smooth relative surface W containing Z, and C is Cartier on W with local equation ell. On the generic fiber the other equation defines exactly ell^4. Both ideals I_(Z/W) and (ell^4) are 2-saturated (the former from R-flatness, the latter from its filtration by flat line bundles). Therefore they agree integrally. This yields local O_W/(ell^4), so every canonical quotient by J^n, especially J^3, is R-flat and reduces to the prescribed special stage. No independently chosen triple or global splitting is assumed.

The obstruction calculation then uses every first-order quotient p=a+bu+3hu^2, q=d+2hu and all quadratic corrections. For the prescribed mod-2 ribbon a,b,h are even and d is odd. Its H^1(O(-4)) coefficient C2=(b-d)(4ah+3b^2-8bd+6d^2) is 2 mod 4, since the first factor is odd and the second is 2 mod 4. The cohomology basis u^-1,u^-2,u^-3 is free over R; no coboundary can cancel that coefficient.

**Assessment: PASS for the stated unramified DVRs and fixed generic support.** The reduction to the triple is a consequence of flatness and the global CI, not an extra assumption. The arithmetic calculation was checked symbolically at the parity level here, not by re-running its complete expansion. Ramified DVRs and unrelated characteristic-zero multiple structures remain outside scope.

## 2. R0019: from local Smith lengths to global residual cycles

At a closed point of C, complete at R=k[[t]]. The CI algebra B is finite over R because its support is C, and torsion-free because a one-dimensional CI is Cohen--Macaulay with no embedded zero-dimensional associated prime. Thus B is free of rank m. Its saturated curvilinear filtration gives a free R-basis b_0=1,b_1,...,b_(m-1) adapted to the flag.

For q in the first nilpotent layer with nonzero generic first class, multiplication by q has zero first row and zero last column. Deleting them leaves an (m-1)-square triangular block with diagonal the maps E_i -> E_(i+1), whose valuations are ord(q_1)+ord(D_(i+1))-ord(D_i). The determinant is nonzero; it is the only potentially nonzero maximal minor, so the Smith-normal-form torsion length is (m-1)ord(q_1)+ord(D_(m-1)). This does not depend on higher coefficients of q.

On a smooth auxiliary surface Q, let h cut out C and write F|Q=h rho, G|Q=h sigma. Provided rho,sigma have no common curve component, cancellation of the nonzerodivisor h in the local ring of Q gives the exact sequence 0 -> O_(rho,sigma)(-C) -> O_Q/(h rho,h sigma) -> O_C -> 0. The middle term is B/qB; its torsion submodule is exactly the finite-length left term, because the right term is free over R. Therefore at each closed point the proper intersection multiplicity of rho and sigma equals the Smith length. Summing these local equalities, not merely their degrees, gives [rho intersect sigma]=(m-1)T+D_(m-1).

**Assessment: PASS conditional on finite-flat curvilinearity, saturated invertible order quotients, nonzero generic first class of q, and proper residual intersection.** The identity is one of zero-cycles. It neither asserts scheme equality nor survives an improper residual intersection without a separate correction.

## 3. Remaining scope boundaries

These checks validate the two logical interfaces but do not independently re-run all Macaulay2/Python calculations or prove that an arbitrary characteristic-zero STCI has the quasiprimitive filtration of R0019. In R0016, the nonsaturated resultant identity is proved by its separately audited duality and local flatness lemmas; R0010 serves as the saturated comparison and R0011 supports only the repeated-root strengthening.


---

## Source: 2026-10-21-intrinsic-ribbon-triple-independent-audit.md

# Independent audit: intrinsic embedded ribbon-to-triple obstruction (2026-10-21)

Status: **independent mathematical audit; verdict B (correct after replacing the flawed difference argument by a canonical module extension)**. Research branch only; no canonical promotion.

## Scope and source provenance

Read `AGENTS.md`, `research/INDEX.md`, `research/AUTHORITY.md`, `research/CONTRIBUTING_AGENT.md`, the provisional theorem on `research/intrinsic-ribbon-triple-2026-10-21`, the literature report on `research/z4-intrinsic-obstruction-literature-2026-10-21`, and the five 2026-10-20 lifting reports on `main`. This audit proves the *general embedded torsor theorem* independently; it does not rerun the previously audited Laurent arithmetic. The explicit quartic coefficient is imported as an independently audited prior calculation, not a fresh computation.

## Verdict B and corrected theorem

Let `i:C -> X` be a regular immersion of codimension two of schemes, with ideal `I`, and `E=I/I²`. Fix a surjective homomorphism of locally free sheaves `q:E -> L` with `L` invertible and kernel `M` invertible. Put `J₂=ker(I -> E -> L)`, and define the **canonical ideal** `K=I J₂+I³` (indeed `I³ ⊂ I J₂`).

There is a canonical exact sequence of **O_C-modules**
```
0 -> L^⊗2 -> J₂/K -> M -> 0.                    (*)
```
The sheaf of embedded ideals `J₃` satisfying `I³ ⊂ J₃ ⊂ J₂`, with local primitive-triple normal form `(x-a y²,I³)` for generators adapted to `q`, is canonically identified with the sheaf of O_C-linear splittings of (*). It is a locally nonempty torsor under `H=Hom_O_C(M,L²)`. Its class is exactly the Yoneda extension class
```
o_X(q) = [J₂/K] ∈ Ext¹_O_C(M,L²) = H¹(C,H).
```
It vanishes exactly when a global embedded primitive triple exists. If one exists, the set of global embedded triples is a torsor under `H⁰(C,H)`.

This holds in arbitrary characteristic, including mixed-characteristic DVRs; smoothness over a DVR is sufficient but not required beyond the stated regular immersion and locally free quotient. The claim is about embedded ideals in the fixed X and the fixed quotient q, not about abstract multiple curves.

## Independent proof

1. Regular immersion gives `I²/I³ ≅ Sym²(E)`. Since `J₂` is the inverse image of `M`, `I² ⊂ J₂`, and the image of `I J₂` in `I²/I³` is precisely the image `ME` of `M ⊗ E -> Sym²(E)`. Consequently
```
(I²+K)/K = I²/(I J₂+I³) ≅ Sym²(E)/(ME) ≅ Sym²(L)=L².
```
The last isomorphism is canonical for a line quotient, with no need to invert 2. The quotient `J₂/I²=M`. These identify the kernel and cokernel of (*).

2. Since `I J₂ ⊂ K`, multiplication by `I` kills `J₂/K`. Thus (*) is genuinely an exact sequence of O_C-modules, not a spurious O_C-module structure on `I/I³`. This repairs the central gap in the provisional proof.

3. For any admissible `J₃`, `I J₃ ⊂ J₃`, `I³ ⊂ J₃`, and the local normal form implies that the image of `J₃` in `E` is `M` and its intersection with `I²` modulo `I³` is `ME`. Therefore `K ⊂ J₃` and `J₃/K -> M` is an isomorphism: its inverse is a splitting of (*).

4. Conversely, a splitting `s:M -> J₂/K` has image an O_C-submodule. Its inverse image `J₃` in `J₂` is an O_X-ideal: multiplying an element of `J₃` by a function in O_X preserves its image modulo K because the action factors through O_C, and `K` is an ideal. It contains K and hence I³, and maps onto M with quadratic intersection ME. Étale/Zariski locally choose adapted generators `x,y` of I, with x mapping to M and y to L. A splitting is generated modulo K by `x-a y²` for some local coefficient a, hence `J₃=(x-a y²,I³)`; the terms x²,xy already belong to the ideal. Since x-a y² is another regular generator of I near C, this is equivalent locally to `(x-a y²,y³)`, a primitive triple with graded pieces O_C,L,L². The construction works over any DVR without division.

5. Splittings of an exact sequence with locally free quotient M exist locally. The difference of two splittings is a unique O_C-linear map M -> L². This action is free, transitive, additive and restriction-compatible. The construction uses only intrinsic ideals and module operations.

6. On a trivializing cover choose splittings s_i and set h_ij=s_j-s_i. Then h_ij+h_jk=h_ik. Replacing s_i by s_i+t_i adds the Čech coboundary t_j-t_i. Vanishing means the splittings can be adjusted to agree and glue, and inverse images in J₂ give a global *embedded ideal*. Conversely a global ideal yields a global splitting. Standard sheaf Ext gives Ext¹(M,L²)=H¹(Hom(M,L²)) because M is locally free. There is no nonabelian obstruction at this fixed embedded stage.

## Arbitrary adapted coordinate transformations

Locally choose generators x,y of I with q(x)=0 and q(y) a frame of L. Any other adapted generators, modulo I³, have the form
```
x' = α x + A x² + B xy + C y²,
y' = β x + δ y + D x² + E xy + F y²,
```
where α and δ restrict to units on C; coefficients may be ambient functions, including dependence on moving base coordinates. Terms from nilpotent variations of these coefficients are already included in their quadratic jets. In the quotient by `(x-a y²,I³)`, x=a y², y'=δ y + O(y²), and x'=(α a+C)y². Hence
```
a' = (α a+C)/δ²
```
with all coefficients restricted to C (and the appropriate local frames). For two choices a,b in the *same original frame*,
```
a' - b' = (α/δ²)(a-b).
```
This is exactly the transition for Hom(M,L²): x' has M-frame αx, y' has L-frame δy. The affine translation C/δ² may depend on the full quadratic neighborhood and base-coordinate movement; it cancels in differences. Arbitrary linear mixing β, all x²/xy terms, and quadratic corrections to y' do not change this result. No chosen retraction of the quadratic neighborhood is used. Equality is equality of ideals, not of preferred generators.

## Functoriality, base change and dependence

Isomorphisms of embedded triples (X,C,q) carry I,J₂,K and (*) to their counterparts, hence carry the Yoneda class functorially. For a flat base change of the ambient setup, the defining ideals, conormal exact sequence and (*) pull back exactly, and the extension class pulls back naturally. For nonflat base change, the same conclusion holds **if** the regular immersion and the conormal quotient remain compatible, the relevant ideal/product/graded identifications commute with pullback, and the pulled-back sequence remains exact; it is not automatic for arbitrary base change. Natural pullback of the Ext class does not assert that the cohomology base-change map is an isomorphism. The class is determined by the embedded quadratic neighborhood O_X/I³ and q: J₂/K is computed entirely inside that truncation. It need not be determined by the associated graded algebra Sym(E) or by the abstract ribbon alone.

## Quartic consistency

For the specified relative rational quartic and distinguished quotient `L=O(-6), M=O(-8)`,
```
H = M^∨ ⊗ L² = O(-4).
```
On the two standard affine charts, H¹(O(-4)) has Laurent representatives u^-1,u^-2,u^-3. The earlier independently audited raw ambient calculation yields the transition defect `K(u)` and for the distinguished quotient `[-6u^-2]`. The current theorem proves **why** the difference of local kernel equations represents the intrinsic Yoneda extension class: each local equation defines a splitting of (*), and their normalized differences are precisely its Čech connecting cocycle. This identifies the type and intrinsic meaning of the previously audited numerical class; it is not a new re-expansion or a re-verification of the sign conventions. The earlier lifting audit establishes the middle coefficient is 2 mod 4 for all specified admissible quotients over Z_(2) and Z_2. No claim for arbitrary ramified DVRs follows.

## Explicit defect in the provisional proof

The statement that one can subtract arbitrary lifts of M *inside I/I³* as O_C-linear maps is not justified: I/I³ has no canonical O_C-module structure. Also the expression I²/(I³+IJ) is circular unless J is fixed and it does not by itself define a common comparison object for varying J. The common object is instead **J₂/(I J₂+I³)**. It is annihilated by I, so the difference construction and its additive law are literal O_C-module statements. The original numerical calculation survives; the original general proof should not be promoted verbatim.

## Audit status and handoff

**Verdict B.** The corrected embedded torsor theorem and its descent/coordinate invariance are proved above by a canonical short exact sequence. No symbolic calculation was needed for the general proof. The quartic coefficient and its universal mod-4 reduction remain imported from the five independently reviewed October 20 reports, not recomputed here. Investigation 3 may safely use the intrinsic extension class as a proved construction, subject to citing this corrected theorem and preserving the fixed-q and base hypotheses. Any identification with divided Frobenius remains unproved. Do not promote or merge this branch without separate repository review.


---

## Source: 2026-10-21-investigation-4-general-pr-mechanism-preliminary.md

# Investigation 4: universal divided-power arithmetic and geometric limits (preliminary)

**Status:** preliminary mathematical analysis from the 2026-10-21 conversation. Not independently audited, not promoted, and not a canonical divided-Frobenius identification.

## 1. Arithmetic theorem

Let \(p\) be prime, \(r\ge1\), and \(0<j<p^r\). Then
\[
v_p\binom{p^r}{j}=r-v_p(j).
\]
Proof: \(j\binom{p^r}{j}=p^r\binom{p^r-1}{j-1}\), and Lucas's theorem gives \(\binom{p^r-1}{j-1}\not\equiv0\pmod p\), because the digits of \(p^r-1\) are all \(p-1\).

Define the integral polynomial
\[
\Delta_{p^r}(a,b)=\frac{(a+b)^{p^r}-a^{p^r}-b^{p^r}}p.
\]
The only terms surviving modulo \(p\) have exponent \(j=kp^{r-1}\), \(1\le k<p\). Their coefficients satisfy
\[
\frac1p\binom{p^r}{kp^{r-1}}\equiv \frac{(-1)^{k-1}}{k}\pmod p,
\]
so
\[
\Delta_{p^r}(a,b)\equiv
\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}{k}
a^{(p-k)p^{r-1}}b^{kp^{r-1}}
=\Delta_p(a^{p^{r-1}},b^{p^{r-1}})\pmod p.
\]
For \(p=2,r=2\), this is \(a^2b^2\); for \(p=2,r=3\), \(a^4b^4\); for \(p=3,r=2\), \(a^6b^3+a^3b^6\).

## 2. Relative obstruction framework (conditional)

For an unramified DVR \(R\) with uniformizer \(p\), suppose a flat parameter space of marked embedded conormal quotients carries a locally free relative Ext obstruction bundle \(\mathcal H\), with a canonical obstruction section \(o\) vanishing on the special fiber. Over the appropriate flat first-order congruence space, the reduction \(o\bmod p^2\) is divisible by \(p\), yielding a leading section \(\lambda\) via \(p\mathcal H/p^2\mathcal H\simeq\mathcal H/p\mathcal H\). If its restriction to the first-order lift torsor is affine-linear, the difference map \(D:T\to H_k\) is linear and the image of \(\lambda\) in \(\operatorname{coker}D\) is lift-independent. Nonvanishing then obstructs every lift in the *specified marked family*. Flatness, base change, the comparison of special-fiber obstruction spaces, and affine linearity must be proved in each example. This does not construct a divided-Frobenius map into the cokernel.

## 3. Counterexample to automatic nonvanishing

Let \(C_R\) be a smooth curve and take a split rank-two conormal bundle \(E=M\oplus L\). The zero section of the corresponding vector bundle has local normal coordinates \(x,y\) and admits globally compatible primitive thickenings \(J_n=(x,y^n)\), using the splitting. The ribbon-to-triple Yoneda obstruction vanishes. Yet the universal polynomial \(\Delta_{p^r}\bmod p\) is nonzero. Therefore universal arithmetic nonzero cross-effects do **not** force nonzero geometric obstruction classes.

## 4. Normal-order observation and limits

If \(a\) is a unit along \(C\) and \(b\in I_C\) is a normal parameter, the least normal degree of \(\Delta_{p^r}(a,b)\bmod p\) is \(p^{r-1}\). Thus this *particular leading cross-effect* appears in a quadratic normal neighborhood only when \(p^{r-1}\le2\). This does not exclude other contributions or establish a universal thickening stage. In particular, the quartic \(p=2,r=2\) case has the suggestive quadratic term \(a^2b^2\), but a canonical comparison to the Yoneda obstruction has not been constructed.

The cross-effect satisfies the additive polynomial 2-cocycle identity; for \(r=1\), its negative is the usual carry polynomial in length-two \(p\)-typical Witt addition. Such an arithmetic cocycle is **not automatically** a Čech cocycle of embedded thickenings.

## 5. Open mathematical problem

Construct a natural, coordinate-independent comparison from a divided-power/Frobenius/Witt operation into an appropriate relative embedded obstruction cokernel, with precise marking and base-change hypotheses; alternatively, show why no such map exists generally. Separate (a) universal arithmetic identities, (b) intrinsic deformation-theoretic construction, and (c) nonvanishing in a specific embedded example.

**No new script or independent audit accompanies Investigation 4.**
