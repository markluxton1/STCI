# Independent audit: fixed quadric boundary despite large lifting freedom

October 30, 2026. Reviewer: line_audit, independently reconstructing the
root proposal. The source containment, cycle inequality, dimensions and
equal-degree pencil test were also checked by the separate child reviewer
weighted_family_local_check.

**Verdict: PASS for the stated family, the strengthened residual cycle
floor, and the necessary global triangular-row condition.** These are
reviewed provisional deductions, not canonical promotion or a general
STCI nonexistence theorem.

The audited proposal is
[the quadric-boundary construction and obstruction](2026-10-30-stci-game-quadric-boundary.md).
The independently reviewed
[equation-freedom formula](2026-10-28-stci-search-freedom.md) and its
[proof audit](2026-10-28-stci-search-freedom-independent-audit.md)
are used as premises. Their inherited proof and computations were not
rerun.

## Literal hypotheses and the fixed-factor input

Work over an algebraically closed characteristic-zero field, with
\[
C=C_0=[s^4:s^3t:st^3:t^4],\qquad Q=(q=0),\qquad
q=x_0x_3-x_1x_2.
\]
Fix \(m\ge1\), set \(d=3m+2\), and choose an actual cubic
\(H\in H^0(\mathcal I_C(3))\) with \(q\nmid H\). Let
\[
V_{e,r}=H^0(\mathbf P^3,\mathcal I_C^r(e)),\qquad
W_H=H^mS_2+V_{d,m+1}.
\]
The powers are ideal sheaf powers, equivalently saturated homogeneous
powers. No equality with unsaturated ordinary powers is assumed.

The reviewed fixed-factor identity applies with order \(m+1\) and degree
\(3m+2\), and gives the stronger equality
\[
V_{3m+2,m+1}=q\,V_{3m,m}.
\tag{1}
\]
This is an identity of actual homogeneous global equation spaces.
Consequently
\[
W_H\subset(q,H^m).
\tag{2}
\]
The conclusion is not based on a generic symbol or a formal normal
coordinate calculation.

## The residual is genuine, including its multiplicity

On \(Q\simeq\mathbf P^1\times\mathbf P^1\), the nonzero restriction
\(H|_Q\) has class \((3,3)\). It contains \(C\), whose class is
\((1,3)\), exactly once: a second copy would leave class \((1,-3)\),
which has no effective divisor. Thus
\[
\operatorname{div}_Q(H)=C+R_H,\qquad [R_H]=(2,0),\qquad\deg R_H=2.
\]
The effective residual \(R_H\) is a pair of ruling lines or a doubled
ruling line. It has no component equal to \(C\). In particular a doubled
line is retained as a nonreduced degree-two cycle; its reduced support
has degree one, which must not be confused with the cycle degree.

Because \(q\nmid H\), the forms \(q,H^m\) are a regular sequence and
define a complete-intersection curve with cycle
\[
[V(q,H^m)]=m[C]+mR_H.
\]
For any proper pair \(F,G\in W_H\), (2) gives
\[
(F,G)\subset(q,H^m),\qquad
V(q,H^m)\subset V(F,G)
\]
scheme-theoretically. Localizing at the generic point of each ruling
component gives a surjection of Artinian quotient rings. Its length
comparison proves a coefficientwise inequality, not merely set
containment:
\[
R\ge mR_H,\qquad \boxed{\deg R\ge2m},
\tag{3}
\]
where \([V(F,G)]=m_C[C]+R\). If \(R_H=2L\), (3) reads
\(R\ge2m[L]\). If the pair is improper, it already cannot cut out
only \(C\). Hence no two members of the entire stated source can form
a sole-support pair.

This verifies the stronger uniform floor, beyond the proposal's original
set-theoretic degree-two boundary observation. The global higher-order
corrections all vanish on \(Q\), so they cannot repair this fixed
residual restriction.

## The coefficient dimensions are exact, with the correct denominator

The cubic has generic normal order exactly one. One can see this directly
from the simple \(C\) component of \(H|_Q\). Its leading symbol is
therefore nonzero at the generic point of \(C\). For a quadratic \(f_2\),
the order of \(H^mf_2\) increases from \(m\) precisely when
\(f_2|_C=0\), and \(H^0(\mathcal I_C(2))=kq\). It follows that
\[
H^mS_2\cap V_{d,m+1}=k\,qH^m.
\]
Multiplication by the nonzero polynomial \(H^m\) is injective. Using the
reviewed source formula
\[
D(m)=\frac{5m^3+15m^2+16m+6}{6},\qquad
\dim V_{d,m+1}=D(m),
\]
gives
\[
\dim W_H=D(m)+9.
\]
The reviewed surjective order-\(m\) symbol map at \(d=3m+2\) gives
\[
\dim V_{d,m}
=D(m)+(m+1)(5m+9).
\]
Thus the relative dimension tends to one, with codimension exactly
\(5m^2+14m\). The denominator is the **order-\(m\) equation space**
\(V_{d,m}\). Relative to all degree-\(d\) forms \(S_d\), the limiting
fraction is \(5/27\), not one. The near-one ratio does not say that
\(W_H\) contains a generic element of \(V_{d,m}\) or is exhaustive.

