# Sections and modules through a finite normalization

This home gives the fixed-**degree** descent criterion, its rank-one module form and its support/blowup reformulation for an integral curve. It complements the all-degree relation-cone theorem [R-0003](../results/fixed_carrier_conductor_criterion.md); the latter is not a replacement for prescribed-degree membership or the full module factorization below. The original P-032 inverse-support omission is corrected explicitly. The main criterion, module factorization, degree formula and support-contained power proof are characteristic independent; the Cartier-index compression paragraph has its stated characteristic-zero/generic-regularity assumptions.

## Prescribed degree, full support, and the conductor square

Let k be algebraically closed. Let \(C\subset\mathbf P^3_k\) be an integral curve of degree \(d\), let
\(X=V(F)\) be an integral carrier of degree \(a\), and let
\(\nu:S=X^\nu\to X\) be its finite normalization.  Put
\(H=\nu^*O_X(1)\), and define the **entire** reduced inverse image
\[
W=(\nu^{-1}C)_{\mathrm{red}},
\]
including possible isolated points. Let \(\Gamma_1,\ldots,\Gamma_s\) be only its curve components, and set \(\delta_i=[k(\Gamma_i):k(C)]\).

A nonzero mate pulls back to a nonzero section whose zero scheme is an effective Cartier divisor on the integral normal surface S. Every minimal prime of a nonzero principal ideal in a Noetherian domain has height one. Thus an isolated zero-dimensional component of W forbids a mate in every degree on this carrier. Finiteness rules out contracted divisors, but does not rule out isolated inverse points.

Let \(Q_X=\nu_*O_S/O_X\), let
\(\mathfrak c=\operatorname{Ann}_{O_X}(Q_X)\), and define the full,
potentially nonreduced conductor schemes

\[
 \Delta=V_X(\mathfrak c),\qquad
 \widetilde\Delta=S\mathbin{\times}_X\Delta.
\]

For a fixed
\(b>0\), the following are equivalent:

1. there is a degree-\(b\) form \(G\), not divisible by \(F\), with
   \(|V(F,G)|=C\);
2. there are positive integers \(m_i\), an effective Cartier divisor
   \(A=\sum_i m_i\Gamma_i\) with \(|A|=W\), and an isomorphism
   \(\phi:O_S(A)\xrightarrow{\sim}O_S(bH)\) such that the transported
   canonical section \(s_A=\phi(1_A)\in H^0(S,O_S(bH))\) maps to zero in
   \(H^0(X,Q_X\otimes O_X(b))\);
3. the same divisor data exist and there is a section
   \(t_\Delta\in H^0(\Delta,O_\Delta(b))\) such that
   \(s_A|_{\widetilde\Delta}=\nu_\Delta^*t_\Delta\).

The choice of \(\phi\) changes \(s_A\) only by a scalar, so the descent
condition is independent of that choice.  It is essential here that \(A\),
not necessarily each prime \(\Gamma_i\), is Cartier. The sum expression can have support W only when W is pure dimensional; it cannot silently omit isolated inverse points.

A mate restricts to a section on \(X\), and its pullback divisor has support
exactly \(\nu^{-1}C\), giving condition 2.  Conversely, zero normalization
defect means that \(s_A\) descends to a section of \(O_X(b)\).  The restriction

\[
 H^0(\mathbf P^3,O(b))\longrightarrow H^0(X,O_X(b))
\]

is surjective because \(H^1(\mathbf P^3,O(b-a))=0\), so the descended section
has an ambient lift \(G\).  Finite surjectivity of \(\nu\) shows that its zero
support on \(X\) is exactly \(C\).  Conditions 2 and 3 are equivalent by the
conductor fiber-product sequence

\[
 0\longrightarrow O_X\longrightarrow
 \nu_*O_S\oplus O_\Delta\longrightarrow
 \nu_*O_{\widetilde\Delta}\longrightarrow0,
\]

tensored by \(O_X(b)\).

Every such mate satisfies

\[
 \boxed{ab=d\sum_i m_i\delta_i,}
\]

because

\[
 ab=(bH)\cdot H=A\cdot H
 =\sum_i m_i(H\cdot\Gamma_i)
 =d\sum_i m_i\delta_i.
\]

