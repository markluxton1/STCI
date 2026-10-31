# A Chow-pencil multiplicity test and its limitation

Work over an algebraically closed field with the fixed embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\). The [global Chow-resultant certificate](../synthesis/global_equations_and_constructions.md#chow-determinant-and-the-sole-support-certificate) says that a proper degree-\((4,5)\) pair with sole support \(C_0\) has line resultant proportional to the fifth power of its Chow form. Restricting to one explicit pencil gives useful family exclusions, but a single pencil does not test every possible residual curve.

This proof preserves the former P-036 argument independently of the stronger carrier exclusion. Its exact linear source dimensions and explicit polynomial identities are supported by [the retained checker](../computations/verify_chow_pencil_45.py); the written multiplicity and irreducibility arguments supply their geometric meaning. The monomial source spaces and resultant/corank family exclusions below work in every characteristic: their dimension proofs use distinct monomials with coefficients one, and the valuation proof uses no division. The explicit irreducible one-pencil survivor uses invertibility of two, so that illustration is asserted only in characteristic different from two. Neither statement extends the full characteristic-zero quartic-carrier exclusion to positive characteristic.

## The exact pencil, source spaces and valuation contradiction

For

\[
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

consider the Schubert pencil

\[
 L_{[\beta:\gamma]}:\quad x_1=0,\quad
 \gamma x_3-\beta x_0=0,
\]

parametrized by

\[
 [x_0:x_1:x_2:x_3]=[\gamma U:0:V:\beta U].
\]

The only nonzero Pluecker coordinates are
\(p_{01}=\beta\) and \(p_{13}=\gamma\).  Substitution into the exact Chow quartic, or direct computation of
\(\operatorname{Res}(s^3t,\gamma t^4-\beta s^4)\), gives

\[
 \operatorname{Ch}_{C_0}|_L=-\beta\gamma^3.
\]

Consequently any degree-\((4,5)\) pair supported on \(C_0\) must satisfy

\[
 \operatorname{Res}_{U,V}(F|_L,G|_L)
 =\mu\beta^5\gamma^{15},\qquad \mu\ne0.
\]

Monomial restrictions in degrees four and five span all binary monomials of the corresponding degree on \(C\). Consequently restriction has dimensions seventeen and twenty-one, respectively, giving

\[
 \dim I_{C_0}(4)=18,\qquad \dim I_{C_0}(5)=35,
\]

and the stronger intersections

\[
\begin{aligned}
 J_4&=I_{C_0}(4)\cap(x_1,x_2x_3,x_3^2)_4,
 &\dim J_4&=13,\\
 J_5&=I_{C_0}(5)\cap(x_1,x_3^2,x_2^2x_3)_5,
 &\dim J_5&=28.
\end{aligned}
\]

For the first dimension, the quotient by
\((x_1,x_2x_3,x_3^2)\) has degree-four basis

\[
 x_0^4,\ x_0^3x_2,\ x_0^2x_2^2,\ x_0x_2^3,\ x_2^4,\ x_0^3x_3.
\]

The image of \(I_{C_0}(4)\) is the five-dimensional hyperplane omitting
\(x_0^4\), with representatives
\(x_0A,x_0B,x_0D,x_2D,x_0^2q\).  This gives \(18-5=13\).
Similarly, the quotient by \((x_1,x_3^2,x_2^2x_3)\) has eight degree-five
basis monomials, and the image of \(I_{C_0}(5)\) is the seven-dimensional
hyperplane omitting \(x_0^5\), with representatives

\[
 x_0^2A,\ x_0^2B,\ x_0^2D,\ x_0x_2D,\ x_2^2D,\ x_0^3q,\ x_0^2x_2q.
\]

Hence \(\dim J_5=35-7=28\).

If \(F\in J_4\), then \(F|_L=\beta\widehat F\), and at \(\beta=0\) the
residual form \(\widehat F\) is divisible by \(V\).  Since
\(F|_{L_0}=0\), support equality would force \(G|_{L_0}=cV^5\).
Scaling the quartic contributes \(\beta^5\) to the resultant, while the
shared residual \(V\)-root contributes at least one more order.  Thus the
resultant has \(\beta\)-order at least six, not five.

If \(G\in J_5\), write \(G|_L=\beta\widehat G\).  At \(\beta=0\),
\(\widehat G\) is divisible by \(V^2\), while support equality forces
\(F|_{L_0}=cV^4\).  Scaling the quintic contributes \(\beta^4\), and the
specialized Sylvester matrix has corank at least two, so the residual
determinant contributes at least two further orders.  Again the total
\(\beta\)-order is at least six.  Therefore no member of \(J_4\) or \(J_5\)
can occur in a \((4,5)\) pair.  In particular, the simpler contained spaces
\(I_4\cap(x_1,x_3^2)\) and \(I_5\cap(x_1,x_3^2)\), of dimensions 10 and 25,
remain excluded, as does the whole family

\[
 F=x_1A+\kappa q^2
\]

against every quintic mate, without the regular-ratio assumption
used by the regular-ratio finite-jet argument.  The involution

\[
 (x_0,x_1,x_2,x_3)\longmapsto(x_3,x_2,x_1,x_0)
\]

gives the symmetric excluded spaces

\[
 I_4\cap(x_2,x_0x_1,x_0^2)_4,\qquad
 I_5\cap(x_2,x_0^2,x_0x_1^2)_5,
\]

again of dimensions 13 and 28, including
\(F=x_2D+\kappa q^2\).

One pencil is nevertheless not exhaustive.  The explicit forms

\[
\begin{aligned}
F={}&x_0^3x_2-x_0^3x_3+x_0^2x_1x_2-x_0x_1^3
      -x_1^2x_3^2+x_1x_2^3,\\
G={}&x_0^4x_2-x_0^4x_3+x_0^3x_1x_2-x_0^2x_1^3\\
   &-x_1x_2^2x_3^2-x_1x_2x_3^3+x_2^5+x_2^4x_3
\end{aligned}
\]

both lie in \(I_{C_0}\). On the displayed pencil their restrictions are
\[
F|_L=\gamma^3U^3(V-\beta U),\qquad
G|_L=\gamma^4U^4(V-\beta U)+V^4(V+\beta U).
\]
Multiplicativity of the binary resultant, evaluation at \(U=0\) and \(V=\beta U\), and the scaling factor \(\gamma^{15}\) give exactly

\[
 -2\beta^5\gamma^{15}.
\]

The quartic \(F\) is absolutely irreducible when two is invertible: as a
quadratic in \(x_3\), its discriminant has odd degree three in \(x_2\) over
\(\overline{k}(x_0,x_1)\), and so is not a square.  Yet on the
coordinate-reversed pencil both restricted forms share the projective factor
\(U\), and the homogeneous resultant is identically zero.  This pair is a
route-limitation certificate, not an STCI candidate.

For comparison,

\[
 \dim(I_4\cap(x_1,x_3)_4)=14,\qquad
 \dim(I_5\cap(x_1,x_3)_5)=30.
\]

If both members lie in these spaces, both contain the line
\(V(x_1,x_3)\), and their restricted binary forms share the factor \(U\);
the resultant is identically zero.  This simultaneous case is therefore a
common-line exclusion, not merely a lower bound on \(\beta\)-adic order.

The exact script `computations/verify_chow_pencil_45.py` checks the dimensions,
the stronger monomial-ideal intersections, the Chow restriction, the
coefficient-factor claims, and the explicit one-pencil survivor and reversed
failure.  Passing one pencil is only necessary; this is a family exclusion, while the independent [multiple-structure proof](QUASIPRIMITIVE_MULTIPLICITY_FIVE.md) closes the degree pair in characteristic zero. It does not prove unrestricted STCI nonexistence.



## Consolidation review

Independent review reconstructed the preserved arguments, source coverage and
characteristic boundaries. The bounded proof clarifications in this account
were checked against the original arguments; no material preservation finding
remains. This reviewed consolidation does not promote additional canonical
results or extend the claims beyond their stated hypotheses.
