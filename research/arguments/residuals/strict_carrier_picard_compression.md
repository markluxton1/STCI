# Picard compression on ample strict carriers

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed LC1–LC4 and their stated minimum-mate arithmetic. Inherited inputs are the stated Lefschetz/Kummer input, established R-0077 equality/second-blowup bounds and actual local-index extension.

The shared setup and notation are the [two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary) and [whole equality boundary](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary). This account owns the strict-carrier Lefschetz and Picard compression argument.

## Lefschetz compression on ample strict carriers

**Scope and status.** This is a new application of established Lefschetz
and Kummer theory to the actual first graph, reconstructed at the scope above.
It applies in characteristic zero, also to entirely-thick original pairs.
The equality case below uses the connected-direction and second-blowup
bounds of [R-0077](../../results/connected_normal_directions.md), whose necessary connectedness, equality and second-blowup proof route was independently reconstructed on November 23, 2026. It does not assume a normal original carrier.

**Lefschetz input.** For an integral ample Cartier surface \(S\) in a
smooth projective threefold \(B\), the restriction of \(\operatorname{Pic}(B)\)
has saturated image in \(\operatorname{Pic}(S)\) if \(\operatorname{Pic}(B)\)
is torsion-free (over an algebraically closed characteristic-zero field).
More precisely, if \(rM=A|_S\) with \(A\in\operatorname{Pic}(B)\),
then \(A=rA_0\) in \(\operatorname{Pic}(B)\) and \(M=A_0|_S\).
Indeed [Cotner–Zavyalov, Theorem 3.2.2](https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64)
applied to \(\mu_{\ell^j}\), with affine complement to the ample divisor,
gives an isomorphism in \(H^1\) and injectivity in \(H^2\).
The Kummer sequence, since both schemes have global units \(k^*\),
gives \(\operatorname{Pic}(S)[\ell^j]=0\) and injectivity of
\(\operatorname{Pic}(B)/\ell^j\to\operatorname{Pic}(S)/\ell^j\).
Prime-power decomposition gives the assertion for \(r\).
This is the existing ample-divisor Lefschetz theorem, not a new
Noether–Lefschetz assertion that every class on \(S\) is ambient.
Normality of \(S\) is not needed.

**Application (LC1).** Retain the actual proper sole-support pair with
orders \(p,q>0\) and degrees \(a\ge3p,\ b>3q\), and suppose its first
strict intersection \(W\) has sole reduced support a smooth integral
curve \(T\subset E\). Write \(c=m-pq\) if \(T\) is a section over \(C\);
more generally let \(c\) be the actual generic length along \(T\).
Assume the strict degree-\(b\) carrier \(S\) is integral and regular at
the generic point of \(T\). Set \(A=aH-pE\).
The divisor \(S\sim bH-qE=(b-3q)H+qL\) is ample: the maps of the two
basepoint-free classes \(H,L\) have no common contracted curve, so the
map to their product is finite. The blowup formula gives
\(\operatorname{Pic}(B)=\mathbb ZH\oplus\mathbb ZE\).

Let \(R\) be the lcm of the actual local indices of \(T\) on \(S\)
in the almost-Cartier sense. The effective Cartier divisor \(W=cT\)
gives \(R\mid c\); the generically regular \(S_2\) extension argument
of [AC1–AC3](../carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices)
gives the effective Cartier divisor \(RT\) on \(S\).
Putting \(k=c/R\), the equality \(k[RT]=A|_S\) and the Lefschetz input give
\[
 \boxed{k\mid\gcd(a,p),\qquad
 RT\sim (a/k)H-(p/k)E\ \text{ on }S.} \tag{LC1}
\]
The index is on the strict carrier, not the normalization or the original
carrier in \(\mathbf P^3\).

