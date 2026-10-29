# Independent audit of the one-binomial arithmetic bound

Started 2026-10-28; completed 2026-10-29. Reviewer:
`arithmetic_search/spreadout_audit`.

**Verdict: PASS, with the stated one-binomial scope.** The proposed
divisibility statement in the [arithmetic search note](2026-10-28-stci-search-arithmetic.md),
Section 3, holds for the fixed quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), over an algebraically closed field of
characteristic \(p>0\): if a homogeneous supported pair of degrees
\((a,b)\) has at least one binomial equation, then
\[
p\mid m_C=ab/4,\qquad ab\ge4p,\qquad\max(a,b)\ge p.
\tag{A1}
\]
The mate can be an arbitrary homogeneous polynomial. The argument does
not apply to two arbitrary non-binomial equations. The exact conclusion
\(\delta_{\rm bin}(p)=p\) for \(p\ge7\) follows by combining (A1)
with the inherited actual \((4,p)\) construction. These are reviewed
provisional deductions; this audit does not promote a canonical record
or change the unrestricted characteristic-zero status.

The separate [search-logic audit](2026-10-28-stci-search-logic-audit.md)
already records the all-pairs characteristic-limit equivalence and its
quantifiers. It is not reproved here. This audit concentrates on the new
binomial restriction, including arbitrary mates, reducible equations,
full inverse support, and the semigroup coefficient argument.

## 1. Reduction of an arbitrary binomial equation

Suppose \(V(F,G)_{\rm red}=C_0\), with positive homogeneous degrees.
Every irreducible factor \(H\) of \(F\) must contain \(C_0\).
Indeed, \(V(H,G)\subset C_0\). A common surface component is
impossible; otherwise the intersection of the two positive-degree
surfaces has a curve, whose support must be \(C_0\). Hence
\(H\in I_{C_0}\). The same observation rules out monomial factors,
because the curve lies in no coordinate hyperplane.

After cancelling any common monomial, a binomial containing the dense
torus of \(C_0\) is a scalar multiple of \(M_1-M_2\), where the two
monomials have disjoint support. Write its exponent difference as
\(d\mathbf v\), with \(\mathbf v\) primitive. The corresponding
primitive monomials \(U,V\) have equal restrictions to \(C_0\):
their exponent difference has zero image in the torsion-free parameter
lattice. Thus among the factors \(U-\zeta V\), indexed by the
distinct roots of unity appearing in \(U^d-V^d\), exactly the factor
with \(\zeta=1\) contains the torus of \(C_0\).

All factors must contain \(C_0\), so \(d=p^e\). Consequently
\[
F=cF_0^{p^e},\qquad F_0\text{ an irreducible binomial},
\qquad a=p^e a_0.
\tag{A2}
\]
In particular \((F_0,G)\) is itself a supported pair. Bézout gives
\(a_0b=4m_0\), with integer \(m_0>0\), and
\(m_C=p^e m_0\). This establishes the factor reduction needed to
transfer divisibility, rather than only a lower bound, to the original
degrees. A binomial with a common monomial or several distinct primitive
factors cannot occur in a supported pair.

## 2. Independent reconstruction of the mixed-support exclusion

Use the integer weight grading
\[
\operatorname{wt}(x_0,x_1,x_2,x_3)=(4,3,1,0).
\]
The toric ideal of \(C_0\) and \(F_0\) are homogeneous for this
grading. Put \(A=k[x_0,x_1,x_2,x_3]/(F_0)\), a graded domain,
\(g=G\bmod F_0\), and \(P=I_{C_0}/(F_0)\). Sole support means
\(\sqrt{(g)}=P\). Each nonzero weight component \(g_w\) belongs
to \(P\), so \(g_w^N=h g\) for some \(N>0\), \(h\in A\).

For a nonzero element of an integer-graded domain, let its width be the
difference between its largest and smallest occurring weights. The
extreme components of a product cannot cancel, so widths add. The left
side above has width zero, giving
\[
0=\operatorname{width}(h)+\operatorname{width}(g).
\]
Therefore \(g\) has only one weight. Choose the corresponding
weight component \(H\) of the original degree-\(b\) polynomial
\(G\). Then \(G-H\in(F_0)\), and
\((F_0,H)=(F_0,G)\). This preserves the actual homogeneous degree
and does not assume the mate was originally a binomial or an eigenvector.

If neither monomial of \(F_0\) is a pure power, both have at least
two variables. Then
\[
P_1=[0:1:0:0],\qquad P_2=[0:0:1:0]
\]
belong to \(V(F_0)\) and lie outside \(C_0\). Sole support forces
\(H(P_1)\ne0\) and \(H(P_2)\ne0\), so both \(x_1^b\) and
\(x_2^b\) occur in \(H\). Their weights \(3b\) and \(b\)
are distinct because \(b>0\), contradicting the single weight of
\(H\). The grading is by integers, not by integers modulo \(p\).

