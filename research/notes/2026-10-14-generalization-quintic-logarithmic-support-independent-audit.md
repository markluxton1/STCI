# Independent audit of the logarithmic binary-support mechanism

Date: 2026-10-14, completed across local midnight on October 15.

Status: **PASS for the new characteristic-zero support mechanism,
quadratic representation test, stabilizer rank test, and unified A4
allowance equations. The attempt-04 matrix is not accepted as the actual
finite-h2 conductor incidence because its input uses a wrong coordinate
binding.** This is an independent written proof audit, not a new quintic
exclusion or a proof of emptiness of any coefficient locus.

The reviewed proposal is
[the logarithmic conductor-support note](2026-10-14-generalization-quintic-logarithmic-conductor-support.md).
Accepted actual-conductor, homogeneous-gcd-cover and previous quintic
certificates are premises. Their verifiers were not rerun. The audit
checks the new elementary implications directly and checks the new
coordinate bridge against the coordinate definitions in those premises.

## 1. General Hamiltonian criterion: independently proved

Let k be algebraically closed of characteristic zero. Let F,H be nonzero
binary forms of degrees n>=1 and h>=1. Define

    D_H = H_t partial_s - H_s partial_t.

Then the following three conditions are equivalent:

    supp(div F) contained in supp(div H);
    F divides H F_s and F divides H F_t;
    F divides D_H F.                                      (A)

Here support is projective support. In the final divisibility D_H F has
degree n+h-2; when h=1 the condition means D_H F=0.

For the middle condition, factor F=ell^m G at any linear factor ell of F,
with ell not dividing G. At least one of the two nonzero constants
ell_s,ell_t is nonzero. Differentiating in that coordinate gives exact
ell-adic order m-1, because m is nonzero in k. Each other coordinate
derivative has order at least m-1. Consequently the two divisibilities
hold at ell precisely when ell divides H. Checking all factors of F
proves the first equivalence, including their full multiplicities.

For the final condition, use s!=0 and x=t/s, writing

    F=s^n f(x), H=s^h q(x).

A direct product-rule calculation gives

    D_H F = s^(n+h-2) [n q'(x) f(x) - h q(x) f'(x)].      (B)

Suppose f has a root alpha of multiplicity m. If q(alpha)!=0, the
second summand has order exactly m-1, while the first has order at
least m. The nonzero scalar h*m prevents cancellation of that leading
term, so F cannot divide D_H F. If q has order r>=1 at alpha, both
summands have order at least m+r-1>=m, including the case in which a
summand vanishes identically. The other projective chart gives exactly
the same argument at s=0. Thus F divides D_H F precisely when every
root of F is a root of H. No squarefreeness assumption is present.

This proof needs both degree h and all relevant multiplicities m to be
nonzero scalars. Characteristic zero supplies that hypothesis. An
unrestricted positive-characteristic statement is false, for instance
when F is a p-th power. For h=1, degree alone forces the quotient to
be zero, and (A) says exactly F is a nonzero scalar multiple of H^n.

The two-derivative formulation yields unique homogeneous quotients
L_s,L_t of degree h-1 and Euler's identity

    H F_s=L_s F, H F_t=L_t F,
    s L_s+t L_t=n H.

These equations and (A) retain all root multiplicities. They express a
support condition; they do not determine conductor multiplicities or
prove descent of a section through a nonnormal surface.

## 2. Quadratic H: the eigenvector test and characteristic polynomial

For H=a s^2+b st+c t^2, D_H preserves degree n. Therefore (A) is
equivalent to

    D_H F=mu F for a scalar mu.                           (C)

For a nonzero coefficient vector f, this is equivalent to all two-by-two
minors of [f | D_H f] vanishing. Indeed, choose any nonzero coefficient
f_i; vanishing of its minors with all other rows gives
mu=(D_H f)_i/f_i and then all rows of (C). Choosing that coefficient
in the proof introduces no coefficient inversion in the global minor
equations themselves.

The induced vector field on x=t/s is -2H(1,x) partial_x. Its zero
divisor is the quadratic divisor of H, including a double zero when
H is a square. Thus the geometric eigenvector argument in the proposal
is also valid: any root outside its zero divisor gives a forbidden
order m-1 term.

The derivation acts on coordinate functions by

    D_H(s)=b s+2c t, D_H(t)=-2a s-b t.

The matrix of these values on the coordinate column (s,t)^T is

    A=[[b,2c],[-2a,-b]], A^2=(b^2-4ac) I.

