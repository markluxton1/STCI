# Independent audit: special sections and their STCI scope

Date: 2026-10-24. Reviewer: independent agent stci_final_audit.
Review target: Sections 1 and 7–13 of
[the special-lines research note](2026-10-24-special-lines-planes-research-note.md).
Status: **PASS for these scoped statements and their limitations;
research evidence only, not canonical promotion or an STCI exclusion**.

The reviewer read [INDEX](../INDEX.md) first and then the exact records
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md),
[STCI-R-0001](../results/quartic_carrier_exclusion.md), and
[STCI-R-0019](../results/quasiprimitive_residual_cycles.md).
Their accepted normal splitting/degree and carrier conclusions were used as
premises. None of their proof computations was rerun. The arguments below
were reconstructed independently; agreement of agents or a passing script
is not substituted for proof.

## 1. Proper intersection and actual local lengths

Nonzero homogeneous forms with no common surface component are a regular
sequence in the polynomial ring of projective three-space. Their intersection
is a pure one-dimensional Cohen--Macaulay complete intersection, with
\([Z]=m[C]+\mathcal R\) and \(de=4m+\deg\mathcal R\).
The qualification that a plane contain no residual component is necessary
and retained. Residual intersections at points already on \(C\) must also
be retained. The note does not infer a downstairs residual curve from an
exceptional vertical cycle.

Under sole support, at each closed \(p\in C\), the local ring
\(B=\mathcal O_{Z,p}\) is Cohen--Macaulay of dimension one with one minimal
prime. A plane equation \(h\) is a parameter and nonzerodivisor, since no
plane contains this nonplanar curve. Multiplicity associativity and the
Cohen--Macaulay parameter-length formula give

\[
\ell(B/hB)=e_h(B)
=\ell(B_{\eta_C})e_h(\mathcal O_{C,p})
=m\operatorname{ord}_p(h|_C).
\]

This proves the actual local lengths \(3m,m\), \(2m,2m\), and \(4m\).
Neither restricted equation is zero and they have no common plane curve
component, since either failure would put a plane curve inside \(Z\).
The same quotient length is their local plane intersection multiplicity.
This argument requires no generically curvilinear algebra or saturated flag.
The note correctly distinguishes it from conditional R0019 formulas and
does not infer an ideal or Hilbert function from the length.

## 2. Tangency, local examples, and global singularities

The plane intersection length is at least the product of the two germ
multiplicities, with equality exactly when the tangent cones have no common
linear factor. For smooth germs the length is the contact order. The note
correctly distinguishes a smooth plane section from a section by the ambient
surface's tangent plane.

The local model
\[
F=x,\qquad G=x+y^m,\qquad H_r:y+t^r=0
\]
has sole reduced support \(C=V(x,y)\), generic length \(m\), two smooth
ambient surfaces, and smooth plane germs with contact exactly \(rm\).
The thickness-four examples \((x,y^4)\), \((x^2,y^2)\) yield different
plane embedding dimensions despite identical lengths \(4r\). These are
local tests, not projective witnesses for the fixed quartic.

For \(m>1\), independent generic first conormal symbols would generate the
maximal ideal of the transverse regular local ring and force colength one.
Their wedge therefore vanishes generically, hence identically on \(C\).
Where both symbols are nonzero the tangent planes agree. Zero symbols,
including identically zero symbols, are correctly distinguished.

The global singularity paragraph also passes. If \(X=V(F)\) were smooth
along all of \(C\), then \(C\) would be Cartier on a smooth neighborhood in
\(X\), and \(G|_X\) would have divisor exactly \(mC\) there. Restriction
to \(C\) gives
\[
\mathcal O_C(e)\simeq N_{C/X}^{\otimes m},\qquad
4e=m(14-4d),
\]
using the accepted normal degree fourteen and the smooth hypersurface
normal sequence. Combining with \(de=4m\) gives \(16=d(14-4d)\).
For positive integral \(d\) the right side has maximum twelve, so there is
no solution. Each hypothetical surface is singular somewhere on \(C\).
This does not locate the singularities or force a common singular point.
It is the standard global adjunction argument, not an exclusion of the
remaining higher-degree singular carriers.

The reviewer suggested changing the local phrase “does not force ambient
singularities” to “does not force an ambient singularity at the point of
concentration.” The author applied this clarification, so the local
examples and global adjunction conclusion are visibly compatible.

## 3. Lines and residual divisors on the quadric

For two nonzero restrictions to a line, the common zero scheme is the
divisor of their gcd. Since \((F,G)\subset I_C\), it contains \(C\cap L\).
Sole support gives no other support, and its degree is at most
\(\min(d,e)\). Individual restrictions can have noncommon additional roots.
If one restriction is zero, the other is nonzero and its entire degree
divisor is supported on \(C\cap L\).

There is no plane-like multiplication-by-\(m\) formula for line sections.
In the local model, the actual transverse line \(t=y=0\) has quotient
length one for every \(m\). This suffices to disprove the local algebraic
implication and is not presented as a special global projective line.