A pure power of an endpoint coordinate \(x_0\) or \(x_3\)
cannot form a nonzero homogeneous binomial relation: its weight is the
unique extreme at its standard degree. Thus, after coordinate reversal,
every admissible \(F_0\) has the form in the next section. This
reconstructs the carrier reduction independently of the OCR of
[Thoma (1989), Theorem 2.3](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections).
That primary paper uses the same convention of one binomial equation
with an arbitrary mate. No two-binomial hypothesis is imported.

## 3. Full inverse image under the monomial cover

Write
\[
F_0=x_1^{a_0}-x_0^{n_0}x_2^{n_2}x_3^{n_3},
\qquad n_0+n_2+n_3=a_0,
\qquad4n_0+n_2=3a_0.
\tag{A3}
\]
Thus \(n_2=3a_0-4n_0\), \(n_3=3n_0-2a_0\), and
\(2a_0/3\le n_0\le3a_0/4\). There is no integral solution for
\(a_0=1,2\), hence \(a_0\ge3\) and \(n_0\ge2\).
Primitivity gives
\[
\gcd(a_0,n_0,n_2,n_3)=\gcd(a_0,n_0)=1.
\tag{A4}
\]

The map
\[
\phi:\mathbf P^2\longrightarrow V(F_0),\quad
[U:V:W]\longmapsto
[U^{a_0}:U^{n_0}V^{n_2}W^{n_3}:V^{a_0}:W^{a_0}]
\tag{A5}
\]
is basepoint-free and finite: its image ring contains the three pure
\(a_0\)-th powers, and the ambient polynomial ring is finite over
that subring. Its image is the irreducible hypersurface \(V(F_0)\).

The full reduced inverse image of \(C_0\) is
\[
B=V^4-UW^3=0.
\tag{A6}
\]
For an independent check, on \(UW\ne0\) membership in \(C_0\)
also makes \(V\ne0\). Put \(z=V^4/(UW^3)\). Pulling back the
three relations
\[
x_2^4=x_0x_3^3,\qquad
x_1^4=x_0^3x_3,\qquad
x_1^3=x_0^2x_2
\]
gives respectively
\(z^{a_0}=z^{n_2}=z^{n_3}=1\). Now
\[
\gcd(a_0,n_2,n_3)
=\gcd(a_0,4n_0,3n_0)
=\gcd(a_0,n_0)=1,
\]
so \(z=1\), including in characteristics dividing some of the
exponents. This is the needed primitivity check; equality of the first
quartic relation alone would leave extra roots-of-unity sheets.

If \(UW=0\), the first relation forces \(V=0\), again giving
(A6). Conversely the parametrization
\([U:V:W]=[s^4:st^3:t^4]\) of (A6) maps to \(C_0\) with
parameters \((s^{a_0},t^{a_0})\). The binomial \(B\) is
irreducible in every characteristic, since its exponent difference is
primitive and the exponent of \(U\) is one. Thus this is the full
inverse support, not merely a generically selected sheet. This also
independently verifies the specialization of Thoma's Theorem 2.4 used
in the main note.

## 4. The missing coefficient and its scope

The pullback of the arbitrary mate has sole reduced support (A6), so
unique factorization in \(k[U,V,W]\) gives
\[
\phi^*G=c(V^4-UW^3)^N,\qquad a_0b=4N,
\qquad N=m_0>0.
\tag{A7}
\]
No monomial factor can be present: it would add a coordinate line to
the reduced zero support. Every monomial in the image ring has
\(U\)-exponent \(a_0r_0+n_0r_1\), with \(r_i\ge0\).
Since \(a_0\ge3\), \(n_0\ge2\), exponent one is absent.
In (A7) the coefficient of \(UV^{4N-4}W^3\) is \(-cN\),
so \(p\mid N\). Equation (A2) now proves (A1) for the original
pair. Since \(p\mid ab\), a prime divides at least one of \(a,b\),
yielding \(\max(a,b)\ge p\). The same coefficient argument in
characteristic zero excludes the entire one-binomial class.

The proof uses actual polynomials and their full support under a finite
map; it does not replace coefficients by arbitrary elements of
\(k(C_0)\). It imposes no assumption about a saturated first normal
relation, no smoothness of the carrier along \(C_0\), and no
classification of all arbitrary carriers. No countercase was found
within the asserted hypotheses.

## 5. A concrete characteristic-five comparison