**Actual lift (LC2).** Write \(a'=a/k,p'=p/k\). If
\(p'\le q\) and \(a'-3p'\le b-3q\), restriction of
\(\mathcal O_B(a'H-p'E)\) to \(S\) is surjective on global sections.
By Serre duality the required vanishing of
\(H^1(B,\mathcal O_B(a'H-p'E-S))\) is equivalent to vanishing of
\[
 H^2(B,\mathcal O_B((b-a'-4)H+(1+p'-q)E)).
\]
For \(p'<q\), use the
[graph vanishing in R-0077](../../results/connected_normal_directions.md#connectedness-and-residual-attachment),
\(H^i(B,jH-nE)=0\) for \(i>0,n\ge0,j\ge3n-1\), with
\(n=q-p'-1,\ j=b-a'-4\).
For \(p'=q\), restriction to \(E\) of the extra \(E\)-twist has
fiber degree \(-1\) and is acyclic, reducing to \(H^2(\mathbf P^3,\mathcal
O(b-a'-4))=0\). Lift the canonical section of \(RT\) to \(B\); the
blowup section dictionary supplies an actual degree-\(a'\) form in
\(H^0(\mathbf P^3,I_C^{p'}(a'))\). Its intersection with the original
degree-\(b\) carrier has reduced support exactly \(C\): off \(E\) the
strict carrier has no intersection with the lifted section, and the new
form vanishes along all of \(C\). It is a proper intersection since
its restriction to \(S\) is nonzero. The lift need not preserve the
original nonreduced ideal or have exact order \(p'\) in general.
Thus for a minimum actual mate, or an absolute minimum degree-product
pair, these lifting inequalities force \(R=c\). On the edge
\((a,b)=(3p,4q)\), \(p\le q\), they always hold and \(c=2pq\) for a
constant section. For \(p=1\), (LC1) already gives \(R=c\).

**Normal replacement on the graph (LC3).** If the strict pair has
generic embedding dimension at most one along its smooth sole-support
curve, and \(bH-qE-A\) is globally generated, a general member of
\[
 \{\lambda G'+F'J:J\in H^0(B,\mathcal O_B(bH-qE-A))\}
\]
is smooth off \(T\) by characteristic-zero Bertini and regular at its
generic point by the first-symbol test. It is \(S_2\) as a hypersurface
and hence normal; connectedness of an ample divisor gives integrality.
Choose \(\lambda\ne0\) and avoid the proper linear condition of
containing \(E\), so the ideal on \(B\) is preserved and this member is
the strict transform of an actual degree-\(b\), order-\(q\) equation.
This is the same generator-replacement argument as NR1, now on \(B\).
On the edge with \(p\le q\), the difference is \(qH+(q-p)L\) and is
globally generated. The replacement is normal on the graph even if
both original equations are generically thick along \(C\).

**Application to the first entirely-thick numerical pair.** Suppose
\((a,b;p,q)=(6,8;2,2)\) is an actual sole-support pair. By R-0077 its
first strict intersection is supported on one constant section with
\(c=8\). Let \(r,s\) be the actual generic orders on that section of
the strict sextic and octic. They lie in \(\{1,2\}\), since each
order is bounded by the multiplicity of the corresponding normal root.
The second-blowup inequality of
[R-0077](../../results/connected_normal_directions.md#bounding-the-orders-after-blowing-up-the-section)
gives
\[
 10s+18r\le(7-d)8+d\,rs,\qquad d\in\{2,3\}.
\]
For \(r=2,s=1\) it fails (46 exceeds 44 or 38), and for \(r=s=2\)
it fails (56 exceeds 48 or 44). Hence \(r=1\).
By LC3 a general strict octic is normal and preserves the strict
pair, since the difference is \(2H\). The original ambient pair is
also preserved by this replacement. By LC1 the marked section on that
strict octic has \(R\mid8\) and \(8/R\mid\gcd(6,2)=2\), so \(R=4\)
or \(8\). If \(R=4\), LC2 produces a degree-three ambient mate for
the replaced octic, contrary to the low-degree carrier exclusion
([R-0001](../../results/quartic_carrier_exclusion.md) and the degree
\(\le3\) exclusions). Thus
\[
 \boxed{R=8,\quad\text{and some point of }T\text{ has actual local index }8.}
 \tag{LC4}
\]
The last statement follows because every local index divides eight.
This is not an exclusion of \((6,8)\). It changes its remaining
entirely-thick problem to a generically curvilinear CI on the first
graph, with a forced maximal local Cartier index on an ample normal
strict carrier. Normality of the original octic in \(\mathbf P^3\)
does not follow. Local symbolic-power and socle arguments can now
be studied on the marked section with its actual conormal bundle,
rather than assumed on the original \(C\).


