# Independent audit: full attachment, residual genus and small degree

Date: 2026-10-28. Reviewer: root integration agent. Source:
[liaison residual-degree budgets](2026-10-28-residual-degree-liaison-budgets.md).
**Outcome: PASS in the stated residual-inclusive scopes. No canonical
promotion.** The degree of the once-linked curve is not used as the
genuine residual degree.

## 1. Full attachment and the cohomology hypotheses

I reconstructed the two genus equations independently. For the genuine
linked pair \(T,Z\), degrees \(4m,r\), write \(N=a+b-4\). Adjunction
gives \(p_a(Y)=1+Nab/2\), linkage gives
\(p_a(T)-p_a(Z)=N(4m-r)/2\), and the union exact sequence gives
\(p_a(Y)=p_a(T)+p_a(Z)+B-1\). Elimination produces
\(B=Nr-2p_a(Z)+2\), and hence
\(B=Nr+2h^0(O_Z)-2h^1(O_Z)\). These calculations use full schemes
and work for linked non-Gorenstein locally CM curves.

If \(h^0(O_Z)\le h\), dropping nonnegative \(h^1\) gives the source's
bound with denominator \(N\). For reduced \(Z\), its global function
dimension is its number of connected components, at most its degree.
Thus \(B\le(N+2)r\). If \(H^0(O_Z)=k\), then
\(B\le Nr+2\). The equality case in the reduced bound forces as many
components as degree, hence disjoint lines. All are conditional on the
literal global-function or reducedness statements. Topological
connectedness of a nonreduced curve does not imply \(h^0=1\).

The source correctly distinguishes the marked attachment from the full
one. A marked lower bound is also a lower bound for the full attachment
and may therefore be used to weaken the inequalities. Equating the two
lengths in the identity would be wrong. Explicitly computing the entire
primary component already determines its generic multiplicity, so these
bounds are useful for independently controlled attachment data or proposed
families, not as a computational shortcut after that extraction.

## 2. Double-line control and complete degree-two list

The displayed ribbon has square-zero ideal \(O_L(e)\), so additivity of
Euler characteristics gives genus \(-e-1\), degree two and
\(h^0=e+2\) for \(e\ge-1\). The two conormal coefficients of degree
\(e+1\) have no common zero, so their kernel has degree \(-e-2\).
This gives the displayed saturated homogeneous ideal and proves the
unbounded-negative-genus control among arbitrary candidate curves.

Purity justifies the classification used for degree two. With sole line
support and generic length two, \(I_L^2 O_Z\) vanishes generically. Its
image would be a finite-support submodule, so it vanishes by local CM
purity. The remaining square-zero ideal is a torsion-free rank-one module
on the smooth line and therefore an invertible sheaf. This gives precisely
the ribbon cases. The reduced alternatives are conics or two lines,
including the disjoint case; no punctual embedded corrections are permitted.

For an actual full double-line component of \(Y\), at least one defining
equation has nonzero first normal symbol along its line. Otherwise the
generic quotient maps onto the length-three square-maximal-ideal quotient,
contradicting total generic length two there. A nonzero symbol is a
section of \(O_L(d-e-2)\), for one of the actual degrees \(d\le b\).
Thus \(e+2\le b\), and substituting into
\(B=2N+2e+4\) proves the source's upper bound. Its parity and lower bound
also hold for conics and skew lines. A degree-one pure curve is a reduced
line and has \(B=N+2\). This verifies the small-residual exclusion test
without assuming reducedness of all candidates.

## 3. Equation and higher-support consequences

The standard dual linkage mapping cones for a line of type \((1,1)\)
and a planar conic of type \((1,2)\) give exactly the two stated minimal
resolutions for \(I_T\). The shifts can be read from dualizing their
two-generator Koszul resolutions by \(a+b\); no cancellation remains
when \(a,b\ge4\). ACM is preserved by this linkage. Two skew lines
instead have Rao module in degree zero, so dual linkage moves it to
degree \(a+b-4\), as claimed. These are necessary primary-ideal filters,
not existence assertions for the fixed quartic.

For a ribbon over a smooth support of degree \(d\), genus \(g\), the
ambient conormal has degree \(-4d-2g+2\). Removing a nilpotent quotient
of degree \(\ell\) leaves a kernel of degree
\(-4d-2g+2-\ell\). The same nonzero-symbol argument gives
\(\ell\le(b-4)d-2g+2\). Its Euler characteristic gives
\(p_a(Z)=2g-1-\ell\). Substitution into the full-attachment identity,
with \(r=2d\), yields
\(B\le(a+2b-8)r-8g+8\). The proof requires a genuine ribbon on smooth
support and does not cover arbitrary higher nilpotent layers.

## 4. Literature and conclusion

I opened [Bayer–Eisenbud's original ribbon paper](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf)
to verify the square-zero extension framework. The source attributes the
double-line description to existing primary literature; no novelty is
claimed for that classification. The liaison and full-attachment inputs
have their separately retained source/audit paths and were not rerun as
new computations.

The source's quantitative conclusions and counter-controls reconstruct
correctly. The missing universal input is a bound for attachment or
negative genus for arbitrary actual residual structures. Fixed numerical
data for the once-linked curve do not supply that bound while its
supported and genuine-residual parts redistribute degree. No unrestricted
positive residual floor is established or implied.
