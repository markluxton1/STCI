# Arithmetic descent beyond binomial carriers

Date: 2026-10-29. Investigator: `arithmetic`. **Status: independently
reviewed provisional research.** The [independent review and constructive
addendum](2026-10-29-arithmetic-beyond-binomial-audit.md) check the source,
higher-jet obstruction, explicit mates and conductor calculation.
The [separate explicit-mate audit](2026-10-29-arithmetic-explicit-mate-audit.md)
independently reconstructs the positive result and checks the literal
four-variable forms by Macaulay2 at primes 43 and 53.
No canonical result/question is changed. The unrestricted characteristic-
zero STCI question for
\(C_0=[s^4:s^3t:st^3:t^4]\) remains open.

The output is a uniform degree-growth obstruction on a specified larger
source, together with explicit positive-characteristic pairs on a genuinely
non-binomial carrier. This goes beyond the one-binomial class in the
[earlier arithmetic search](2026-10-28-stci-search-arithmetic.md), without
claiming an exhaustive reduction of arbitrary carriers.

## 1. A specified twenty-three-parameter source

On \(\mathbf P^2_{s:t:z}\), put
\[
\begin{aligned}
 U_0&=s^4+s^2zL_0,&U_1&=s^3t+s^2zL_1,\\
 U_2&=st^3+\alpha z^4+szC_2,&U_3&=t^4+zB_3,
\end{aligned}\tag{1}
\]
where \(\alpha\ne0\), \(L_0,L_1\) are arbitrary linear forms,
\(C_2\) an arbitrary quadratic, and \(B_3\) an arbitrary cubic.
There are \(1+3+3+6+10=23\) scalar parameters. Every system restricts
on \(c=(z=0)\) to literal \(C_0\). This enlarges the inherited
eleven-parameter family by varying both formerly fixed coordinates and
the transverse terms of the third.

Retain basepoint-free systems with **full** reduced inverse support of
\(C_0\) equal to \(c\). Basepoint freeness makes the map finite onto
its integral image because its pullback of \(\mathcal O(1)\) is the
ample \(\mathcal O_{\mathbf P^2}(4)\). Birationality is separate;
when present the image has degree sixteen and the map is its normalization.
The admissible locus of this enlarged source is not classified here, and
a generic member is not asserted admissible.

The family is nonempty: \(L_0=L_1=C_2=0\),
\(\alpha=1,B_3=s^3\) gives the inherited finite birational map
\[
U=(s^4,s^3t,st^3+z^4,t^4+s^3z).\tag{2}
\]
Its full singleton support and degree-sixteen image are recorded in
[R-0017](../results/singleton_plane_conductor_descent.md) and its cited
evidence. Those accepted characteristic-zero proofs are inputs, not
replayed computations. The same literal map works in every characteristic:
on \(s\ne0\) its inverse uses \(t/s=X_1/X_0\) and
\(z/s=X_3/X_0-(X_1/X_0)^4\); on \(s=0\), membership in \(C_0\)
forces \(z=0\). These formulas do not divide by a characteristic.

## 2. Higher jets turn descent failure into degree divisibility

**Jet-gap lemma.** Let \(A\) be a target local ring inside a source
DVR with uniformizer \(r\) and residue field \(E\). Suppose that,
modulo \(r^e\), \(e\ge2\), every element of \(A\) has the form
\(R(w)\), where \(R\in k(W)\) and the residue \(w_0\) is
transcendental over \(k\). Let
\[
q=c+ar+O(r^2),\qquad c\in k^*,\quad a\in E^*.
\]
If \(q^b\in A\), for \(b>0\), then characteristic zero is
impossible; in characteristic \(p>0\), necessarily
\[
\boxed{p^{v_p(b)}\ge e.}\tag{3}
\]

The residue of \(R(w)=q^b\bmod r^e\) is \(c^b\). Injectivity
of \(k(W)\to E\) forces \(R(W)=c^b\), so the whole jet must be
constant. In characteristic zero its coefficient of \(r\) is
\(bc^{b-1}a\ne0\). In characteristic \(p\), write
\(b=p^vn\), \(p\nmid n\). Frobenius gives the first nonconstant
term \(nc^{b-p^v}a^{p^v}r^{p^v}\), with nonzero coefficient. This
proves (3). Localized denominators are allowed: a denominator with nonzero
residue is invertible modulo \(r^e\). Ordinary differentiation detects
only \(p\mid b\); the first surviving Hasse order records the necessary
\(p\)-power.

