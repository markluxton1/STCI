# Exact Chow bundle maps and ambient equations

This is reviewed mathematics for an algebraically closed field
of any characteristic. It clarifies the prescribed bundle types in the
[global Chow-resultant criterion](global_equations_and_constructions.md#p-033-the-global-chow-resultant-certificate).
It gives neither a new supported pair nor an exclusion of all such pairs.

## A general Hom identity on the Grassmannian

Let \(G=\operatorname{Gr}(2,V)\), with \(\dim V\ge3\) and tautological
rank-two bundle \(S\). For integers \(r,s\ge0\),
\[
\operatorname{Hom}_G(\operatorname{Sym}^r S^\vee,
                     \operatorname{Sym}^s S^\vee)
\simeq H^0(\mathbf P(V),\mathcal O(s-r)).
\]
For \(s\ge r\), a global form acts by multiplication after restriction
to each line. For \(s<r\), both sides vanish.

To prove surjectivity, use the point-line incidence variety with projections
\(\pi\) to \(G\) and \(q\) to \(\mathbf P(V)\). Evaluation gives
\[
\pi^*\operatorname{Sym}^r S^\vee\longrightarrow q^*\mathcal O(r).
\]
A fiber of \(q\) is \(\mathbf P^{\dim V-2}\). On this fiber,
\(\pi^*S^\vee\simeq\mathcal O\oplus\mathcal O(1)\), with evaluation
onto the trivial summand. Its symmetric-power evaluation kernel is
\(\bigoplus_{j=1}^r\mathcal O(j)\). A proposed bundle map followed by
target evaluation kills this kernel: on each positive-dimensional point
fiber there are no maps \(\mathcal O(j)\to\mathcal O\) for \(j>0\).
It therefore factors through a map
\(q^*\mathcal O(r)\to q^*\mathcal O(s)\). Since \(q_*\mathcal O=\mathcal O\),
this factor is a global form of degree \(s-r\). Evaluation at all points
of each line identifies the original map with multiplication by that form,
and also proves uniqueness. The fiber splitting and vanishing argument
uses no characteristic-zero decomposition of representations.

## The prescribed Sylvester bundles already retain the equations

For positive \(a,b\), every global map
\[
\operatorname{Sym}^{b-1}S^\vee\oplus
\operatorname{Sym}^{a-1}S^\vee
\longrightarrow\operatorname{Sym}^{a+b-1}S^\vee
\]
is uniquely the Sylvester map of two global forms of degrees \(a,b\).
Thus, once these exact source and target bundles are imposed, there is no
additional independent multiplication-block or global-section lifting
condition. Constructing such a map with determinant a nonzero pure power
of the prescribed curve's Chow form is still the original existence problem.
The [resultant criterion](global_equations_and_constructions.md#p-033-the-global-chow-resultant-certificate)
retains properness, degree divisibility and the exact cycle interpretation.

Arbitrary linear determinants have different scope. The full Chow complex
can recover more than its determinant, which records the associated cycle;
see [Eisenbud–Schreyer, Proposition 1.3 and Theorem 1.4](https://arxiv.org/pdf/math/0111040).
Their Theorem 0.2 and curve constructions in Theorem 4.3 and Proposition 4.4
already give a linear determinant for \(C_0\): the line bundle
\(\mathcal O_{\mathbf P^1}(3)\), after twisting by
\(\mathcal O_{C_0}(-1)=\mathcal O_{\mathbf P^1}(-4)\), is acyclic.
Direct sums give every positive Chow power. The resulting bundle maps are
\[
\mathcal O_G(-1)^{4m}\longrightarrow\mathcal O_G^{4m},
\]
rather than the prescribed symmetric-power bundles. They represent sheaves
on the reduced curve, and do not construct the desired embedded
complete-intersection thickening.

The elementary Hom proof, exact bundle consequence and primary-source
applications received independent review in the final source checkpoint
`57fb49bc41a40a0eca766f6640a49b36e97ef078`. That follow-up closes the earlier
source's audit gap. The present consolidation retains their full scope;
result records are unchanged.
