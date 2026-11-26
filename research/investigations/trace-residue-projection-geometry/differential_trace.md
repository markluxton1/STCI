# Differential trace and endpoint contacts

Provisional calculation for the [trace and projection investigation](index.md).
For this comparison, let \(Y\) be any pure curve missing \(L=V(z,w)\).
On the normalizations of its reduced components the projection to
\(\mathbf P^1_{[z:w]}\) is finite and separable. Weight all traces and
residues by the generic cycle multiplicities. The logarithmic characters
below apply on components meeting the dense torus.

## Two traces

Set \(\lambda=w/z\), \(\xi=xy/(zw)\), and \(\eta=zy^2/(x^2w)\). The weighted
ordinary trace is \(T=\operatorname{Tr}(\xi)\). Define \(S\) and \(U\) by
tracing the corresponding rational differentials and dividing by
\(d\log\lambda\):
\[
  2\,\frac{x\,dy-y\,dx}{zw}=\xi\,d\log\lambda+\xi\,d\log\eta,
  \qquad 2S=T+U.
\]
The twisted regular differential \(x\,dy-y\,dx\) has trace in
\(H^0(\mathbf P^1,\omega(2))\), so \(S\) is constant. The trace of \(xy\)
is a section of \(\mathcal O(2)\), so \(T\) has at most simple poles at
zero and infinity. These conclusions use the ordinary trace of
differentials and its residue compatibility. [Stacks, Trace maps on de
Rham complexes](https://stacks.math.columbia.edu/tag/0FK6).
[Tate, Residues of differentials on curves](https://www.numdam.org/articles/10.24033/asens.1162/).

For a normalized branch over zero, choose \(r\) with \(\lambda=r^e\), and
write \(x/z=\sum a_i r^i\) and \(y/z=\sum b_j r^j\). With multiplicity
omitted, the contributions to \(S\) and to the constant Laurent
coefficient \(T_0\) of \(T\) are respectively
\[
 \operatorname{res}\frac{(x/z)d(y/z)-(y/z)d(x/z)}{r^e}
   =\sum_{i+j=e}(j-i)a_i b_j,\qquad
 \operatorname{res}\frac{(x/z)(y/z)d\lambda}{\lambda^2}
   = e\sum_{i+j=e}a_i b_j.
\]
At infinity the weighted differential residues sum to \(-S\). The
ordinary residue reciprocity applies to any such cycle. The skew pairing
for \(S\) sees the difference of complementary contact orders. At even
ramification index it misses the middle order, which still contributes
to \(T_0\). The contact orders \(1,3\) on a translated quartic give
\(S=2q\), \(T=4q\), and \(U=0\) on that component, where \(q=u/v\).
Thus for the entire translated cycle \(S=2M_1\), \(T=4M_1\).

For a proper CI missing \(L\), \(S\) agrees with the relative CI residue of
\(D_{03}=F_zG_w-F_wG_z\). On \(z=1\), implicit differentiation on the
reduced support gives the differential comparison with \(D_{12}\) and the
generic mixed-minor/socle identity gives it with the cycle weights. The
finite-flat relative residue specializes to the binary first-jet pairing.
The cycle determines the value of \(S\). The actual pair supplies its
representation in the binary Gorenstein algebra. [Spectral–Jacobian
bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md).

## CI with a nontranslated residual curve

Take the quartics
\[
 F=x^4-z^3w+zx(zw-xy),\qquad G=y^4-zw^3+wy(zw-xy).
\]
Their restrictions to \(L\) are \(x^4,y^4\), so the pair is proper and
misses \(L\). The first normal jets give numerator \(x^3y^3\) in the
binary residue, hence \(S=1\).

On \(zw\ne 0\) set \(\alpha=x/z,\ \beta=y/w\), and \(t=\alpha\beta\).
The two equations become
\(\alpha^4=\lambda(1+\alpha(t-1))\) and
\(\lambda\beta^4=1+\beta(t-1)\), with both factors nonzero. Multiplying
and factoring gives
\[
 (t-1)(t^3+2t+1-\alpha-\beta)=0 .
\]
The \(t=1\) branch is the reduced quartic. The residual branch has
\(\beta=t/\alpha\) and satisfies
\(\alpha^2-(t^3+2t+1)\alpha+t=0\). This quadratic is irreducible over
\(k(t)\) since its discriminant
\((t^2+t+1)(t^4-t^3+4t^2-t+1)\) is squarefree. Eliminate \(\alpha\) between
it and \(\alpha^4-\lambda(1+\alpha(t-1))\). The resultant divided by
\(-\lambda\) is monic, with top terms \(t^{12}+t^{11}+7t^{10}\).
It is squarefree generically, as the undivided resultant has gcd \(1\)
with its \(t\)-derivative at \(\lambda=2\). Its value before dividing at
\(t=1\) is \(\lambda^2-194\lambda+1\). The only points with \(zw=0\) are
the two endpoints. It follows that the residual curve has degree \(12\)
and contributes \(-1\) to both \(T\) and \(S\). The full pair has \(T=3\),
\(S=1\), and \(T-2S=1\).