The fixed quartic's inherited minimum mate degree is \(25\) in
characteristic five. The inherited cubic-carrier family has a smaller
maximum defining degree there. One explicit member is
\[
\begin{aligned}
F&=x_1^3-x_0^2x_2,\\
G&=x_2^{20}-3x_0x_1x_2^{13}x_3^5
 +3x_0^2x_1^2x_2^6x_3^{10}-x_0^5x_3^{15}.
\end{aligned}
\tag{A8}
\]
Its degrees are \((3,20)\). On \(x_0=1\), \(F=0\) gives
\(x_2=x_1^3\), and direct substitution gives
\[
G(1,u,u^3,v)=(u^4-v)^{15}\quad\text{in characteristic five}.
\]
Thus the affine reduced intersection is exactly
\([1:u:u^3:u^4]\). On \(x_0=0\), \(F=0\) gives
\(x_1=0\), and then \(G=x_2^{20}\); the only projective point
is \([0:0:0:1]\). This proves full projective support equality,
not only generic contact. Its generic thickness is \(15\), in
accord with (A1).

An independent Macaulay2 evaluation of these two displayed polynomial
identities returned:

```text
PASS char5 (3,20): affine restriction (u^4-v)^15; boundary restriction y^20; degrees 3,20
```

The exact [check script](../computations/verify_stci_search_binomial_2026_10_29.m2)
and its [saved output](../computations/verify_stci_search_binomial_2026_10_29.txt)
are preserved in the repository. Run:

```sh
/opt/homebrew/bin/M2 --script research/computations/verify_stci_search_binomial_2026_10_29.m2
```

The script was copied unchanged from the original temporary check and
rerun successfully on 2026-10-29 to save the output above. The exact chart
proof is self-contained; this computation checks the newly displayed
formula and does not replay inherited carrier proofs. This example
illustrates why fixed-quartic optimality does not bound the unrestricted
search.

## 6. A sharper small-prime consequence

The same audited argument yields the exact restricted minima
\[
\delta_{\rm bin}(2)=\delta_{\rm bin}(3)=4,
\qquad\delta_{\rm bin}(5)=20.
\tag{A9}
\]
For \(p=2,3\), a smaller maximum would force both degrees at most
three. No degree-one equation contains \(C_0\), an admissible
binomial cannot have degree two by Section 2, and \((3,3)\) has
degree product nine, not divisible by four. The inherited
\((4,4)\) and \((4,3)\) pairs attain four.

For \(p=5\), assume a binomial pair has maximum degree less than
20 and reduce to \(F_0\) as above. If \(n_2=0\), primitivity
forces the fixed quartic \((a_0,n_0,n_3)=(4,3,1)\), whose
inherited minimum mate is 25. If \(n_3=0\), primitivity forces
the cubic \((a_0,n_0,n_2)=(3,2,1)\). The endpoint monomial
\(U^NW^{3N}\) in (A7), since \(n_2>0\), forces
\(a_0\mid N\) and hence \(4\mid b\); then \(5\mid N\)
forces \(20\mid b\), a contradiction.

In the remaining case \(n_2,n_3>0\), the same endpoint gives
\(4\mid b\), so \(b\in\{4,8,12,16\}\). From \(5\mid a_0b\)
we obtain \(a_0\in\{5,10,15\}\). The interval in (A3) has no
integer solution for \(a_0=5\). For \(a_0=10\), its only
solution is \(n_0=7\). For \(a_0=15\), \(n_0=10\) is
nonprimitive, leaving \(n_0=11\). In both remaining cases
\(v_5(N)=1\). Therefore the coefficient with binomial index five
in (A7) is nonzero: writing \(N=5M\), it is the index-one
coefficient in \((V^{20}-U^5W^{15})^M\), with \(5\nmid M\).
It has \(U\)-exponent five, absent from the image semigroup
\(\langle a_0,n_0\rangle\), whose smallest positive element is
at least seven. This contradiction rules out maximum degree below
20, and (A8) attains it.

The only imported input in this small-prime sharpening is the reviewed
[fixed-quartic mate minimum](2026-10-05-positive-quartic-carrier-optimality.md)
and its [independent reconstruction](2026-10-05-foundational-frontier-audit.md).
The finite arithmetic cases above are proved explicitly, rather than
being presented as an incomplete enumeration.

## 7. What remains unresolved

The all-pairs minimum satisfies
\(\delta(p)\le\delta_{\rm bin}(p)\), which gives an upper bound,
not the lower bound needed for characteristic-zero nonexistence.
Nothing here reduces a general pair to a binomial carrier, preserves
properness through torus degeneration, or proves \(p\mid m_C\)
for two arbitrary non-binomial equations. A fixed-degree or
fixed-carrier computation remains a statement about its actual tested
locus. No unrestricted STCI conclusion follows from this audit.
