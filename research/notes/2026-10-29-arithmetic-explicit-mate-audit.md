# Independent audit: explicit mates on the non-binomial degree-sixteen carrier

Date: 2026-10-29. Reviewer: `arithmetic/explicit_mate_audit`.

**Verdict: PASS for Sections 3--5 of the [arithmetic proposal](2026-10-29-arithmetic-beyond-binomial.md).**
The explicit degree-\(p\) mates exist for every prime \(p\ge43\),
both displayed equations are non-binomial, and the claimed restricted
minimum equals \(p\), using the separately audited jet-gap lower bound.
The optional conductor calculation \(\mathcal O(-51D)\) is also valid.
These are reviewed provisional claims. This audit promotes no canonical
record and makes no unrestricted lower-bound claim for \(\delta(p)\).

## Scope and reconstruction of the actual map

Work over an algebraically closed field of arbitrary characteristic with
\[
U=(s^4,s^3t,st^3+z^4,t^4+s^3z),\quad
A=x_0^3x_3-x_1^4,\quad B=x_0^2x_2-x_1^3,\quad
F=A^4-x_0^{13}B.
\]
The map has no basepoint: \(s\ne0\) is handled by \(U_0\), and
at \(s=0\) the remaining two coordinates are \(z^4,t^4\).
Its ample pullback \(\mathcal O(4)\) implies finiteness onto its
image. On \(s\ne0\), coordinates \(x=t/s,n=z/s\) map to
\((x,x^3+n^4,x^4+n)\), giving an explicit inverse on the image.
Thus this is a finite birational normalization in every characteristic.

Direct substitution gives \(A(U)=s^{15}z\), \(B(U)=s^8z^4\),
and hence \(F(U)=0\). The polynomial \(F\) is primitive linear in
\(x_2\): its coefficient is \(-x_0^{15}\), while its constant
coefficient restricts to \(x_1^{16}\) at \(x_0=0\). These
coefficients are coprime. Gauss's lemma proves irreducibility in every
characteristic, so the integral image is exactly \(V(F)\), of degree
sixteen. The explicit inverse also proves that the normalization is an
isomorphism off \(D=(s=0)\).

The full inverse support of literal \(C_0\) is \(c=(z=0)\).
On \(s\ne0\), membership in its affine graph requires \(n^4=0\)
and \(n=0\), hence \(n=0\). At \(s=0\), the image
\([0:0:z^4:t^4]\) belongs to \(C_0\) only when \(z=0\).
This includes all boundary points and uses no separability assumption.
These characteristic-independent checks justify extending the inherited
characteristic-zero model to every positive characteristic; they do not
reopen its accepted characteristic-zero exclusion.

## Independent uniform verification of the mate formula

For prime \(p\ge43\), put
\(r=3p\bmod4\), \(n=(3p-r)/4\), \(E=(p-3r)/4\).
For \(j=4h+\ell\), \(0\le\ell<4\), the proposed polynomial is
\[
P_p=x_1^r\sum_{j=0}^{n}(-1)^j\binom nj
x_0^{E+h-3\ell}x_3^{n-j}B^hA^\ell,
\qquad G_p=x_2^p-P_p.
\]
The parameter split is exhaustive. If \(p\equiv3\pmod4\), then
\(r=1,E=(p-3)/4\ge10\). If \(p\equiv1\pmod4\), the smallest
such prime at least 43 is 53, and \(r=3,E=(p-9)/4\ge11\).
Thus every exponent \(E+h-3\ell\) is nonnegative. The degree of a
summand is
\[
r+E+h-3\ell+n-4h-\ell+3h+4\ell=r+E+n=p.
\]
In the localization of the hypersurface ring at \(x_0\), expand
\[
x_1^{3p}/x_0^{2p}
=x_1^r(x_0^3x_3-A)^n/x_0^{2p}.
\]
For each \(j=4h+\ell\), replace \(A^{4h}\) using
\(A^4=x_0^{13}B\). The resulting exponent of \(x_0\) is
\(3(n-j)-2p+13h=E+h-3\ell\). This reconstructs exactly \(P_p\).
Pulling back to the source yields \(P_p(U)=s^pt^{3p}\), first on
\(s\ne0\), hence globally as a polynomial identity. Frobenius gives
\[
G_p(U)=(st^3+z^4)^p-s^pt^{3p}=z^{4p}.
\]
Therefore \(G_p\) is not zero on \(X\); irreducibility of \(F\)
proves properness. Finiteness, surjectivity and the full inverse-support
calculation prove \(V(F,G_p)_{\rm red}=C_0\). Degree exhaustion gives
the cycle \(4p[C_0]\). The proof is uniform in \(p\), rather than an
inference from finitely many characteristics. The threshold 43 is
sufficient; optimality of that threshold is not asserted.

## Both equations and the restricted minimum

The two source polynomials \(U_2=st^3+z^4\),
\(U_3=t^4+s^3z\) are distinct irreducibles in every characteristic:
use primitive linearity in \(s\) and \(z\), respectively. They are
not associates of \(s,t\). Unique factorization in a putative relation
\(U^a=cU^b\) forces equal \(U_2,U_3\) exponents, then equal
\(U_1\) exponents by the \(t\)-order, then equal \(U_0\)
exponents by the \(s\)-order. Thus the image admits no nonzero
binomial relation, in particular its defining equation is non-binomial.