With coefficient columns for the basis (s,t), the operator matrix is
A^T. This transpose convention has no effect on the characteristic
polynomial or any support conclusion, but specifying the convention
avoids confusing point-coordinate and coefficient-coordinate matrices.

Put Delta=b^2-4ac. If Delta!=0, A has eigenvalues lambda,-lambda with
lambda^2=Delta. Its induced action on degree n forms has eigenvalues
(n-2i)lambda, for 0<=i<=n. For n=8 this gives

    char(D_H;mu)
      =mu (mu^2-4Delta)(mu^2-16Delta)
           (mu^2-36Delta)(mu^2-64Delta).                  (D)

Both sides are polynomial in a,b,c, so equality on Delta!=0 proves
the polynomial identity everywhere. Alternatively, if Delta=0 and
H!=0, an invertible linear coordinate change takes H to a nonzero
multiple of s^2, for which D_H is a nonzero multiple of s partial_t.
That action is nilpotent, has characteristic polynomial mu^9, and
has kernel spanned by s^8. Thus the repeated-root locus is retained;
it permits exactly the single-root support that (A) requires.

For H=z^2+vz+w and F(z)=sum_(i=0)^8 c_i z^i, homogenize with
z=t/s. Formula (B) becomes

    8(v+2z)F(z)-2(z^2+vz+w)F'(z).

Its z^9 terms cancel, and its degree-i coefficient is exactly

    d_i=(8-2i)v c_i+(18-2i)c_(i-1)-2(i+1)w c_(i+1),
    c_(-1)=c_9=0.                                        (E)

Thus equation (7) of the proposal is correct for any supplied octic
coefficient vector in this same coordinate. It does not validate the
geometric provenance of that coefficient vector.

## 3. Projective stabilizer rank test: independently proved

For F!=0 of degree n>=1, consider the four coefficient columns

    F, (s partial_s-t partial_t)F, s partial_t F, t partial_s F.

Their rank is at most three if and only if some nonzero element X of
sl2 acts by X(F)=mu F. A dependence cannot use only the first column,
since F!=0. Conversely such an eigenrelation is a dependence. The last
three operators form a basis of sl2 over characteristic zero.

The projective vector field induced by a nonzero X is nonzero and is a
global section of T_(P1)=O_(P1)(2). In a finite chart it is a polynomial
of degree at most two times partial_x; its projective zero divisor has
degree two. The same root-valuation argument used in section 1 forces
every root of F to lie in this divisor. Hence F has at most two distinct
projective roots. Conversely, if the support of F has one or two
points, choose a nonzero quadratic H vanishing on these points. Section
2 gives D_H F=mu F, supplying the dependence. Therefore

    rank[F | (s partial_s-t partial_t)F |
               s partial_t F | t partial_s F]<=3
       iff F has at most two distinct projective roots.   (F)

This proof also covers n=1,2, when the rank inequality is automatic and
the root bound is automatic. No assertion about a reduced determinantal
scheme or about stabilizers in positive characteristic is needed.

## 4. Unified Jbar/A4 allowance: independently proved

Let H be a nonzero quadratic, P a nonzero linear form, F a nonzero octic,
and j the actual Jbar scalar. Then the conditional support requirement

    j!=0: supp(F) contained in supp(H);
    j=0:  supp(F) contained in supp(HP)

is equivalent, on k-valued points, to existence of L_1 in Sym^1 and
mu in k satisfying

    D_(HP) F=L_1 F,
    j D_H F=mu F.                                        (G)

If j!=0, the second equation is (C) with eigenvalue mu/j. It forces
support in H, which also lies in HP; the first equation follows from
section 1. If j=0, F!=0 forces mu=0, and the first equation is exactly
the degree-three case of (A), allowing HP. This includes P equal to a
root of H, repeated H, and P at infinity. No disjoint-root hypothesis or
root-partition enumeration is required.

One can also remove the auxiliary quotient variables without choosing
roots: the first equation says that the degree-nine coefficient vector
of D_(HP)F lies in the span of the independent vectors sF,tF. Thus it is
equivalent on F!=0 to rank[sF | tF | D_(HP)F]<=2, together with
rank[F | j D_HF]<=1. These fixed-size matrix conditions retain the same
conditional support statement. They add no conductor-descent result.