Apply this at \(D=(s=0)\), using \(z=1\), \(r=s/z,y=t/z\) and
the target frame \(X_2\). Put
\(u=U_2=\alpha+r[y^3+C_2(r,y,1)]\). The coordinates
\(U_0/u,U_1/u\) vanish modulo \(r^2\), while
\[
w=U_3/u,\quad w_0=\frac{y^4+B_3(0,y,1)}\alpha,\quad q=1/u.
\]
The element \(w_0\) is transcendental: its numerator has degree exactly
four in \(y\). The linear coefficient of \(q\) is
\(-\alpha^{-2}[y^3+C_2(0,y,1)]\ne0\), since the quadratic term
has degree at most two. The target local ring at the image line reduces
modulo \(r^2\) to rational functions of \(w\), with the denominator
check in the lemma.

A sole-support mate \(G_b\) pulls back to
\(G_b(U)=\lambda z^{4b}\), \(\lambda\ne0\), by full inverse
support and unique factorization. Division by \(\lambda U_2^b\)
forces \(q^b\) to descend. Every retained member of (1) therefore has
no characteristic-zero mate and, in characteristic \(p>0\), every mate
satisfies
\[
\boxed{p\mid b.}\tag{4}
\]
Neither equation has a binomial hypothesis. On the sublocus
\(L_0=l_0s,L_1=l_1s\), the first two target coordinates vanish
modulo \(r^3\), strengthening (3) to \(p^{v_p(b)}\ge3\), in
particular \(4\mid b\) in characteristic two. For a birational
degree-sixteen image, \(m_C=4b\); thus \(p\mid m_C\) for every odd
prime, and \(\max(16,b)\ge p\).

## 3. A carrier admitting no binomial relation

For (2), set
\[
A=x_0^3x_3-x_1^4,\quad B=x_0^2x_2-x_1^3,\quad
F=A^4-x_0^{13}B.\tag{5}
\]
Its image is the integral degree-sixteen surface \(X=V(F)\), and
\[
A(U)=s^{15}z,\qquad B(U)=s^8z^4.\tag{6}
\]
The polynomial \(F\) is primitive and linear in \(x_2\), with
coefficient \(-x_0^{15}\). Its constant coefficient is not divisible
by \(x_0\), since at \(x_0=0\) it is \(x_1^{16}\). Hence it is
irreducible in every characteristic.

The image lies on **no nonzero homogeneous binomial hypersurface**.
The source polynomials \(st^3+z^4\) and \(t^4+s^3z\) are distinct
irreducibles: each is primitive linear in one variable, with coprime
coefficients in the polynomial ring of the other two. They are not
associates of \(s\) or \(t\). In a relation \(U^a=cU^b\), unique
factorization forces equal exponents of \(U_2,U_3\); the \(t\)-
exponents then force equality for \(U_1\), and the \(s\)-exponents
force equality for \(U_0\). Only the trivial relation remains.

This proves that the carrier itself is genuinely non-binomial. A
binomial containing \(C_0\) need not contain \(X\), so this argument
alone does not exclude binomial mates. The explicit mates below are
proved non-binomial separately.

## 4. Explicit degree-p mates and exact minimum for p at least 43

Let \(p\ge43\) be prime. Set
\[
r\equiv3p\pmod4,\quad0\le r<4,\qquad
n=(3p-r)/4,\qquad E=(p-3r)/4.
\]
Here \(r=1\) or \(3\), and \(E\ge9\). For \(j=4h+\ell\),
\(0\le\ell<4\), define
\[
P_p=x_1^r\sum_{j=0}^{n}(-1)^j\binom nj
x_0^{E+h-3\ell}x_3^{n-j}B^hA^\ell,
\qquad G_p=x_2^p-P_p.\tag{7}
\]
All exponents are nonnegative because \(E+h-3\ell\ge E-9\ge0\).
Each summand has ordinary degree \(p\). The bound \(E\ge9\) holds
for primes \(p\equiv3\pmod4\) at \(p\ge43\), and for
\(p\equiv1\pmod4\) at \(p\ge53\); the only primes from 43 to 52
are 43 and 47. Thus (7) covers every prime at least 43.

