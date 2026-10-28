# Genuine residual degree: attachment bounds, low-degree structure, and genus limits

Date: 2026-10-28. Author: residual-liaison agent. Status: **provisional,
pending independent review; no canonical promotion**. This answers the
quantitative question for proper intersections containing the fixed quartic,
without assuming that a sole-support endpoint is impossible.

## 1. The exact objects and inherited inputs

Let \(k\) be algebraically closed of characteristic zero, and let
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). For an actual homogeneous
proper pair, write

\[
Y=V(F_a,G_b),\qquad [Y]=m[C]+R,\qquad r=\deg R=ab-4m.
\]

Let \(T\) be the **full** \(C\)-primary component, and let \(Z\) be the
residual scheme after removing it. Thus \([Z]=R\), \(\deg T=4m\), and
\(\deg Z=r\). The two schemes are locally Cohen–Macaulay, share no curve
component, and are linked by \(Y\). They need not be reduced, connected, or
Gorenstein. When \(r>0\), put

\[
N=a+b-4>0,\qquad B=\operatorname{length}(T\cap Z).
\]

Retrieval followed [INDEX](../INDEX.md) and [MAP](../MAP.md), then:

- [The attachment-module source](2026-10-27-absorption-attachment-module.md)
  and its [independent audit](2026-10-27-absorption-attachment-module-audit.md):
  the full attachment is different from the marked \(C\cap Z\), and its
  length can be computed by torsion, determinant, and normal-nilpotent
  contributions. The linkage budget below is already present there in
  its \(T\)-side form; it is not a new theorem.
- [The reviewed once-link source](2026-10-28-residual-liaison-construction.md)
  and [audit](2026-10-28-residual-liaison-audit.md): degree, genus, Rao module,
  equation recovery, and flatness concern \(D=Y:C\), whose cycle is
  \((m-1)[C]+R\). These do not identify \(\deg D=ab-4\) with \(r\).
- [R-0032](../results/full_conormal_socle_budget.md) assumes reduced support
  exactly \(C\). Its displayed socle identity cannot be applied to the
  present residual-inclusive problem without proving the additional
  residual terms. That scope is retained.

The additional deductions in this note are conditional lower bounds using
the full attachment, and exact tests on genuine residuals of degrees one
and two. They complement order-dependent graph bounds; they do not replace
them with an unrestricted positive residual floor.

## 2. The attachment identity on the genuine residual side

The same standard linkage calculation gives

\[
\boxed{B=Nr-2p_a(Z)+2.}\tag{1}
\]

Indeed adjunction gives \(p_a(Y)=1+Nab/2\), and linkage gives

\[
p_a(T)-p_a(Z)=\frac N2(4m-r).
\]

The scheme-union exact sequence gives
\(p_a(Y)=p_a(T)+p_a(Z)+B-1\), proving (1). These formulas hold for
nonreduced locally Cohen–Macaulay schemes, using their dualizing modules;
they are not formulas for the reduced support or normalization.

Since \(p_a(Z)=1-h^0(\mathcal O_Z)+h^1(\mathcal O_Z)\), equation (1)
also reads

\[
B=Nr+2h^0(\mathcal O_Z)-2h^1(\mathcal O_Z).
\tag{2}
\]

Consequently, if a separate argument supplies \(h^0(\mathcal O_Z)\le h\),
then

\[
\boxed{r\ge\max\{1,\lceil(B-2h)/N\rceil\}.}\tag{3}
\]

This is useful when the full-primary attachment module can be computed
before a residual decomposition. It is conditional on that extra
cohomology information; connected nonreduced support does not imply
\(h^0=1\).

Two clean cases need no detailed cohomology calculation:

- If \(Z\) is reduced, it has at most \(r\) connected components, and
  \(h^0(\mathcal O_Z)\) is their number. Thus
  \[
  \boxed{r\ge\max\{1,\lceil B/(a+b-2)\rceil\}.}\tag{4}
  \]
- If \(Z\) is reduced and connected, or more generally
  \(H^0(\mathcal O_Z)=k\), then
  \[
  \boxed{r\ge\max\{1,\lceil(B-2)/(a+b-4)\rceil\}.}\tag{5}
  \]

