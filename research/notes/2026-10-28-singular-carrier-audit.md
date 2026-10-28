# Independent audit: prescribed A-type carriers and actual residual cancellation

Date: 2026-10-28. Reviewer: `blowup_linear_systems` research agent, independent
of the proposing `singular_carrier_construction` agent.
Source: [Prescribed singular carriers](2026-10-28-singular-carrier-construction.md).
**Outcome: PASS for the stated complex, sufficiently-high-degree construction,
local residual assertions, primitive genus calculation, and very-general
class-group application.** These are reviewed provisional deductions, not
canonical promotions or a construction of a sole-support pair.

I reconstructed the arguments below, including the marked curve, rather than
using the proposing agent's statement of success. No accepted proof or
inherited certificate was rerun. All checks are symbolic proofs in the stated
parameter ranges; no finite computation is substituted for those proofs.

## 1. Marked finite jets and the actual local Cartier index

The prescribed pair is

\[
R=\mathbf C[[t,y,z]]/(ty-z^r),\qquad C=(y,z),\quad r\ge2.
\]

The completed A-type class group is \(\mathbf Z/r\), and \((y,z)\) is a
generator. I checked the marked-generator statement independently against
[Brevik–Nollet, *Picard groups of normal surfaces*, Example 2.1(a)–(b)](https://arxiv.org/html/1208.0269v1#S2.SS1).
This is a statement about the specified ideal, stronger than identification of
an unmarked A-type singularity.

I reconstructed the source's formal elimination for
\(f=ty-z^r+h\), \(h\in(y,z)\cap\mathfrak m^{r+1}\).
At each total degree \(N\ge r+1\), a perturbation monomial with a \(y\)
factor is removed by changing \(t\) by a degree-\(N-1\) term. A remaining
monomial with a \(t\) factor also has a \(z\) factor and is removed by changing
\(y\) by a degree-\(N-1\) multiple of \(z\). The corrections preserve
\((y,z)\), have identity linear part, and affect only higher degrees after
the targeted term. What remains is \(-z^r\) times a one-variable unit,
absorbed by an \(r\)-th root. Completeness gives a convergent formal
automorphism in the maximal-ideal topology. Dividing an initial unit
coefficient of \(f_0\) does not alter the error ideal.

There is a second independent way to protect the mark. Parameter Morse
splitting in the variables \((t,y)\), retaining \(z\), puts \(f\) into
\(TY+g(z)\), with \(g\) of exact order \(r\). The changes can have identity
linear part. On the original \(C\), \(z=0\), and \(T|_C\) has nonzero linear
\(t\)-term. Since \(T|_C\,Y|_C=0\) in the domain \(\mathbf C[[t]]\), one
has \(Y|_C=0\). Thus \(C\) becomes \((Y,z)\); the generator class has been
retained. This confirms that unmarked finite determinacy is not being used
as a substitute for a statement about the pair.

The algebraic local index is indeed exactly \(r\). Completion takes the
rank-one reflexive module representing \(rC\) to a free module of rank one;
faithfully flat descent of freeness makes the algebraic module free. For
\(0<m<r\) its completed class is nonzero and hence it cannot have been free
before completion. Equivalently use the injection of algebraic local class
groups into completed local class groups recorded in the cited primary
paper. The source correctly uses the marked generator for this conclusion.

## 2. Finite-jet global realization

The base ideal prescribed at \(P\),

\[
I_{B,P}=(ty-z^r)+\mathfrak m_P^r I_{C,P},
\]

is a coherent global prescription: it is the inverse image of a submodule
in the finite-length quotient \(I_C/(I_CI_P^r)\). Away from \(P\) it is just
\(I_C\). Algebraic regular parameters with \(I_C=(y,z)\) exist because the
ambient space and the curve are smooth. Only their finite jets enter the
prescription.

For sufficiently large degree, Serre generation supplies both the nonzero
\(ty-z^r\) coefficient and the needed conormal evaluations elsewhere.
The open condition of a unit coefficient gives §1's completed marked pair.
Off \(C\), usual Bertini applies. At a point of \(C\setminus\{P\}\),
the evaluation map onto a two-dimensional conormal fiber is surjective;
the incidence of a point and a section with zero first normal has codimension
two in the section space, while the point varies in dimension one. The
bad incidence therefore cannot dominate the section space. This justifies
simultaneous smoothness all along the punctured curve, not merely at each
individually chosen point.

The resulting hypersurface has precisely the isolated prescribed A-type
singularity. A reducible projective hypersurface would be singular along
the curve where two surface components intersect; a nonreduced one would
be singular generically along a surface. Both contradict the established
singular locus. Thus the global surface is integral, and its isolated
normal A-type germ plus smooth complement make it normal.

This proves actual homogeneous carriers for every \(r\), with a sufficient
but unspecified large-degree threshold depending on the prescribed base
ideal. The result is not a formal germ without algebraization, and it is
not an explicit assertion in a particular small degree.

## 3. Symbolic powers, residual smoothness, and the two attachment lengths

At the marked completed stalk, for \(1\le m\le r\), the ideal
\(J_m=(y,z^m)\subset R\) is \((y,z)\)-primary: its quotient is
\(\mathbf C[[t,z]]/(z^m)\), whose only associated prime is \((z)\).
At the generic curve point \(t\) is a unit, so \(y=z^r/t\), and this ideal
has valuation \(m\). Hence it is the symbolic ideal of the divisorial
multiple \(mC\). For \(m=r\), \((y,z^r)=(y)\) on the surface. This also
checks the expected Cartier transition at the local index.

For \(m<r\), eliminating \(y\) from \(g=y+z^m\) gives
\(z^m(t+z^{r-m})\). The factors \(z\) and \(t+z^{r-m}\) are relatively
prime in \(\mathbf C[[t,z]]\). Thus the full primary component is
\((y,z^m)\), and the residual is the smooth parameterized curve
\((y+z^m,t+z^{r-m})\). On it the ideals of \(C\) and \(T_m\) restrict to
\((z)\) and \((z^m)\), respectively. The marked and full attachment lengths
are exactly \(1\) and \(m\).

The unit-coefficient variant is equally valid: for
\(g=A y+Bz^m\), \(A,B\) units, the implicit-function theorem first gives
\(y=z^m u(t,z)\) with \(u\) a unit. The residual equation is
\(t u-z^{r-m}=0\), whose \(t\)-derivative is nonzero at the origin. The
same ideal restrictions give lengths \(1,m\). In particular this is an
open condition in the two minimal-generator coefficients, rather than a
special section that may disappear under globalization.

For a fixed constructed normal carrier, a large twist of its coherent
divisorial ideal is generated. A further twist separates points and first
jets on the smooth punctured surface: choose a generating section nonzero
at a point and multiply it by ambient linear forms. It also gives a
birational map on that surface, by ratios of linear forms times such a
section. Bertini smoothness and irreducibility for this mobile system give
a smooth integral residual away from \(P\); the local calculation supplies
smoothness of its closure at \(P\). Generation at \(P\) supplies the open
unit coefficients above.

The divisor has exact generic multiplicity \(m\), and its full primary
component is \(T_m\), not an arbitrary lower witness. Since
\(H^1(\mathbf P^3,\mathcal O(b-a))=0\), its surface section lifts to an
actual homogeneous mate. It is nonzero on the integral surface, giving a
proper pair. These arguments establish all existence assertions of §4 in
their sufficiently-large-\(b\) range.

The local class identity \([D]_P=-m[C]_P\) explains the forced residual
through \(P\) whenever \(r\nmid m\). A divisor missing \(P\) has zero local
class. This is actual downstairs residual geometry, with no inference from
an exceptional vertical curve.

## 4. Primitive layers and the genus/attachment formulas

This part required a separate check: the local Cartier index is not itself
the conormal degree. The first-normal section of the carrier has precisely
a simple common zero at \(P\). In the marked coordinates its coefficients
are \((t,0)\) to first order; the allowed higher perturbation adds terms
of order at least \(t^r\) on \(C\). Elsewhere the carrier is smooth. Its
saturated relation line in \(N_C^*\) is therefore
\(\mathcal O_C(-a)(P)\), of degree \(-4a+1\).

For \(2\le m\le r\), the local ambient ideal of \(T_m\) is
\((y,z^m)\), so the curve is primitive everywhere. The quotient of
\(N_C^*\) by that saturated relation is its primitive conormal line \(L\).
Using the accepted determinant degree \(-14\),

\[
\deg L=-14-(-4a+1)=4a-15.
\]

The nilpotent associated-graded pieces are \(L^i\), \(0\le i<m\), since
locally the nilpotent parameter is the single coordinate \(z\). Additivity
of Euler characteristic on \(C\cong\mathbf P^1\) gives

\[
\chi(\mathcal O_{T_m})=m+
\frac{m(m-1)}2(4a-15),
\]

which is exactly the source's genus formula. For \(m=1\), it gives the
reduced rational quartic directly, so no nonexistent first nilpotent layer
is required.

Finally substituting this genus and \(\deg T_m=4m\) into the inherited
full linkage attachment identity gives

\[
\begin{aligned}
\operatorname{length}(T_m\cap D)
&=(a+b-4)4m-2p_a(T_m)+2\\
&=m\bigl(4b+1+m(4a-15)\bigr).
\end{aligned}
\]

Its local summand at \(P\) is \(m\), while reduced attachment there is
one. The source preserves this distinction and does not substitute the
full global attachment length for a determinant divisor on reduced \(C\).

## 5. Literal Noether–Lefschetz scope and the October 2026 paper

I opened the primary full text of
[Brevik–Nollet, *Noether-Lefschetz theorem with base locus*, Theorem 1.1](https://arxiv.org/html/0806.1243v3#S1.Thm1).
It requires a complex base scheme of dimension at most one, embedding
dimension at most two off finitely many points, degree at least four,
generation of \(I_B(a-1)\), and either the stated reduced condition or a
nonzero section of \(I_B(a-2)\). Here the sole curve support is \(C\), the
only possible embedding-dimension-three point is \(P\), and the last two
conditions hold for a sufficiently large twist. Its conclusion is the
**very-general** free Weil class group generated by \(H,C\). This verifies
the source's application, including its necessary qualification.

The unique singular point has algebraic local class group \(\mathbf Z/r\)
and \(C\) maps to a generator, while \(H\) is Cartier. The kernel of the
local restriction is therefore \(\mathbf ZH\oplus\mathbf Z(rC)\), which
is exactly \(\operatorname{Pic}(S)\). A positive relation
\(n[C]=b[H]\) is absent on these very-general carriers even when \(r\mid n\).
This statement does not classify the class groups of special members or
give a uniform high-index exclusion.

I also independently opened the official full text of
[Brevik–Nollet, *Noether–Lefschetz theory and surfaces containing a multiple curve*, Theorem 1.1](https://doi.org/10.1017/nmj.2026.10139).
The publisher gives 19 October 2026 as the online publication date. The
theorem concerns a smooth complex threefold with \(H^1(\mathcal O_X)=0\),
a smooth connected curve, an ordinary ideal power \(I_C^q\), \(q\ge2\),
and a very-general sufficiently-high-degree containing surface. Its
conclusion identifies **Picard groups**. These containing surfaces are
nonnormal along the curve. The source correctly refrains from turning it
into a statement about all Weil or almost-Cartier multiples, arbitrary
special carriers, or the fixed quartic's STCI status.

## 6. Interpretation and remaining boundary

The source supplies a controlled positive family with arbitrary local
index and smooth actual residuals. The freedom to choose the index does
not supply a global positive divisor relation. Its very-general members
make that difference especially explicit. All degree thresholds remain
existential Serre/Bertini thresholds; no small-degree equation pair or
complete-absorption family is claimed.

No correction to the mathematical statements was required in this audit.
The necessary retained distinctions are: marked versus unmarked analytic
type; completion versus actual algebraic Cartier index; full primary versus
reduced attachment; Zariski general construction versus very-general
class-group theorem; and a Picard computation on nonnormal surfaces versus
a theorem about the full almost-Cartier group.

## 7. Root integration addendum: two later computations

Reviewer: root integration agent, after the original independent review.
Both additions pass reconstruction; this does not change canonical status.

For source §4.1 I substituted \(y=uz\) into the literal local pair and
removed one factor of \(z\) from each equation. Eliminating \(u\) gives
\(z^{m-1}(t+z^{r-m})\). The two relatively prime factors give exactly
the displayed primary ideal \((u,z^{m-1})\) and the residual transform.
On the other chart \(z=vy\), the second strict equation is
\(1+y^{m-1}v^m\), a unit on its exceptional divisor. Thus the
component count, the absence of an extra vertical fiber, and the actual
cycle \((m-1)e+\widetilde D\) follow from the local ideals. This is a
check of the graph formula with normal orders one, not a new homogeneous
globalization assertion beyond the original source.

For the Nagoya specialization in source §7, I checked the two literal
sufficient conditions in Remark 1.2 against the official full text. For
\(d\ge4q\), the generation twist is at least three. The second
condition has the nonzero section consisting of the \((q-1)\)-st power
of the containing quadric times an ambient form of degree
\(d-2q-2\ge0\). Hence the stated sufficient bound is valid. It gives
the paper's Picard-group conclusion for very general complex members,
not a bound for every singular carrier or an assertion about almost-Cartier
classes. The generation of \(I_C(3)\) is an inherited premise.