The comparison with the weighted-subalgebra family is also correct when
its own denominator is stated: at degree \(3m\), its dimension is
asymptotic to \(m^2/4\), while
\(\dim V_{3m,m}=D(m)\sim5m^3/6\). That relative fraction is
\(3/(10m)\), tending to zero.

The fixed-boundary obstruction is not vacuous through an absence of
proper pairs. The linear space \(W_H\) has no fixed surface factor:
it contains \(H^mS_2\) and \(q^{m+1}S_m\), whose common divisorial
factor is one because \(\gcd(H,q)=1\). For a fixed nonzero row, avoiding
its finitely many irreducible factors is a nonempty open condition on
the other row. Thus proper pairs exist. One can simultaneously take
their two quadratic classes independent in \(S_2/kq\); then every
nonzero scalar pencil member still has exact normal order \(m\).
The boundary obstruction persists even on that locus.

## The global triangular-row restriction

Let actual \(F_a,G_b\) form a hypothetical sole-support pair, with
\(a\le b\). For any actual homogeneous polynomial \(P\in S_{b-a}\)
and any nonzero scalar \(\lambda\), the replacement
\[
G'_b=\lambda G_b+PF_a
\]
preserves the homogeneous ideal together with \(F_a\). This new row
cannot be zero, since that would make the original pair improper.
Its generic normal order must satisfy
\[
\operatorname{ord}_C(G'_b)\le\lfloor b/3\rfloor.
\tag{4}
\]
If its order were larger, the reviewed global fixed-factor theorem would
force \(q\mid G'_b\) (or no nonzero form could have that order at all).
Then \(V(q,F_a)\) would be contained in the sole-support intersection.
The partner \(F_a\) cannot also be a multiple of \(q\), which would
retain a surface component. Otherwise \(F_a|_Q\) is a nonzero section
of \(\mathcal O_Q(a,a)\). Sole support would force its divisor to be
supported on \(C\), hence to have class \(e(1,3)\). Equality with
\((a,a)\) is impossible for \(a>0\). This proves (4).

For equal degrees, the same argument covers every nonzero scalar pencil
member, including the individual original rows. Thus the pencil claim
passes without assuming irreducibility of either row.

The restriction concerns actual homogeneous global row operations with
invertible determinant. Formal cancellation over \(k(C)\) can use poles
and does not supply such an operation. In the present failed family,
\(f_2G-g_2F\) has a factor \(q\), but the coefficient matrix of this
replacement has determinant \(f_2\), which is not a global unit. It
does not preserve the original homogeneous ideal. This explains why
the fixed-boundary proof is a substantive additional obstruction and
why the necessary row test is not sufficient.

## General quadric restriction interface

The proposal's additional necessary condition also passes. For actual
forms not divisible by \(q\), write their exact restrictions as divisors
\[
F_a|_Q=uC+A_Q,\qquad G_b|_Q=vC+B_Q,
\]
with neither residual divisor containing \(C\). Their classes are
\[
[A_Q]=(a-u,a-3u),\qquad [B_Q]=(b-v,b-3v).
\]
Any common residual curve would lie outside \(C\) and violate sole
support. With no common component, their intersection degree is
\[
(a-u)(b-3v)+(a-3u)(b-v).
\]
Sole support requires the entire intersection support to lie on \(C\).
The orders \(u,v\) here are orders inside \(Q\), which need not equal
the ambient normal orders. This is a precise remaining global incidence,
not a solved concentration bound or an existence claim.

## Review outcome and limitations

The proposed failed construction and obstruction are uniform in \(m\)
and all coefficients in the same fixed-\(H\) source, including reducible
\(H\) and doubled residual rulings. The dimensions retain sheaf powers
and use the reviewed source formula as a premise. Properness is retained
for the cycle floor, and a proper locus exists. The global row filter
is necessary for every actual hypothetical pair, while its formal-to-global
bridge remains explicitly unproved.

These statements provide proactive nonexistence principles: higher-order
freedom can leave a fixed global boundary unchanged, and every allowable
global triangular representative must stay below its forced-factor
threshold. They neither exhaust arbitrary global pairs nor establish a
universal residual floor. No canonical result/question record is changed.
