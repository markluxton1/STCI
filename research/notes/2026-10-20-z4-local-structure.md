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