On \(Q\), if \(q\) divided one defining form, the other restriction would
have a divisor solely supported on \(C\), forcing
\((e,e)=b(1,3)\), impossible in positive degree. Thus both restrictions
are nonzero, and
\[
\operatorname{div}F_Q=aC+R_F,\quad
R_F=(d-a,d-3a),\quad 1\le a\le\lfloor d/3\rfloor.
\]
The residuals contain no \(C\) component by definition; sole support
excludes any other common component, and their proper intersection is
supported on \(C\). The quadric pairing gives
\[
\deg(R_F\cdot R_G)
=(d-a)(e-3b)+(d-3a)(e-b)
=2de-4(db+ea)+6ab,
\qquad R_F\cdot C=4d-6a.
\]
The distinction between orders on \(Q\) and ambient normal orders is
retained. No residual scheme is identified with a first-normal defect
without the extra R0019 hypotheses.

## 4. Saturated normal count and the explicit residual example

The degree-four osculating vector is everywhere nonzero, lies in
\(\Omega_{\mathbf P^3}(1)|_C\) by the Euler relation, and is conormal by
tangency. It gives
\(\mathcal O(-4)\subset E(4)\), hence \(L_{\rm osc}=\mathcal O(-8)\).
For a nonzero first symbol, removing its actual zero divisor \(A_F\)
gives \(L_F=\mathcal O(a_F-4d)\). If the saturated directions do not agree
identically, their wedge has divisor degree
\[
\deg\det E-\deg L_F-\deg L_{\rm osc}
=-14-(a_F-4d)+8=4d-6-a_F.
\]
The identically zero-symbol, singular-point, and identical-direction
qualifications are necessary and retained. Proportional generic symbols
have the same saturated subline, so \(4d-a_F=4e-a_G\). In the accepted
balanced bundle the direction-map degree is \(4d-7-a_F\), without a
degree-at-most-two bound.

Independently, set \(f_i(u)=F_{x_i}(1,u,u^3,u^4)\). Euler and
differentiation along \(C\) give
\[
f_0+uf_1+u^3f_2+u^4f_3=0,\qquad
f_1+3u^2f_2+4u^3f_3=0.
\]
Their paired-point derivative is \(4u^3(f_2+2uf_3)\); the reversed
chart gives the factor \(s^3\). This proves the homogeneous degree
\(4d-6\) quotient independently of symbolic computation.

For the cubic in (10.5), the displayed gradient is correct and never
vanishes on \(C\), including infinity. Its coincidence polynomial is
\(s^6+t^6\), with six distinct zeros in characteristic zero.
The pair \((F,x_0F+q^2)\) has ideal \((F,q^2)\), with common saturated
direction of degree five. Its quadric factorization is
\[
F_Q=(a^2-b^2)(bc^3-ad^3).
\]
The two distinct residual ruling fibers and \(C\) are generically reduced
in \(V(F,q)\); replacing \(q\) by \(q^2\) doubles every generic
multiplicity, proving the full cycle (10.6). This is a proper pair with
visible residual support, not an STCI witness. The note correctly limits
the type of small-bound assertion that this example refutes.

## 5. Universal incidence cycle and algebra bundle

Every member plane is a proper section of sole-support \(Z\).
The universal plane is fiberwise a nonzerodivisor on
\(Z\times\mathbf P^1\), so its relative Cartier divisor is flat over
the parameter line. Fibers are finite of length \(de\); properness and
finite fibers give finiteness. Hence this is finite flat of rank \(de\).

Cartier intersection of
\([Z\times\mathbf P^1]=m[C\times\mathbf P^1]\) with the universal
plane gives \(m\) times its divisor on the reduced product:
\(3\Delta+\Gamma_\iota\) or
\(2\Gamma_{c_+}+2\Gamma_{c_-}\).
This is a fundamental cycle identity in the ambient product and does not
make the thickened incidence scheme a divisor on the reduced product.

For degree-\(k\) plane families, let
\[
A=\chi(\mathcal O_Z)=de(4-d-e)/2,\qquad
B=\chi(\mathcal O_Z(-1))=de(2-d-e)/2.
\]
The displayed universal-plane exact sequence gives
\(\chi(\mathcal O_W)=A-(1-k)B=de+kB\).
A rank-\(de\) bundle on \(\mathbf P^1\) has Euler characteristic
\(de+\deg\mathcal B\), proving
\[
\deg\mathcal B=-kde(d+e-2)/2.
\]
For \(k=4\) this is exactly (11.2). Rank, degree, and cycle are formal
compatibility conditions, without an established incompatibility.

## 6. Evidence and outcome

The new exact identity script was rerun with
/tmp/stci-z4-env/bin/python and returned **PASS**, using SymPy 1.14.0.
The local models, normal count, explicit residual pair, and global
adjunction were also reconstructed algebraically above. Computation
supports the displayed identities and is not proof of a new exclusion.

No substantive mathematical correction was required in the reviewed
Sections 7–11. The local/global singularity wording clarification was
applied. The separate geometry audit governs the dual singular-locus
classification, which is not an input to the STCI statements checked here.

Section 1 accurately retains the scopes of R0020, R0001, and R0019.
Sections 12–13 leave the unrestricted STCI problem open, do not propose an
unsupported inequality, and distinguish the residual example from sole
support. The remaining dependency is global control of actual homogeneous
equations, higher normal data, and embedded gluing. These reviewed
proposals have not been promoted to canonical result records.
