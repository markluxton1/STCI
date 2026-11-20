---
id: STCI-R-0078
type: result
title: Quadratic conductor postulation at one moving point
scope: "#scope"
statement: "#statement"
proofs:
  - name: separated covers, transverse lattices and the osculating quadric
    at: "#proof"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Quadratic conductor postulation at one moving point

A quadratic cover converts a hypothetical two-equation presentation into
postulation conditions on a finite boundary. Moving its branch section
concentrates that boundary at one general point, so the conditions become
an explicit map on actual homogeneous forms. For the general one-point
osculating cover, its length cannot contradict the displayed scalar bound
on any generically regular smaller carrier; the embedded kernel retains
information that this comparison loses.

## Scope

Let \(Y=V(F_a,G_b)\subset\mathbf P^3\) be an actual proper homogeneous
complete intersection with sole support \(C_0=[s^4:s^3t:st^3:t^4]\)
over an algebraically closed field of characteristic zero.
Write \(5\le a\le b\), \(n=ab/4\), and \(H\) for the Hilbert function
of the maximal-ideal filtration of its generic transverse Artin
algebra. The proof below takes \(a\ge5\) as a hypothesis. Applying
that degree range to unrestricted existence uses the separately reviewed
[quartic-carrier exclusion](quartic_carrier_exclusion.md), which is not
reproved here.
Put \(\Lambda_j=\#\{i:H_i\ge j\}\), \(L=\Lambda_1\), and
\[
 S_\Lambda=\sum_j\binom{\Lambda_j}{2},\qquad
 M_\Lambda=\sum_j\lfloor\Lambda_j/2\rfloor,\qquad
 D_H=\min_{c\in\mathbb R}\sum_i H_i|i-c|.
\]
For the homogeneous-kernel and scalar-postulation assertions assume \(F\) integral.
This covers the unrestricted existence question: every pair of opposite
irreducible factors of a hypothetical presentation cuts a nonempty
curve supported on \(C_0\), hence is itself a presentation. Its
degrees and transverse algebra are those of that factor pair.

## Statement

1. Adjoin a square root of any ambient quadric restricting to \(w^2\)
   on \(C_0\), with \(w\) outside the ambient linear series on \(C_0\).
   The conductor boundary \(\Delta\) of either separated branch of \(Y\)
   has length at most \(4S_\Lambda\). A general choice attains this
   maximum at four simple zeros of \(w\). There
   \(\Delta\cap C_0=(L-1)\operatorname{div}(w)\) as a scheme on the
   reduced curve. At an arbitrary marking the maximum is attained
   exactly when multiplication by \(R-w^2\) at all zeros has closed
   Jordan partition \(\Lambda\) as specified in the proof.
2. For general \(p\in C_0\) there is an explicit rank-three quadric
   \(R_p\) singular at \(p\), with zero divisor \(8p\) on \(C_0\).
   It is nonsquare on any preassigned integral surface in \(\mathbf P^3\),
   simultaneously for a finite list after choosing \(p\).
   The whole conductor of the resulting cover is supported at \(p\) and
   \[
                 \ell\Delta_p\le U_H:=3S_\Lambda+D_H-M_\Lambda
                                  \le4S_\Lambda-M_\Lambda .
   \]
3. For this one-point cover the degree-\(d\) piece of the saturated
   boundary ideal is the kernel of the explicit local map
   \({\cal P}_d\) on ambient forms. In particular
   \[
   \ker {\cal P}_d=(F)_d\quad (2d+2<b),\qquad
   \operatorname{rank}{\cal P}_d+
   \operatorname{rank}{\cal P}_{a+b-5-d}\le\ell\Delta_p .
   \]
   Ranks in negative degrees are zero. The scalar lower bound
   \(B_{a,b}\) derived below from this range and complementary postulation is always
   strictly below \(U_H\). Comparing those two numbers alone can never
   exclude a generic transverse Hilbert function in the stated scope.
4. If \(F\) is regular at the generic point of \(C_0\), the *actual*
   one-point length required of a mate exceeds \(B_{a,b}\). It equals
   \((8-s)\lfloor n^2/4\rfloor-4\lfloor n/2\rfloor\), where \(s=2\)
   if the tangent plane of \(F\) equals the osculating plane along
   general \(C_0\), and \(s=1\) otherwise.
5. In the original smooth pencil fixing both endpoints, assume \(F\)
   is smooth at both. To obtain a scalar deficit below \(B_{a,b}\) the
   carrier must be tangent to the containing quadric at both points.
   For \(a\ge6\) its two conormal slopes must also agree and be nonzero,
   leaving at most **one** eligible pencil parameter. For \(a=5\) at
   most two parameters can work. These necessary loci have codimension
   at least three and two respectively in the open subset of
   \(H^0(\mathcal I_{C_0}(a))\) smooth at both points.
   At a candidate parameter the higher normal coefficients
   and nonsplitting on the same carrier still enter.

## Proof

The [moving-cover argument](../arguments/linkage/moving_quadratic_covers.md)
constructs the actual separated algebra, proves the assertions about
the four roots and the osculating cone, and identifies the kernel on
homogeneous forms. The [local lattice argument](../arguments/linkage/quadratic_conductor_lattices.md)
proves the length bounds, the equality criterion at jumps and the
restriction to the reduced curve.
The [smooth-carrier calculation](../arguments/linkage/conductor_on_a_smooth_carrier.md)
gives the exact cyclic length and applies it to both cover families.

For the scalar comparison use the integral carrier \(F\) in assertion 3.
Put \(q=\lceil b/2\rceil-1\) and
\(H_*=\binom{q+2}{3}-\binom{q-a+2}{3}\), with truncated binomials.
This is the rank in degree \(q-1\) from the low-degree kernel. The
[canonical injection](../arguments/linkage/quadratic_covers_and_conductor_descent.md#8-attachment-and-a-global-lower-bound-on-boundary-length)
gives last nonzero \(h\)-vector entry at least \(a+b-4\).
There are no internal gaps in the \(h\)-vector of this standard
graded CM boundary. Applying complementary postulation in degrees
\(q-1,a+b-4-q\) therefore gives \(\ell\Delta_p\ge
B_{a,b}=2H_*+a+b-3-2q\).

Write \(h=\max H_i\). The binary initial form of the degree-\(a\)
equation bounds \(h\) by its normal order. Restriction to the smooth
quadric bounds that order by \(a/3\), since \(C_0\) has type \((1,3)\)
there and the defining equation has no quadric factor. Thus
\[
 3S_\Lambda\ge\tfrac32(n^2/h-n)
      \ge a(9b^2/32-3b/8).
\]
Also \(D_H\ge M_\Lambda\): for each superlevel set of cardinality
\(l\), pair its smallest and largest indices, continuing inward.
Each of the \(\lfloor l/2\rfloor\) pairs contributes at least one to
the distance from any \(c\). To bound \(2H_*\), telescope it as
\(\sum_{j=0}^{a-1}2\binom{q+1-j}{2}\). Its nonincreasing summands
have mean at most the mean of the first five. Bounding these by
\((q-j)(q+1-j)\) gives \(q^2-3q+4\). Using \(2\le q\le(b-1)/2\)
and \(a+b-3-2q\le a-1\) yields
\[
 U_H-B_{a,b}\ge
       a\bigl(b^2/32+13b/8-27/4\bigr)+1>0 .
\]
This compares an upper estimate with a lower estimate. The actual
length at the osculating point can be smaller than the upper estimate.

## Consequence for equation realization

The unrestricted pair can be tested at a general point where its
normal filtration is flat. The global source of each test is still
\(H^0(\mathbf P^3,\mathcal O(d))\). A candidate embedded thickening
with a carrier \(F_a\) fails the required presentation with degree
\(b\) if the one-point kernel contains an independent form at
\(2d+2<b\). The ranks in complementary degrees also test postulation
beyond that onset. The [osculating-plane calculation on an embedded
ribbon](../arguments/linkage/moving_quadratic_covers.md#the-homogeneous-jet-test)
exhibits how to recover an actual equation in the kernel. The outstanding
question is which restrictions of homogeneous forms on a candidate
thickening force such a failure. On a generically regular carrier the
exact length already exceeds the lower bound, including **every integral
quintic** through the curve. A scalar deficit in this one-point osculating
family can therefore come only from a generically singular carrier. In the cyclic case the
upper bound is sharp on the required nonosculating local model; this is
not an existence assertion for a supported CI.

The exceptional osculating direction has a separate global constraint:
its ribbon has [nonzero primitive-triple obstruction](../arguments/normal-geometry/osculating_ribbon_obstruction.md).
A finite-flat quasiprimitive flag extending it needs second-layer defect
degree at least two. The minimum is attained by a projective line of
embedded CM triples, whose defect divisors are osculating involution pairs;
these triples are non-Gorenstein at the defects. At an endpoint the
[flat moving graph](../arguments/linkage/moving_quadratic_covers.md#the-flat-graph-at-the-endpoint)
places its entire generic conductor length in punctual torsion, explaining
why substituting the limiting square quadric loses the conductor.

## Limitations

Neither the scalar estimates nor the ribbon control exclude an arbitrary
pair. The homogeneous-kernel test requires the actual embedded thickening,
and the fixed-endpoint slope calculation assumes the smaller carrier is
smooth at both endpoints. Singular endpoints retain their full lattice
problem. Existence of an unrestricted characteristic-zero pair remains open;
the global conclusions here are not asserted in positive characteristic.

## Review

On November 20, 2026, separate independent reviews reconstructed the
local lattice bound and equality criterion, the singularity estimate,
the exact cyclic lengths and endpoint codimensions, the scalar
postulation comparison, the separated-cover construction, the general
four-root locus, the osculating cone's nonsplitting, and the homogeneous
kernel map. They checked the stated freeness, characteristic-zero,
integrality and actual-CI hypotheses and found no material proof defect.
The height-two Lefschetz input was checked against the
[primary source](../literature/README.md#artinian-jordan-type-and-the-quadratic-conductor).

The companion calculation was replayed with SymPy 1.14.0 and verified
the osculating cone, conductor length three and unique moving plane on
the ribbon control. This is exact support for that control, not a
calculation of a hypothetical supported CI.

The six independent mathematical, editorial and research-context reviews
also identified the sharp cyclic bound, quintic consequence, osculating
ribbon obstruction and flat graph specialization. Each new deduction
received separate proof review. Their integration and the final full-suite
synthesis are recorded with the PR's validation; proof acceptance alone
does not determine the next research priority.
