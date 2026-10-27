# Scope audit: the selected endpoint-four carrier has a nonsplit generic node

Date: 2026-10-26. Reviewer: `pencil_geometry`, independently reconstructing
the local-to-global implication. **Completed fixed-carrier scope bridge,
with two exact finite certificates; provisional research, not canonically
promoted.** The local node lemma and the modular-to-characteristic-zero
argument are distinct from the finite rank computations. This final audit
starts no new computation or research lane.

## Validated jet-kernel input and independent finite evidence

The selected rational sextic is
\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3,
\quad q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2.
\]
The [actual-sextic note](2026-10-25-endpoint4-actual-sextics.md) uses the
following completed finite input:
\[
\{G\in H^0(\mathbf P^3,\mathcal O(16)):
G_\eta\in(F_*)+\mathfrak m^{12}\}
=F_*H^0(\mathbf P^3,\mathcal O(10)).
\tag{1}
\]
The evidence consists of two implementations:

* The [Macaulay2 certificate](../computations/endpoint4_fixed_m2_2026_10_25.m2),
  its [execution metadata](../computations/endpoint4_fixed_m2_2026_10_25.json),
  and [log](../computations/endpoint4_fixed_m2_2026_10_25.txt) record a
  \(690\times969\) matrix of rank 683 over \(\mathbf F_{65521}\),
  rank 286 for the known degree-ten multiples, and rank zero for their
  product with the jet matrix.
* The primary's [independent explicit normal-division implementation](../computations/endpoint4_fixed_jet_independent_2026_10_26.py)
  and [output](../computations/endpoint4_fixed_jet_independent_2026_10_26.json)
  construct the quotient coordinates separately, recover rank 683,
  and annihilate all 286 known multiples at every sample.

A failed intermediate annihilation check was traced to a multiline
Macaulay2 assignment that included only the first two terms of the global
carrier. Parenthesizing the whole assignment restored all four terms;
the corrected checks above pass, and the implementation correction is
preserved in the metadata. The failed check is not evidence for (1).

Here is the rank-lifting argument, separately from the computations. Over
\[
B=\mathbf Z[1/2,z,z^{-1},(1+z^2)^{-1}],
\]
the coefficient \(z^8(1+z^2)\) of the quadratic \(u^2\) term is a unit.
Explicit normal division modulo \(\mathfrak m^{12}\) gives the free
23-element basis
\[
1,v,\ldots,v^{11},\quad u,uv,\ldots,uv^{10}
\]
for \(B[u,v]/(F_*,\mathfrak m^{12})\). Its rule replaces \(u^2\)
by a multiple of \(v^2\) plus higher-total-degree terms; higher terms
terminate at degree twelve. More explicitly, the 78 truncated monomials
have 55 relations given by \(F_*\) times monomials of degree at most
nine. Ordering first by increasing total degree and then by decreasing
\(u\)-exponent makes their 55 pivot coefficients units; the nonpivot
monomials are exactly the displayed 23. Thus the remainder maps of all 969 global
monomials have coefficients in \(B\). A generic formal compatibility
identity makes that rational remainder identically zero and therefore
zero under each good specialization. The samples \(z=1,\ldots,30\)
are good modulo 65521: neither \(z\) nor \(1+z^2\) vanishes there.

The modular rank 683 is consequently a lower bound for the rational
specialized matrix rank. Its kernel has dimension at most 286. The 286
global multiples are independent, lie in the generic compatible kernel,
and are killed by every sample map, so both the sample kernel and the
generic compatible kernel are exactly this known space. This proves
(1); the constant rational coefficient maps and their ranks persist
under every characteristic-zero extension of the coefficient field.
Neither implementation substitutes free \(k(z)\)-coefficients for the
constant global source. This audit reads the persisted finite evidence
and independently reconstructs its scope bridge; it does not rerun those
completed rank computations.

Let \(k\) be a characteristic-zero coefficient field, \(K=k(z)\), and
\(A=K[[u,v]]\), with \(\mathfrak m=(u,v)\), in the actual balanced chart
\[
(x_0,x_1,x_2,x_3)=(1,z,z^3+v,z^4+u+\tfrac32zv).
\]
The quadratic term of \(F_*\) is
\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\tag{2}
\]
The discriminant square class is \(1+z^2\). This is nonsquare in \(K\):
over an algebraic closure of the constant field the polynomial has two
simple zeros, whereas a rational square has even valuations. Thus the
nonsplit property persists under every characteristic-zero extension of
the constant field. Extending the function field to its algebraic closure
would lose precisely the Galois constraint used below and is not the
allowed global coefficient operation.

## The nonsplit-node lemma, with finite-length hypotheses