All assertions above concern geometric points and a polynomial
incidence presenting them. They do not identify that incidence with a
reduced scheme, nor claim that an underlying-support condition over an
arbitrary nonreduced parameter base is equivalent to those equations.
For example, over k[epsilon]/(epsilon^2), F=s^2+epsilon t^2 and H=s^2
have the same underlying support, but D_H F=-4epsilon st is not a
scalar multiple of F. This distinction is harmless for the stated
characteristic-zero geometric-point criterion and should be preserved
in subsequent elimination or closure language.

There is a separate witness-lifting caveat for (F). Over the same ring,
let F=s^n+epsilon t^n with n>=3. Subtracting nF from the second column
of the stabilizer matrix leaves that column divisible by epsilon;
the third column is also divisible by epsilon. Thus all four-by-four
minors vanish. But D_H F=mu F for H=a s^2+b st+c t^2 forces

    mu=n b, c=0, epsilon a=0, 2n epsilon b=0.

Every coefficient of H is then in (epsilon), so no such H defines an
R-valued point of the projective quadratic space. This example forbids
promoting the field-valued determinantal criterion to a witness-lifting
statement over arbitrary bases. It does not by itself show that the
determinantal ideal is nonradical.

## 5. New coordinate-binding gap in attempt02/attempt04

This gap is independent of sections 1--4 and their proofs. The finite
monic quadratic cover is explicitly defined with

    z=r/delta, H_z(z)=z^2+vz+w

in section 1 and section 3 of the
[accepted homogeneous-gcd audit](2026-10-13-session-nonendpoint-homogeneous-gcd-rank-and-cover-independent-audit.md).
The actual primitive conductor polynomial is F_p(p), with

    r0=delta/p,
    Pt(p)=p^3 P(delta/p)/delta^3

in sections 2 and 4 of the
[accepted diagonal-norm note](2026-10-12-session-nonendpoint-diagonal-norm-identity.md).
Combining these definitions gives p=1/z on their common finite chart.
It does not give p=1-z. The latter relation uses the target normalization
coordinate z_target=1-p, which is a different coordinate from r/delta.

The
[attempt02 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt02.m2)
uses the correct cover parameter substitutions but sends its final
primitive-polynomial variable p to 1-zPar. Thus its saved coefficients
are coefficients of a different transformed form. The
[attempt04 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt04.m2)
correctly applies formula (E) to that saved vector and its
[execution record](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
records exit zero. Exact postprocessing cannot repair the wrong
coordinate binding. Consequently its 9-by-2 matrix must not be cited
as the actual finite-h2 conductor-support matrix.

The corrected homogeneous conductor in the z chart is

    F_z(z)=z^8 F_p(1/z),                                  (H)

after the same actual parameter substitutions. If F_p=sum f_i p^i,
its z coefficients are f_(8-i). Formula (H) is homogeneous coordinate
interchange, so no division by z is needed in the final octic. It keeps
all degree drops: p=0 maps to z=infinity and p=infinity maps to z=0.
The intrinsic A4 allowance p=0 is therefore the linear form s when
z=t/s. Equivalently, in p coordinates the allowed quadratic is
H_p(p)=1+vp+wp^2, and the A4 allowance is p=0. Either choice is valid
provided both the actual conductor and all allowed forms use it.

This audit records the required correction; the shared-incidence
worker owns the corrected capture. No corrected capture, rank-locus
emptiness or geometry of its surviving points is asserted here.

## 6. Localization and acceptance boundary

The abstract criteria need F,H,P nonzero. If any is zero, its divisor
or the support criterion used here is undefined or changes meaning;
matrix minors alone may then vanish for an irrelevant reason. The
original geometric zero-form stratum remains a separate obligation.

The rational finite-h2 cover also retains its original determinant
open condition, exact-gcd cofactor condition, actual projection-center
avoidance, and any other accepted geometric hypotheses. A normalized
polynomial coefficient vector obtained by clearing denominators and
removing common parameter content represents the actual conductor only
where the resulting scalar comparison is a unit and the original
conductor is nonzero. On denominator or content boundaries, a
specialized primitive extension or the closure of the rational map
cannot replace the original coefficient equations. In particular,
the original four linear cover equations are the correct data for
retaining the repeated-root determinant boundary; the homogeneous
general criterion itself excludes no such boundary.

Accepted new mathematics from this audit consists of (A)--(G), with
their nonzero and characteristic-zero hypotheses. The coordinate
correction (H) follows directly from the accepted coordinate
definitions. The quintic application remains a necessary support
incidence, still requiring its correctly bound actual coefficients,
all original geometric conditions, and the full nonlinear conductor
descent conditions. There is no new global quintic, C0, or STCI
conclusion.
