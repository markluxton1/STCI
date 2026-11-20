# The conductor of a square root on a transverse algebra

Let \(O=k[[u]]\), \(K=k((u))\), with \(2\) invertible. Let \(A\) be a finite
free commutative \(O\)-algebra, with augmentation \(A\to O\) and nilpotent
kernel \(J\). Fix \(v\in J\), write \(N\) for multiplication by \(v\), and
take \(w\in O\) of order \(e>0\). In \(A_K\) there is a unique root \(z\)
of \(w^2+v\) with augmentation \(w\). Its binomial expansion terminates by
nilpotence. In odd characteristic the coefficients lie in
\(\mathbb Z[1/2]\), by the formal square-root recursion. Set
\[
 B=A+zA,\qquad \mathfrak c=\{h\in A:zh\in A\},\qquad
 \delta=\ell_O(B/A).
\]
The quadratic relation makes \(B\) a ring and identifies \(A/\mathfrak c\)
with \(B/A\) by multiplication by \(z\) modulo \(A\).
Write \(S(\mu)=\sum_i\binom{\mu_i}{2}\) for a partition \(\mu\).

## Length, equality and the restriction to the reduced branch

If \(N\) has generic Jordan partition \(\mu\), then
\[
             \delta\le e S(\mu).
\]
Equality holds exactly when \(N\) has the same partition on the closed
fiber. In the equality case the image of \(\mathfrak c\) in \(O\) is
\((w^{L-1})\), for \(L=\max\mu_i\).

First suppose the partitions agree. All powers of \(N\) have the same
rank on the two fibers. Their nonzero Smith factors are units, so each
kernel surjects onto the corresponding kernel on the closed fiber.
Lift each length-\(l\) Jordan generator into \(\ker N^l\). The strings
are an \(O\)-basis by reduction. Thus \(A\), as a module for \(v\), is
a direct sum of copies of \(A_l=O[v]/v^l\). On each summand \(z\) acts
by the same polynomial in \(v\) over \(K\).

In the length-\(l\) model put \(x=z-w\). Then \(v=x(2w+x)\) and the
larger lattice is \(B_l=O[x]/x^l\). Indeed these rings agree over
\(K\) by the unit linear term there. Over \(O\), adjoining \(z\) adds
the generator \(x\), and \(1,z\) generate as an \(A_l\)-module.
The transition matrix from \(1,v,\ldots,v^{l-1}\) to the \(x\)-power
basis is triangular with diagonal \((2w)^j\), \(0\le j<l\).
That block contributes \(e\binom l2\).

Write \((Z-w)^l=P_l(v)+ZQ_l(v)\) in the polynomial ring
\(O[Z]=O[v]\oplus ZO[v]\), with \(v=Z^2-w^2\). The block conductor
is \((P_l,Q_l)\) modulo \(v^l\). In fact \(zQ_l=-P_l\) and
\(zP_l=-(v+w^2)Q_l\) in \(B_l\). Conversely a relation
\(a(v)-Zh(v)=0\) in \(B_l\) is a multiple of \((Z-w)^l\), and
its odd coefficient belongs to \((P_l,Q_l)\).
Evaluating at \(Z=w,-w\) gives \((P_l(0),Q_l(0))=(w^{l-1})\).
On a longest block we may take \(1\) as generator. Since
\(N^{L-1}1\ne0\) on the closed fiber, its coefficient at a longest
generator is a unit modulo \(v\). Replacing that generator by \(1\)
still gives a string basis, and \(N^L1=0\) upstairs. Any shorter generator has
augmentation zero, since a nonzero augmentation would make it a unit
over \(K\). Subtract their augmentations times \(1\) from any other
length-\(L\) generators. Now only the first block maps to the reduced
branch, giving the stated restriction.

For arbitrary \(N\), introduce an independent variable \(W\) and the
Laurent matrix \(Z(W)=\sum_{j\ge0}\binom{1/2}{j}W^{1-2j}N^j\).
The negative of the lowest valuation of a full-size minor of
\([I\mid Z(w)]\) is \(\delta\), by Smith form. Over \(K[[W]]\) the
constant matrix \(N\) has partition \(\mu\). The block determinant just
proved gives lowest Laurent exponent \(-S(\mu)\). All coefficients of
the minors in the original basis lie in \(O\). Evaluation at \(w\)
gives the upper bound. If the closed partition \(\nu\) differs, ranks of
powers specialize downwards, so \(\nu\) is strictly dominated by
\(\mu\), and \(S(\nu)<S(\mu)\) by strict convexity. Applying the
same calculation over \(k[[W]]\) shows that every coefficient at
exponent \(-S(\mu)\) vanishes modulo \(u\). Every minor at \(w\)
then has valuation strictly greater than \(-eS(\mu)\).

## Extra vanishing at a quadratic singularity

