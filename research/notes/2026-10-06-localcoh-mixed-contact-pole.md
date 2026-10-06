# A coprime mixed constant-direction contact pair fails the target equations

Date: 2026-10-06. Status: **PROVED / EXACT COMPUTATION** for the explicit
quartic pair only. The finite all-stage reduction depends on the existing
characteristic-zero quartic local-cohomology bound. This does not exclude
all mixed constant directions.

The exact companion `verify_localcoh_direction_contact_survivor.py` constructs
explicit ambient-coprime quartics \(F,G\) with balanced first symbols
\((2h_F,h_F)\), \((2h_G,h_G)\). Their common scalar divisor is

\[
D(t)=t^4-t^3-3t^2-t+1.
\]

It verifies \(\gcd(F,G)=1\) and the second-contact identity
\(h_F b_G-h_G b_F=0\), where \(b_F,b_G\) are the quadratic normal
coefficients along the kernel of the common first direction. Thus this pair
passes both first-conormal rank and generic length-at-least-three tests.
Its degree-four common scalar divisor also kills the P-010 obstruction class
\(h_{1/2}\), as checked independently by
`verify_localcoh_constant_direction_apolar.py`.

The complete target-specific generic inverse-system equations are finite.
An order-four ancestor has the ten inverse-monomial coefficients with
\(i+j\le3\), for monomials \(U^{-i-1}V^{-j-1}\). Multiplication by the
two quartics gives twelve linear equations over \(\mathbf Q(t)\), with
socle right sides \(1,t^2\). These are the actual balanced-frame
representatives of \(u,v\), since the first normal determinant of \((q,B)\)
relative to \((U,V)\) is \(t^3\).

The exact linear solution forces its four highest inverse coefficients to be

\[
(8,-4,2,-1)\,C(t),\qquad
C(t)=\frac{(t+1)D(t)(2t^6-3t^5+2t^4-3t^3-2t+1)}
 {5t^4-2t^3+6t^2-2t+5}.
\]

The lower principal-part freedom does not affect this coefficient. The
script now explicitly asserts that the displayed numerator and denominator
are coprime and that the denominator has degree four; earlier Oct5 output
merely printed the fractions. Therefore \(C(t)\) has finite poles over
the algebraic closure. A global highest symbol is a regular section of
\(O(7)^4\) in the fixed balanced frame, and cannot have these poles.

Thus this pair has no global quartic common ancestor for the two fixed
targets. The finite principal-part bound makes the exclusion apply at every
direct-limit stage. The lesson is concrete: rank-one first symbols, valid
second contact, and a permitted scalar pole divisor can all hold while the
target-specific highest ancestor coefficient still has forbidden poles.
