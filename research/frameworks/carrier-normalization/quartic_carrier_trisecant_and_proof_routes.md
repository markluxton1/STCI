# Trisecant contradictions and alternative proof routes

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

## 3. Nonendpoint trisecant: exact all-length contradiction

The normal conic model has an exceptional divisor of bidegree \((2,2)\) on \(\mathbf P^1\times\mathbf P^1\), with distinguished horizontal \(B\) of class \((1,0)\). Multiplicity two on \(B\) leaves two ruling fibers and violates singleton inverse support. With multiplicity one, the residual class is \((1,2)\). Every reducible residual is either a \((1,1)\) curve plus a ruling fiber or a second horizontal plus two ruling fibers, including doubled fibers; the [audit](../../arguments/carriers/genus_two_nonendpoint_proof.md) handles the coefficient-zero horizontal boundary. The remaining integral residual is a rational graph, meeting \(B\) in two transverse points.

Write \(a\) for the correction coefficient of \(B\). At the contacted ADE chain, let \(n\ge1\) be its length and \(1\le k\le n\) the contacted node; the other chain has length \(m\ge0\). Solving the inverse Cartan recurrence with virtual boundary \(z_0=a\) gives
\[
z_1=\frac{na+n+1-k}{n+1}.
\]
The other chain contributes \(ma/(m+1)\). The equation \(Z\cdot B=0\) is therefore
\[
a=\frac{(n+1-k)/(n+1)}
{3-n/(n+1)-m/(m+1)}
=\frac{(n+1-k)/(n+1)}
{1+1/(n+1)+1/(m+1)}<1.
\]
But the horizontal correction budget forces \(a=1\). The strict inequality holds for **all** chain lengths, not merely those in a bounded enumeration. The source checks the exact contact geometry that makes these chain attachments valid.


## 4. Endpoint trisecant: why the full family is necessary

The triple-contact endpoint uses the complete degree-four ideal identity
\[
I(C)\cap(x_2,x_3)^2=(q x_2,q x_3,D),
\]
which gives every relevant quartic as \(F=qQ+DL_0\) (notation defined in the [full reduction](../../arguments/carriers/genus_two_endpoint_proof.md)). The independent coverage audit exhausts the coefficient regimes \(c_0\ne0\), \(a_1\ne0\), \(a_1=0,b_1\ne0\), and \(a_1=b_1=0,c_1\ne0\). This includes the second horizontal fiber at infinity and doubled components.

In the distinct-crossing case the same all-length inequality as Section 3 applies. At triple contact the actual local models include endpoint \(A_n\) chains, an internal \(A_n\) attachment with coefficient \(2/(n+5)<1\), and a \(D_4\) configuration with coefficient \(1/4\); multiplicity three is incompatible with the accepted ADE model. These are **realized local positions in the full equation**, not arbitrary graph possibilities.

For the doubled-horizontal divisor \(2B+2F_0\), the normal derivative along \(B\) is a nonzero section
\[
h(b)=b(A+B_1b+Cb^2)\in H^0(B,\mathcal O_B(3)).
\]
Its zeros, including infinity and repeated roots, have total multiplicity three. For any ADE block, write \(Q=(-E_i\cdot E_j)\), \(v_i=B\cdot E_i\), and \(g_{BB}=v^tQ^{-1}v\). At a root away from the curve contact, the exact crepant residue and divisor calculation gives
\[
2g_{BB}=\operatorname{ord}(h).
\]
The correction equation with \(z_B=1\) requires total block contribution three. If \(A\ne0\), the contact contributes strictly below two and the other roots contribute one; if \(A=0\), the contact order is \(k=2\) or \(3\), the contact contributes at most \((k+2)/2\), and the remaining roots contribute \((3-k)/2\), totaling at most \(5/2\). Both contradict three. This argument handles arbitrary ADE blocks, not just short \(A\)-chains. Its local-coordinate proof and hypotheses remain in the [endpoint independent audit](../../arguments/carriers/genus_two_endpoint_proof.md).


## 5. Two earlier proof paths: exact overlap and unique content

The earlier [conditional endpoint argument](https://github.com/markluxton1/STCI/blob/41c48d13819c318b70a51eebf1478b5b7916c925/research/notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) treats an irreducible \((1,2)\) residual under the normal Gorenstein blowup and horizontal-correction hypotheses. Its distinct crossing calculation follows; the [complete endpoint proof](../../arguments/carriers/genus_two_endpoint_proof.md) also handles reducible and doubled residuals.

The **separate conditional conductor-power argument** belongs to [the bisection descent proof](../../arguments/carriers/genus_two_bisection_descent.md). It derives split-conductor and root-of-unity constraints under its hypotheses; those calculations survive independently of the [global ribbon exclusion](../../arguments/carriers/genus_two_bisection_proof.md). Neither conditional calculation establishes a surviving mate.

### Endpoint irreducible graph: extracted geometric argument

The earlier conditional endpoint note's distinct geometric step can be recorded precisely. In the blowup chart \(x_0=1\), set \(a=x_1/x_0\), \(y=x_2/x_0\), \(x_3/x_0=yb\). The strict transform of \(C\), parametrized by \(r=t/s\), is
\[
a=r,\qquad b=r,\qquad y=r^3.
\]
For an irreducible residual \(R\) of class \((1,2)\), the transformed surface has local equation \(aR(a,b)+yH(a,b,y)=0\). Restriction to \(C\) forces \(R(r,r)\) to vanish to order at least two. Since an irreducible \((1,2)\) curve is a graph \(a=\phi(b)\) and cannot contain the ruling fiber \(b=0\), it follows that \(\phi(0)=0\) and \(\phi'(0)=1\). The degree-two map \(R\to\Gamma\) is therefore unramified over the endpoint, with two distinct inverse points (the second possibly in the opposite chart). Both intersections with \(B=\{a=0\}\) are transverse. This supplies the geometric input for the all-length chain calculation in Section 3.

The calculation supplies the crossings for the irreducible-residual case. The [full endpoint proof](../../arguments/carriers/genus_two_endpoint_proof.md) treats reducible and doubled residuals.


## 6. Source evidence and editorial disposition

The [quartic-carrier assembly](../../arguments/carriers/quartic_carrier_proof.md) proves the exhaustive exclusion, using the focused [nonendpoint](../../arguments/carriers/genus_two_nonendpoint_proof.md) and [endpoint](../../arguments/carriers/genus_two_endpoint_proof.md) arguments. The distinct irreducible-residual crossing calculation above remains available for reuse.

## 7. Evidence and retention

The complete proof dependencies and exact local calculations are retained in those Arguments.