For (4), the equality \(B=(N+2)r\) forces \(r\) disjoint lines: equality
requires \(h^0=r\) and \(h^1=0\), so each connected component has degree
one. This is an equality characterization for any actual pair attaining
it, not a construction of such a pair for arbitrary degrees.

The variable \(B\) cannot silently be replaced by
\(\operatorname{length}(C\cap Z)\). The full attachment can have an
additional normal-nilpotent contribution even when the marked intersection
has been fixed. Likewise (4) cannot be used after merely reducing \(Z\):
that changes its degree and its Euler characteristic.

## 3. Why genus alone does not give an unrestricted degree bound

There are locally Cohen–Macaulay double lines of degree two and arbitrarily
negative arithmetic genus. In coordinates \([x:y:z:w]\), take
\(L=V(x,y)\), choose \(e\ge-1\), and a surjection

\[
\mathcal O_L(-1)^2\xrightarrow{(f,g)}\mathcal O_L(e),
\]

where \(f,g\) have degree \(e+1\) and no common zero on \(L\). The
kernel construction gives the ribbon with ideal

\[
I_Z=(x^2,xy,y^2,gx-fy),
\qquad
0\to\mathcal O_L(e)\to\mathcal O_Z\to\mathcal O_L\to0.
\tag{6}
\]

It has

\[
\deg Z=2,\qquad p_a(Z)=-e-1,\qquad
h^0(\mathcal O_Z)=e+2,\qquad h^1(\mathcal O_Z)=0.
\]

Thus the right side of (1), for fixed \(r=2\), can be arbitrarily large
among unrestricted curve candidates. A reduced integral Castelnuovo bound
cannot be applied to these schemes. Even topological connectedness does
not repair the issue: the extra global functions in (6) are nilpotent.

This is standard ribbon geometry, not a new example. The primary text
[Nollet–Schlesinger, *Hilbert Schemes of Degree Four Curves* (2003)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B62E5E7FF38C897359DE99E647E71DFF/S0010437X03100711a.pdf/hilbert-schemes-of-degree-four-curves.pdf)
uses the displayed homogeneous double-line ideals and genus calculation.
[Bayer–Eisenbud, *Ribbons and their canonical embeddings*](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf)
provides the square-zero extension framework. These sources were inspected
on 2026-10-28; no literature novelty is asserted.

This is a limitation of genus-only reasoning for arbitrary candidates.
It does **not** assert that all these ribbons occur as the full residual
of pairs of two fixed degrees containing \(C\). Actual equations impose
additional bounds, which the next section makes explicit in degree two.

## 4. Actual equations sharply constrain a degree-two residual

Assume \(a\le b\). If the genuine residual degree is one, purity makes
\(Z\) a reduced line. Therefore

\[
\boxed{r=1\ \Longrightarrow\ B=N+2.}\tag{7}
\]

If the genuine residual degree is two, its possible structures are a
plane conic (including intersecting lines and a planar double line), two
skew lines, or a nonplanar double line. In the first two cases,

\[
B=2N+2\quad\text{or}\quad B=2N+4.
\tag{8}
\]

For a double line, (6) gives

\[
B=2N+2e+4.
\tag{9}
\]

For clarity, purity excludes hidden exceptional degree-two schemes in
this list. A component of degree two and multiplicity one is an integral
conic; two components of degree one are lines. With sole support a line,
generic length two makes \(I_L^2\) vanish generically in \(\mathcal O_Z\),
and absence of embedded associated points makes it vanish everywhere.
The resulting square-zero ideal is a torsion-free rank-one module on the
smooth line, hence a line bundle. This gives (6), with \(e\ge-1\) forced
by the globally surjective conormal quotient.

There is now an equation-degree restriction absent from the genus-only
control:

\[
\boxed{e+2\le b.}\tag{10}
\]

To prove it, the conormal sequence of (6) gives

\[
I_Z/I_L^2\simeq\mathcal O_L(-e-2)
\ \subset\ I_L/I_L^2=\mathcal O_L(-1)^2.
\]