Indeed \(H^2=a\) because normalization is finite birational and \(X\) has
degree \(a\), while

\[
 H\cdot\Gamma_i
 =\deg((\nu|_{\Gamma_i})^*O_C(1))
 =\delta_i d.
\]

The degree \(\delta_i\) is the full function-field degree; no separability is
required.  Because normalization is finite, there are no omitted divisors
contracted to closed points.

The conductor condition is indispensable.  At the generic point of a
transversely cuspidal carrier, take

\[
 K[[t^2,t^3]]\subset K[[t]],\qquad K=k(C).
\]

The normalized divisor \(t=0\) is Cartier, but its section \(t\) does not
descend; only valuations in the semigroup
\(\{0,2,3,4,\ldots\}\) do.  Thus positivity, normalized divisor support, and
linear equivalence on \(S\) do not suffice.  The valuation vector must belong
to the multibranch value semigroup and pass conductor gluing.

There is also a module formulation, but it must retain conductor descent.  Set

\[
 M_A=\nu_*O_S(-A),\qquad
 I_A=O_X\cap M_A
\]

inside the total quotient sheaf \(K(X)\).  A mate with normalized divisor
\(A\) is equivalently an inclusion

\[
 O_X(-b)\hookrightarrow I_A\subset O_X
\]

whose induced map upstairs has image exactly \(O_S(-A)\).  Equivalently, one
may map first to \(M_A\), but the composite into \(\nu_*O_S\) must factor
through \(O_X\).  The conductor-supported quotient

\[
 M_A/I_A\hookrightarrow Q_X
\]

is exactly the missing descent information.  Omitting this factorization is
false already for
\(K[[t^2,t^3]]\subset K[[t]]\): the map \(1\mapsto t\) lands in \(tK[[t]]\)
and has the desired normalized divisor, but it does not land in the cusp
ring.  Thus normalized rank-one data alone are not a substitute for the
conductor condition.

The numerical Cartier-index compression in P-015 extends further than originally
stated.  Assume characteristic zero, allow \(C\) to be any integral curve,
and let \(X\) have minimum degree among **all integral carriers admitting a mate for C**, across all defining pairs. This is not a minimum only within one given pair or among all surfaces containing C.  If \(X\) is regular at the generic point of \(C\), then
\(C\cap\operatorname{Sing}X\) is finite and the same almost-Cartier argument
gives

\[
 eC\sim nH,\qquad n=\frac{de}{a}\in\mathbf Z_{>0},\qquad
 n\ge a,\qquad e\ge\frac{a^2}{d}.
\]