For the mate, every summand of \(P_p\) is divisible by \(x_1^r\),
\(r>0\), so \(G_p\) has a pure \(x_2^p\) term. If it were
binomial, it would have the form \(x_2^p-cM\). Its pullback identity
would force \(cM(U)=s^pt^{3p}\). The \(U_2,U_3\) factors must
therefore have exponent zero; writing \(M=x_0^ax_1^b\), comparison
of \(t\)-orders forces \(b=3p\), incompatible with \(\deg M=p\).
This independently proves that the displayed pair has two non-binomial
equations. It does not infer that every possible mate is non-binomial.

The initial [jet-gap audit](2026-10-29-arithmetic-beyond-binomial-audit.md)
proves \(p\mid b\) for every mate on every admissible member of the
literal twenty-three-parameter source. Applying it to this carrier gives
\(b\ge p\). The constructed mate attains \(p\), proving its minimum
mate degree equals \(p\). All birational members have degree sixteen;
therefore the restricted-source minimum of the maximum degree also equals
\(p\) for \(p\ge43\). This has no implication in the required
direction for the all-carrier minimum \(\delta(p)\).

## Independent computer controls

The reviewer inspected the dependency-free sparse verifier and ran a
separate direct Macaulay2 polynomial substitution at \(p=43,53\). The
first attempt had a print-format error after the first algebraic checks;
the corrected run exited successfully with

```text
PASS independent M2 prime=43 degree={43}
PASS independent M2 prime=53 degree={53}
```

The direct check constructs \(P_p\) in four target variables before
substituting the four source polynomials; it does not use the sparse
verifier's reduced \(A(U),B(U)\) monomial formulas. The exact check is:

```macaulay2
scan({43,53}, p -> (
 R=(ZZ/p)[s,t,z]; T=(ZZ/p)[x0,x1,x2,x3];
 A=x0^3*x3-x1^4; B=x0^2*x2-x1^3;
 r=(3*p)%4; n=(3*p-r)//4; E=(p-3*r)//4;
 P=x1^r*sum(0..n,j->(
   h=j//4; ell=j%4;
   (-1)^j*binomial(n,j)*x0^(E+h-3*ell)*x3^(n-j)*B^h*A^ell));
 G=x2^p-P;
 phi=map(R,T,{s^4,s^3*t,s*t^3+z^4,t^4+s^3*z});
 assert(phi G==z^(4*p)); assert(degree G=={p});
 assert(phi(A^4-x0^13*B)==0);
 print("PASS independent M2 prime="|toString p|" degree="|toString degree G);
));
```

The durable [Python verifier](../computations/stci_arithmetic_beyond_2026_10_29.py)
and [saved output](../computations/stci_arithmetic_beyond_2026_10_29.json)
provide additional exact controls at six primes. None substitutes for the
uniform identity above.

## Independent conductor calculation

Let \(\mathfrak c\) denote the conductor upstairs. For a finite
birational inclusion \(A\subset B\), every \(A\)-linear map
\(B\to A\) becomes multiplication by an element of the common fraction
field; the condition that its image lie in \(A\) is exactly the conductor
condition. Thus \(\operatorname{Hom}_A(B,A)=\mathfrak c\) as a
\(B\)-module. Finite duality, in the form of
[Stacks, Lemma 48.11.4](https://stacks.math.columbia.edu/tag/0AX2),
identifies \(\omega_B\) with \(\operatorname{Hom}_A(B,\omega_A)\)
here, because source and target are Cohen--Macaulay of dimension two.
The target is Gorenstein, so
\[
\mathfrak c\simeq
\omega_{\mathbf P^2}\otimes\nu^*\omega_X^{-1}
\simeq\mathcal O_{\mathbf P^2}(-3-4(16-4))=\mathcal O(-51).
\]
The hypersurface formula used here holds without smoothness or normality
of the hypersurface; it is stated in
[de Jong's primary notes, Lemma 1.2](https://www.math.columbia.edu/~dejong/courses/schemes-spring-2020/lecture-notes-b.pdf).
Both primary sources were opened in this audit.

As a \(B\)-ideal this conductor is invertible. It has no support off
\(D\), by the explicit isomorphism there. An invertible ideal has no
additional isolated ideal defect, so it is \(\mathcal O(-aD)\).
Its class forces \(a=51\). This proves the actual ideal equality
\(\mathfrak c=\mathcal O(-51D)\), rather than only a divisor class.

For \(Q=z^4\) and a Frobenius power \(q=p^e\ge51\), the difference
\(Q^q-U_2^q=(-st^3)^q\) vanishes to order at least 51 along \(D\).
It is a global section of the conductor twisted by \(\nu^*\mathcal O_X(q)\)
and therefore descends globally. Adding the descending section \(x_2^q\)
shows that \(Q^q\) descends. The hypersurface sequence and the vanishing
of \(H^1(\mathbf P^3,\mathcal O(q-16))\) lift this to an ambient
homogeneous form. This conceptual argument is valid and gives a separate,
weaker threshold 53 for prime mate degrees. The explicit construction is
independent of it.

## Exact remaining limitations

This audit does not classify the admissible locus of the larger plane
source, compute the minimum for the finitely many primes below 43, or
bound mate degrees on arbitrary other carriers. No torus degeneration or
binomial reduction is assumed to preserve properness. The all-pairs
degree-growth implication remains open.