In \((k[x]/(F))_{x_0}\), the identities
\(x_1^4=x_0^3x_3-A\) and \(A^4=x_0^{13}B\) give
\[
\frac{x_1^{3p}}{x_0^{2p}}
=\frac{x_1^r(x_0^3x_3-A)^n}{x_0^{2p}}=P_p.\tag{8}
\]
For \(j=4h+\ell\), the exponent of \(x_0\) after replacing
\(A^{4h}\) is \(3(n-j)-2p+13h=E+h-3\ell\), as in (7).
Pullback gives \(P_p(U)=s^pt^{3p}\), initially on \(s\ne0\),
then as a polynomial identity. Frobenius therefore gives
\[
\boxed{G_p(U)=(st^3+z^4)^p-s^pt^{3p}=z^{4p}.}\tag{9}
\]
The form \(G_p\) does not vanish identically on \(X\). The finite
surjective map and full singleton inverse support prove
\[
V(F,G_p)_{\rm red}=C_0,\qquad [V(F,G_p)]=4p[C_0].\tag{10}
\]
Thus the actual pair is proper and has degrees \((16,p)\).

Both equations are non-binomial. Every term of \(P_p\) is divisible
by \(x_1^r\), with \(r>0\), so \(G_p\) has the pure monomial
\(x_2^p\) with coefficient one. If \(G_p\) were a binomial
\(x_2^p-cM\), (9) would force \(cM(U)=s^pt^{3p}\).
Unique factorization forces the \(x_2,x_3\) exponents of \(M\) to
vanish, because \(U_2,U_3\) are irreducibles distinct from \(s,t\).
Writing \(M=x_0^ax_1^b\), its pullback is
\(s^{4a+3b}t^b\). Hence \(b=3p\), impossible for a
degree-\(p\) monomial. Thus \(G_p\)
is not binomial. This is a literal two-non-binomial construction.

Combining (4) and (9), the minimum positive mate degree on this
particular non-binomial carrier is exactly
\[
\boxed{b_{\min}(p)=p\qquad(p\ge43).}\tag{11}
\]
The minimum maximum defining degree in (1), restricted to birational
admissible members, is also exactly \(p\) for \(p\ge43\): (4) is
the lower bound and (2),(7) attain it. This is a restricted-source
minimum, not the unrestricted \(\delta(p)\).

The dependency-free [exact verifier](../computations/stci_arithmetic_beyond_2026_10_29.py)
checks homogeneity, nonnegative exponents and sparse polynomial pullbacks
at \(p=43,47,53,59,61,101\). Its
[saved output](../computations/stci_arithmetic_beyond_2026_10_29.json)
records every input. Run
`python3 research/computations/stci_arithmetic_beyond_2026_10_29.py`.
These are finite controls; the uniform proof is (8)--(9).

## 5. Conductor interpretation and the remaining interface

For (2), normalization is an isomorphism off \(D=(s=0)\). Finite
duality identifies its conductor upstairs with
\(\omega_{\mathbf P^2}\otimes\nu^*\omega_X^{-1}\), since \(X\)
is a hypersurface and hence Gorenstein. The finite-duality input is
[Stacks, Lemma 48.11.4](https://stacks.math.columbia.edu/tag/0AX2);
the hypersurface calculation is given in
[de Jong's lecture notes, Lemma 1.2](https://www.math.columbia.edu/~dejong/courses/schemes-spring-2020/lecture-notes-b.pdf).
Locally the conductor identification follows because
\(\operatorname{Hom}_A(B,A)\) consists of multiplication by common-
fraction-field elements carrying \(B\) into \(A\).

Here \(\omega_X=\mathcal O_X(12)\), so the conductor ideal has
class \(\mathcal O(-3-48)=\mathcal O(-51)\). Being invertible and
supported on the single line \(D\), it is exactly
\(\mathcal O(-51D)\). With \(Q=z^4\) and
\(Q-U_2=-st^3\), every Frobenius power \(q=p^e\ge51\) has
\(Q^q-U_2^q\) in the conductor twisted by \(\mathcal O(4q)\).
Hence \(Q^q\) descends to a global section of \(\mathcal O_X(q)\),
which lifts to an ambient degree-\(q\) form by the hypersurface sequence
and \(H^1(\mathbf P^3,\mathcal O(q-16))=0\). This independently
explains how Frobenius removes the nilpotent defect, with the weaker
large-prime threshold 53. Formula (7) supplies threshold 43 without
depending on this duality calculation.

To force unrestricted \(\delta(p)\to\infty\), one still needs an
obstruction for every possible carrier/pair, or a valid reduction to
sources with a gap such as (3). This note proves neither. Arbitrary
normalizations may have nonconstant reduced phases, multiple inverse
branches, or no suitable boundary gap. The concrete advance is a
restricted-source growing lower bound, attained by explicit pairs whose
two equations are non-binomial, and a first surviving Hasse order that
retains the characteristic power invisible to ordinary differentiation.