Assume all the \(J^i/J^{i+1}\) are \(O\)-free, of ranks \(H_i\),
and \(v\in u^sJ+J^2\), where \(s\ge0\) is an integer and
\(2s\le e=\operatorname{ord}(w)\). For a unimodal \(H\), let
\(\Lambda=H^\vee\), whose \(j\)-th part is \(\#\{i:H_i\ge j\}\), and put
\[
 D_H=\min_{c\in\mathbb R}\sum_i H_i|i-c|,\qquad
 M(\lambda)=\sum_j\lfloor\lambda_j/2\rfloor .
\]
Then
\[
 \delta\le(e-s)S(\Lambda)+sD_H-sM(\Lambda)
                  \le eS(\Lambda)-sM(\Lambda).                    \tag{1}
\]
This retains the vanishing of the first normal coefficient. The moving
osculating quadric uses \((e,s)=(4,1)\), giving
\(3S(\Lambda)+D_H-M(\Lambda)\). The inequality needs only the
odd-characteristic local algebra hypotheses above, not the global CI
or characteristic-zero Lefschetz input.

Choose a basis splitting the \(J\)-adic filtration. Each entry of \(N\)
raises filtration degree at least one, and a step of exactly one degree
has coefficient divisible by \(u^s\). In an \(r\)-minor of \(Z(W)\) a
term of degree \(r-2j\) in \(W\) follows \(j\) matrix steps. Write \(d\)
for the sum of the row degrees less the sum of the column degrees.
At least \(2j-d\) of the steps have degree one. Also \(d\le D_H\):
cancel indices selected as both rows and columns, and subtract the
same \(c\) from all degrees in the two equal-size remaining sets.
The term at \(W=w\) thus has valuation at least
\(-(e-s)(2j-r)+sr-sD_H\). A negative lower bound for the number
of one-degree steps merely weakens this estimate.

In a generic Jordan block of length \(l\), an \(h\)-minor has Laurent
pole order at most \(h(2l-2h-1)\). Each nonzero entry in row \(i\),
column \(j'\) has exponent \(1-2(i-j')\), and the largest sum of the
row indices less the sum of the column indices is \(h(l-h)\).
The difference between \(\binom l2\) and this pole bound is at least
\(|h-\lfloor l/2\rfloor|\), by expanding the quadratic separately for
even and odd \(l\). For the whole generic matrix, Cauchy–Binet under
the \(W\)-independent change of basis therefore gives
\[
                 2j-r\le S(\mu)-|r-M(\mu)|
\]
for every *nonzero coefficient* of an \(r\)-minor. Cancellations
cannot lower the preceding coefficient-valuation estimate. Expanding
full-size minors along their identity columns and using
\[
 \min_{0\le r\le\operatorname{rank}A}
       \bigl((e-s)|r-M(\mu)|+sr\bigr)=sM(\mu)
\]
now gives \(\delta\le(e-s)S(\mu)+sD_H-sM(\mu)\).
Here \(e\ge2s\) is exactly what makes the minimum occur at
\(r=M(\mu)\); equality \(e=2s\) is allowed.

Indeed \(\mu\preceq\Lambda\): \(N^j J^i\subset J^{i+j}\) gives kernel
dimension at least \(\sum_{h=i}^{i+j-1}H_h\) on the generic fiber.
By unimodality the largest such sum is the sum of the \(j\) largest
values of \(H\), the kernel dimension for \(\Lambda\). A unit transfer
increasing dominance increases \(S\) by at least one and changes \(M\)
by at most one, so \((e-s)S-sM\) does not decrease when \(e\ge2s\).
Finally, the superlevel sets of \(H\) are intervals
containing a common mode. The sum of distances to that mode on an
interval of length \(l\) is at most \(\binom l2\). This proves (1).
The local hypotheses permit arbitrary higher coefficients. For instance
\(A=O[v_0]/v_0^2,\ v=uv_0,\ w=u^4\) has \(z=u^4+v_0/(2u^3)\)
and attains (1) with length three. For cyclic \(H=(1,\ldots,1)\)
of length \(n\), \(D_H=\lfloor n^2/4\rfloor\) and
\(S(\Lambda)+M(\Lambda)=2D_H\), so (1) equals
\[
 (2e-s)\lfloor n^2/4\rfloor-e\lfloor n/2\rfloor.
\]
The characteristic-zero [cyclic calculation](conductor_on_a_smooth_carrier.md#a-cyclic-length-independent-of-higher-normal-coefficients)
proves equality when the first normal coefficient has exact order
\(s<e\). The inequality does not use that determinant nonvanishing.
No bound with \(2s>e\) is asserted by this optimization.

Independent review reconstructed the general \((e,s)\) coefficient
estimate, the endpoint \(e=2s\), dominance comparison and cyclic
specialization on November 20, 2026.