Suppose \(G\in\mathfrak m\) and \(A/(F_*,G)\) has finite length. Then there
is an integer \(n\ge1\) such that
\[
\operatorname{length}_A A/(F_*,G)=2n,
\qquad G\in(F_*)+\mathfrak m^n.
\tag{3}
\]
More precisely, the largest power in this membership condition is \(n\).
Here finite length is essential: if \(G\) vanished identically on a
formal branch after splitting, intersection length would not be finite.

To reconstruct the assertion, pass to the finite separable quadratic
field
\[
L=K(\sqrt{1+z^2}).
\]
Weierstrass preparation in \(u\) is available because the coefficient
of \(u^2\) in (2) is a unit of \(K\). Its monic quadratic has discriminant
\(v^2\) times a unit whose leading coefficient becomes a square in \(L\).
The square root of the remaining unit, normalized to have constant term
one, exists by the formal Hensel recursion in characteristic zero.
Consequently \(F_*\) factors over \(L[[u,v]]\), up to a unit, as
\[
(u-\phi_+(v))(u-\phi_-(v)),\qquad
\phi_\pm(v)=\pm\frac{z}{2\sqrt{1+z^2}}v+O(v^2).
\]
The two smooth branches are transverse, and their formal series are
exchanged by the nontrivial element of \(\operatorname{Gal}(L/K)\).
Since \(G\) is defined over \(K\), its branch restrictions are Galois
conjugate. Their finite orders are therefore the same integer \(n\).

Intersection length is the sum of these branch orders. For an elementary
way to see this without discarding the node's gluing, the prepared
quadratic quotient is free of rank two over \(L[[v]]\). The determinant
of multiplication by \(G\) is the product of its two branch restrictions;
the length of its cokernel is the \(v\)-order of that determinant, hence
\(2n\). Scalar extension from \(K\) to \(L\) leaves the numerical Artinian
length unchanged, when measured over the respective residue fields.

Membership can also be checked directly. Divide \(G\) by the prepared
quadratic, leaving a remainder \(a(v)u+b(v)\). The difference of the two
branch restrictions is
\(a(v)(\phi_+(v)-\phi_-(v))\). Both restrictions have order at least \(n\),
and the parenthesized factor has order one, so
\(a(v)\in(v^{n-1})\). It follows that \(b(v)\in(v^n)\). The remainder is
therefore in \((u,v)^n\). Conversely every element of \((u,v)^n\) has
order at least \(n\) on each smooth branch. This establishes the precise
membership equivalence after splitting. Faithfully flat field extension
descends the membership to \(A\); alternatively the unique prepared
remainder is already defined over \(K[[v]]\).

This argument tests the potentially delicate edges: it uses actual
Galois-conjugate branches, finite intersection length, both branch orders,
and membership for the *whole formal ideal*. It does not infer a complete
initial ideal from the two individual leading symbols.

## Consequence for every proper degree-sixteen mate on this selected carrier

Let \(G\) be any homogeneous degree-sixteen form over \(k\) such that
\(W=V(F_*,G)\) is a proper complete intersection and contains the fixed
reduced quartic \(C\). Properness ensures finite generic transverse
length along \(C\). Completion preserves this length, and (3) says its
cycle coefficient is \(m_C(W)=2n\).

If \(n\ge12\), membership in (3) implies
\(G_\eta\in(F_*)+\mathfrak m^{12}\). The validated kernel equality (1),
which persists under characteristic-zero coefficient-field extension,
forces the global equality \(G=F_*H_{10}\). That pair is not proper.
Hence every proper pair in this precise fixed-carrier, fixed-degree scope has
\[
\boxed{m_C(W)=2n\le22.}
\]
Bézout gives \(\deg W=6\cdot16=96\). Its residual fundamental cycle
therefore has degree
\[
\boxed{\deg\bigl([W]-m_C(W)[C]\bigr)=96-8n\ge8.}
\tag{4}
\]
In particular, the residual cycle is nonzero. Equivalently, sole support
\(C\) would require \(m_C=96/4=24\), so \(n=12\), which (1) excludes.
Complete-intersection purity rules out hiding degree in isolated embedded
components instead of a positive-dimensional residual cycle.

This implication needs **neither** the full generic initial-CI type
\((2,12)\), saturated first relation, movement-two classification, nor
any assertion about other endpoint-four carrier parameters. Those
hypotheses explain the origin of \(F_*\), but its nonsplit generic node
and the validated fixed-carrier jet kernel suffice for (4). The
conclusion covers one selected sextic and degree-sixteen mates only.
The rest of the endpoint-four family and unrestricted STCI questions remain unchanged.
The bound is not claimed to be attained. The completed finite test and
this independently reconstructed scope bridge do not promote the selected
carrier conclusion to a canonical record or exclude any larger family.