The first normal symbol of a degree-\(d\) equation containing \(Z\)
therefore lies in \(H^0(\mathcal O_L(d-e-2))\). If \(a,b<e+2\), both
first symbols vanish. At \(\eta_L\), both equations then lie in the square
of the maximal ideal of the regular two-dimensional normal local ring.
Their quotient has length at least three, since it surjects onto the
length-three quotient by that square. This already contradicts length two
for a full double-line component of \(Y\). Hence at least one first
symbol is nonzero, and its degree is at most \(b\), proving (10).

Combining the cases yields the exact small-degree test

\[
\boxed{
r=2\ \Longrightarrow\
B\text{ is even and }2N+2\le B\le2N+2b.
}\tag{11}
\]

Thus a full-primary calculation giving \(B>2N+2\max(a,b)\) rules out
genuine residual degrees one and two even without a reducedness assumption.
If \(B>0\), it also rules out the empty residual, so it forces \(r\ge3\).
The congruence \(r\equiv ab\pmod4\) may then strengthen this degree
conclusion, separately from the attachment argument.

The lower endpoint in (11) is the planar conic case. Intermediate even
values correspond to a double-line parameter \(e\), but (11) is a necessary
test, not an existence theorem for the corresponding complete intersection
or the fixed quartic partner.

There is also a global algebraic filter. A line or planar conic is ACM, so
linkage forces the full primary \(T\) to be ACM. For \(a,b\ge4\), its
minimal ideal resolution is respectively

\[
\begin{aligned}
0&\to S(-(a+b-1))^2
\to S(-a)\oplus S(-b)\oplus S(-(a+b-2))\to I_T\to0,\\
0&\to S(-(a+b-1))\oplus S(-(a+b-2))
\to S(-a)\oplus S(-b)\oplus S(-(a+b-3))\to I_T\to0.
\end{aligned}\tag{12}
\]

These are the standard dual mapping cones for linking a line or a
\((1,2)\) conic. Thus the small residual alternatives can be tested on
actual primary ideals and syzygies, not only on cycle degrees. Two skew
lines instead have Rao module \(k\) in degree zero, so \(T\) has Rao
module \(k\) in degree \(N\). No classification of all such primary
thickenings of the fixed \(C\) is asserted here.

## 5. Extension to a ribbon on any smooth residual support

The proof of (10) is not peculiar to lines. Suppose the genuine residual
\(Z\) is a ribbon of multiplicity two on a smooth integral support
\(A\subset\mathbf P^3\) of degree \(d\) and genus \(g\), with nilpotent
line bundle \(L\) of degree \(\ell\). Then

\[
0\to M\to N^*_{A/\mathbf P^3}\to L\to0,
\qquad \deg M=-4d-2g+2-\ell.
\]

At least one actual equation has a nonzero first symbol, a section of
\(M(a)\) or \(M(b)\), because \(Z\) is the full generic
multiplicity-two component. Its divisor of zeros is effective, so

\[
\ell\le (b-4)d-2g+2,
\qquad p_a(Z)=2g-1-\ell\ge4g-3-(b-4)d.
\]

Since \(r=2d\), equation (1) gives the conditional quantitative bound

\[
\boxed{B\le(a+2b-8)r-8g+8.}\tag{13}
\]

Whenever the coefficient is positive, this bounds \(r\) from below using
the full attachment and the support genus. For a line it recovers (11)'s
upper bound. The hypotheses require an actual ribbon on smooth support;
one cannot apply (13) to an arbitrary nonreduced residual with several
layers, singular support, or punctual conormal defects.

## 6. What the present work does and does not supply

The fixed Hilbert polynomial and Rao module of \(Y:C\) supply no extra
residual floor by themselves: they remain unchanged while its cycle
\((m-1)C+R\) redistributes degree. They become useful after controlling
the supported primary part or preserving the actual equation incidence.

The attachment budget gives genuine lower bounds when residual
reducedness, global functions, or a specific multiple-curve structure is
known. Actual equation symbols additionally constrain degree-two and
ribbon residuals, preventing the unbounded-negative-genus control from
being mistaken for an actual fixed-degree counterexample.

The remaining general quantitative task is to bound the full-primary
attachment and the negative-genus contribution for arbitrary residual
structures using actual equations. The source proves neither a positive
lower bound for every unrestricted characteristic-zero pair nor that any
numerically surviving small residual can be constructed. It isolates the
extra geometric information that makes liaison budgets quantitative.
