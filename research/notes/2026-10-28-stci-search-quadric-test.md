# Two actual projection candidates and their exact failures

Started October 28, completed October 29, 2026. Status: **provisional exact
failed-candidate test**, not a canonical exclusion of a normalization model.

The curve is the fixed characteristic-zero quartic
\(C_0=[s^4:s^3t:st^3:t^4]\). The accepted classification
[R-0002](../results/cartier_singleton_lift.md) leaves a smooth-quadric
normalization \(S=\mathbf P^1\times\mathbf P^1\), polarization
\(H=\mathcal O(2,2)\), and diagonal lift \(c\) as a necessary model under
its full-singleton, degree-one, Cartier hypotheses. It does not construct
an admissible projection or a mate.

Put
\[
a=u_0v_0,\quad b=u_0v_1,\quad c'=u_1v_0,\quad d=u_1v_1,
\qquad \Delta=b-c'.
\]
Then \(ad=bc'\), and \(\Delta=0\) is the diagonal. Consider the actual
one-parameter four-section family
\[
U=(a^2+\Delta^2,\;ab,\;dc',\;d^2+\lambda\Delta^2).
\tag{1}
\]
Every coordinate has bidegree \((2,2)\), and restriction to the diagonal
is exactly the prescribed parametrization. The added squares address
the two obvious basepoints of the unperturbed monomial map, making (1)
a plausible first candidate rather than an asserted normalization map.

Nevertheless **every value of \(\lambda\) fails admissibility**, before
any search for a mate. On the chart \(u_0=v_0=1\), write
\(u=u_1,v=v_1\). At \(v=0\), (1) becomes
\[
U=(1+u^2,0,0,\lambda u^2).
\]
At the two geometric points \(u^2=-1\), the diagonal equation is
\(\Delta=-u\ne0\). For \(\lambda\ne0\) their image is
\([0:0:0:1]\in C_0\). Hence the full inverse support contains extra
points off the proposed lift. For \(\lambda=0\), all four
coordinates vanish at those points, so they are basepoints instead.

The [exact Macaulay2 verifier](../computations/stci_search_quadric_endpoint_2026_10_28.m2)
checks diagonal restriction and the witness modulo
\((v,u^2+1)\) over \(\mathbf Q[\lambda,u,v]\). Its saved
[output](../computations/stci_search_quadric_endpoint_2026_10_28.txt)
records the three assertions. This symbolic calculation covers every
scalar parameter, including the zero boundary; it is not a finite
sample or a claim about all degree-eight projections.

Independent reviewer `search_logic_audit` reconstructed the substitution
and both parameter cases on October 29: **PASS for exactly this pencil**.
The rejection does not depend on any unproved finiteness or birationality
claim. The two distinct points assertion is used only in characteristic zero.

The failed attempt changes the next generator: perturbing only the two
outer coordinates leaves simultaneous zeros of the middle coordinates
along an endpoint fiber. A subsequent family should perturb those middle
coordinates as well, then run basepoint and **full inverse support**
screens before a degree-by-degree mate test. The full sixteen-parameter
source and exact global membership test are described in the
[candidate inventory](2026-10-28-stci-search-candidates.md). Failure of
this pencil does not exclude that source, the quadric cone, the plane
model, or arbitrary STCI presentations.

## The next iteration: perturb the middle coordinates

The first rejection suggests modifying both middle sections. The next
actual candidate, using the same Segre coordinates, is
\[
U=(a^2+\Delta^2,\;ab+\Delta^2,\;dc'+2\Delta^2,\;d^2+3\Delta^2).
\tag{2}
\]
This candidate is basepoint free. On the diagonal this follows from the
given quartic parametrization. Off the diagonal, scale Segre coordinates
so that \(\Delta=1\). If \(U_0=U_1=0\), then \(a^2=-1\) and \(b=a\).
The Segre relation \(ad=bc'\) gives \(d=c'\). But then
\(U_3-U_2=1\), so the four sections cannot vanish simultaneously.
The resulting map is finite onto its integral image because its pullback
polarization \(\mathcal O(2,2)\) is ample. Birationality and degree-eight
image are not needed for the next rejection and are not asserted.

On the affine chart \(\Delta=1\), pull back the standard ideal generators
\[
q=x_0x_3-x_1x_2,\quad x_0^2x_2-x_1^3,\quad
x_0x_2^2-x_1^2x_3,\quad x_2^3-x_1x_3^2.
\]
Together with \(ad-bc'=0\) and \(b-c'-1=0\), these define precisely
the off-diagonal inverse scheme of \(C_0\). The chart \(\Delta=1\)
is exactly the standard projective Segre chart \(D_+(\Delta)\), so its
length has no additional scaling multiplicity. The
[updated exact Macaulay2 calculation](../computations/stci_search_quadric_updated_2026_10_29.m2)
finds dimension zero and length **16** over \(\mathbf Q\); its
[saved output](../computations/stci_search_quadric_updated_2026_10_29.txt)
includes the computed Groebner basis. Thus the inverse scheme is nonempty
over the algebraic closure, and full singleton inverse support fails.
Sixteen is the scheme length; reducedness and sixteen distinct points
have not been tested or claimed.

Independent reviewer `search_logic_audit` reconstructed the chart and
basepoint argument, replayed the script, and independently checked that
the quotient has vector-space length sixteen: **PASS for this candidate**.
The review is recorded in the
[positive-search audit, Sections 7--8](2026-10-28-stci-search-logic-audit.md).

There is an all-degree failed-candidate conclusion for the actual image
of (2), without computing its degree or proving birationality. If an
ambient homogeneous mate existed, its pullback would be a nonzero
section of \(\mathcal O(2b,2b)\) whose zero support was precisely the
diagonal together with the finite nonempty off-diagonal inverse support.
On the smooth integral surface \(S\), a nonzero section has a Cartier
zero divisor, which cannot have isolated zero points. Thus **this actual
image admits no mate in any positive degree**. This conclusion uses the
proved basepoint freedom, finiteness and zero-dimensional inverse
calculation; the earlier pencil's displayed extra points alone were not
used to infer isolation.

This is one actual update-and-test iteration: the revised candidate fixes
the first pencil's basepoint mechanism but still has extra inverse points.
It suggests solving the full-inverse parameter conditions in the
sixteen-parameter source, rather than sampling otherwise general
basepoint-free sections. The computation proves a failure for (2); it
does not prove that extra inverse points are unavoidable in that source.