At the generic point the mate first gives a scalar relation
\(r[C]=b[H]\) in \(\operatorname{APic}X\), with \(dr=ab\).  Here \(e\) is the
lcm of the local orders of \([C]\) in the almost-Cartier groups at those
finitely many singular points, so \(e\mid r\) and \(eC\) is Cartier.  The
proof then uses the same
characteristic-zero torsion-freeness of
\(\operatorname{Pic}X/\mathbf ZH\) as P-015.  The inequality n≥a uses the degree-n lifted section and factor lemma from [minimum actual-carrier compression](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#canonical-compression-on-a-minimum-actual-carrier). Intrinsic singularities of
\(C\) on the regular locus of \(X\) cause no problem, since a height-one
prime on a regular surface is Cartier.  What fails when \(X\) is singular at
the generic point of \(C\) is the scalar relation \(r[C]=b[H]\); it must be
replaced by the branch-valuation vector and conductor condition above.

Finally, let
\(\mathcal J=(F,G)O_{\mathbf P^3}\) have no common factor, let
\(B=\operatorname{Bl}_{\mathcal J}\mathbf P^3\), and let \(W=B^\nu\).
Call a prime divisor \(E\subset W\) exceptional when
\(\operatorname{ord}_E(\mathcal J)>0\).  Then

\[
 \sqrt{(F,G)^{\mathrm{sat}}}=I_C
 \quad\Longleftrightarrow\quad
 \text{the set of exceptional-prime centers on \(\mathbf P^3\) is
 exactly \(\{C\}\)}.
\]

Here J is a regular sequence, so Y=V(J) is a pure complete-intersection curve and the exceptional divisor on its blowup is Proj(gr_J O)=P_Y(J/J²), a P1-bundle over Y. Each of its surface components dominates a curve component of Y. Finite normalization preserves component dimensions, so an exceptional prime upstairs cannot acquire a closed-point center; conversely every curve component is covered. This proves both implications, including the absence of additional point centers.  It checks
the support of a proposed pair but, like the graph formulation in P-029, does
not construct one.


## 2. Asymptotic descent when all nonnormality lies on C

**Conditional theorem.** Assume Supp(Q) is contained in C. Then the
following are equivalent:

1. C has an STCI mate on X, of some positive degree;
2. there are b>0 and an effective Cartier divisor A on S such that
   |A|=W and O_S(A) is isomorphic to O_S(bH).

Necessity follows by pulling back a mate. For sufficiency transport
the canonical section of A to s in H0(S,O_S(bH)). The conductor c is
an ideal both in O_X and in nu_*O_S: locally for A subset B,
c={a in A : aB subset A} satisfies cB=c, hence nu_*c_S=c.
Its ideal on S, denoted c_S,
has zero set contained in W, since Supp(Q) is contained in C.

Let I_A=O_S(-A). Since V(c_S) is contained in V(I_A), locally
I_A is contained in radical(c_S). Noetherianity and quasi-compactness
give a single positive N with

    I_A^N contained in c_S.

In each trivialization of O_X(b), the coefficient of s^N therefore
belongs to the conductor. It belongs to O_X; these coefficients glue
because the trivializations are pulled back from X. Hence s^N descends
to t in H0(X,O_X(Nb)). The restriction map

    H0(P3,O(Nb)) -> H0(X,O_X(Nb))

is surjective, since H1(P3,O(Nb-deg F))=0. An ambient lift G has zero
set C on X, by finite surjectivity and |V(s^N)|=W. This is the required
pair (F,G). The proof uses no Frobenius and works in all characteristics.

This removes the **existence of some mate** conductor obstruction for
carriers whose nonnormal locus is entirely supported on C. It does
not remove conductor descent at a prescribed degree and does not
produce the requisite positive Cartier divisor or its linear equivalence.
Additional nonnormal curves away from C remain a genuine loophole.

## 3. Exact control example already present in the checkout

The exact [conductor control verifier](../computations/verify_general_conductor_power.py) reconstructs
the cubic pinch surface

    X: x^2 w-y^2 z=0

and its smooth-scroll normalization with affine chart

    (x,y,z,xi,w)=(u,ur,1,r,r^2).

The marked twisted cubic is

    [s²(t−s):st(t−s):s²(s+t):t²(s+t)].

The four linear forms z−x, z+x, 2y+z+x and 2w−2y−z−x transform this parametrization into 2[s³:s²t:st²:t³], so in characteristic different from two it is a projective copy of the twisted cubic. Its full pulled-back ideal on the normalization chart is

    (h u,h(r+1))=(h) intersect (u,r+1),
    h=r-1-u(1+r).

The two factors are comaximal because h(0,-1)=-2. This example requires
characteristic different from two; the verifier works over Q. Thus the preimage
contains the divisor h=0 and an isolated reduced point (u,r+1).
The obstruction in section 1 already excludes this fixed carrier.
The verifier also checks that this same twisted cubic is STCI on
another carrier by the standard degree-(2,3) pair. Its existence must
remain visible: the obstruction is carrier-specific.


The support-contained proof is a direct global conductor-ideal power argument; it does not discard nilpotents or infer section descent from numerical equivalence. Its control is a twisted cubic on a specific singular carrier, while the same curve admits the corrected-square degree-(2,3) construction on a different carrier. Thus the isolated inverse point excludes that carrier rather than the curve.

## Consolidation review

Independent reconstruction compared the full original prescribed-degree proof and support-contained descent source, including the corrected entire inverse support, module factorization, inseparable degree formula and complete normalized-blowup center argument. It checked the explicit isolated-point twisted-cubic control against its retained exact verifier and preserved its characteristic restriction. The source record and duplicate support note are superseded by this mathematical home; the checker remains necessary support and no other split-sextic source is retired by this review.
