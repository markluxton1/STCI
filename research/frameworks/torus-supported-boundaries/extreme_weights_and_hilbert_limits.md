# Extreme weights and saturated Hilbert limits

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

## III. Extreme weights and full limits

### Restrictions on sole-support pairs

Suppose \(\sqrt J=P\). For each end of the weight range let
\(F_-,G_-\) denote the lowest nonzero components and \(F_+,G_+\) the
highest, with gcds \(h_-,h_+\). Hellus–Hübl's Theorem 1.2(a,b), for
this embedding over an algebraically closed field of characteristic
zero, gives
\[
 h_-,h_+\in P,\qquad
 \sqrt{(F_-,G_-)}=\sqrt{(h_-)},\qquad
 \sqrt{(F_+,G_+)}=\sqrt{(h_+)}.
\]
Both gcds are nonunits and each extreme pair has only height-one
minimal primes. This is a theorem about displayed components of a
hypothetical defining pair. [Hellus–Hübl, Theorem 1.2](https://arxiv.org/pdf/1312.7661).

Thoma's characteristic-zero bihomogeneous-carrier theorem concerns
smooth monomial space curves of degree greater than three. For \(C\)
the carrier condition is having one weight, and the trace argument
below verifies the exclusion with an arbitrary homogeneous mate over
the algebraically closed field \(k\). The earlier binomial-carrier
theorem likewise allows an arbitrary homogeneous mate and applies to
smooth nondegenerate monomial space curves other than the twisted cubic
in characteristic zero. [Thoma 1991](https://link.springer.com/article/10.1007/BF02568376) ·
[Thoma 1989, Theorem 3.1](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections).

Both equations of a hypothetical pair have at least two weights, and
at least one has at least three. The latter is Thoma's weight-count
restriction as recovered in Hellus–Hübl's Remark 1.4. Indeed, if each
equation had just its two extreme components, \(h_-,h_+\) would be a
weight-homogeneous pair with reduced support \(C\), since both contain
\(C\) and their common zeros lie in \(V(F,G)\). [Hellus–Hübl,
Remark 1.4](https://arxiv.org/pdf/1312.7661).

The repository trace restriction for this embedding gives \(ab=0\)
in \(k\) for a sole-support pair with at least one eigenform. It
therefore excludes this case in characteristic zero and forces
\(p\mid ab\) in characteristic \(p>0\). The trace proof also applies
under the two congruences \(F\equiv x_1^a\bmod x_0^2\) and
\(G\equiv x_2^b\bmod x_3^2\) after exchanging and rescaling the equations
as needed. An eigenform factor alone suffices for the characteristic-zero
exclusion by factor reduction. In positive characteristic that reduction
gives \(\max(a,b)\ge p\). A stable height-two homogeneous CI ideal with
radical \(P\) satisfies the trace restriction, since a character basis of
\(J/S_+J\) lifts to generators of the given ordinary degrees. The
extreme-component conclusion also holds in characteristic \(p>0\) under
\(p\nmid ab\). [Trace hypotheses and factor reduction](../../arguments/torus/equivariant_degree_bounds.md#the-bound-and-its-exact-large-prime-minimum) ·
[Equivariant generator
lifting and trace consequence](../../arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections) ·
[Prime-to-\(p\) extreme components](../../arguments/torus/equivariant_degree_bounds.md#extreme-components-of-arbitrary-presentations).

A separate bound for **proper sextic eigenpairs**, with or without
containment of \(C\), is that their transverse quotient on \(\Omega/T_C\)
has total length at most eight, sharply, over an algebraically closed
field of any characteristic. It leaves at least four degrees on the
coordinate boundary.
[Sharp sextic quotient bound](../../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound).

### First cancellation and the full homogeneous initial ideal

For the minimum weight, write \(F_-=h_-A\), \(G_-=h_-B\) with \(\gcd(A,B)=1\). The actual combination
\[
H_1=BF-AG=B(F-F_-)-A(G-G_-)\in J
\]
cancels the displayed lowest-weight products. Its first **nonzero** weight component belongs to the full \(\operatorname{in}_wJ\), but need not belong to \((F_-,G_-)=h_-(A,B)\). Membership in the latter requires both divisibility by \(h_-\) and membership of the quotient in \((A,B)\). When it does belong, further lifted syzygy cancellations may still create new initial generators. The maximal-weight case reverses the weight; normal-symbol cancellation requires compatible lifts in the actual global equation source, not merely \(k(C)\)-linear relations.

The [normal Koszul calculation](../../arguments/normal_koszul_cancellation.md) develops this cancellation mechanism; the [full sextic limit](../../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit) gives a concrete extra generator. Gröbner fans organize the weight initials of a fixed homogeneous ideal, whereas the normal filtration is a separate Rees construction. The [normal-cone base-change criterion](../../results/normal_cone_slice_specialization.md) distinguishes flat power quotients from arbitrary closed-fiber specialization; the [endpoint-lattice construction](generic_algebras_and_endpoint_contact.md#endpoint-lattices-and-contact) handles projective-image specialization.

### Opposite saturated Hilbert limits

The full weight initial ideal comes from contracting the translated ideal
after inverting the orbit parameter \(h\), or equivalently from
\(h\)-saturating the normalized equations. It retains the original graded
Hilbert function. Irrelevant saturation then gives the projective Hilbert
limit, with the same Hilbert polynomial. Coprime displayed initials already
give the full saturated CI limit by the regular-sequence argument.
[Construction and saturation](../../arguments/equations/global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit) ·
[Coprime sextic example](../../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit).

For sole support, the closed incidence
\(\mathcal I^N\subset\mathcal J\subset\mathcal I\) with fixed Hilbert
polynomial retains the support and generic length at both ends of the
same orbit. The incidence allows embedded points, and a fixed limit can
require additional generators. The CI test uses the minimal generator
spaces of the moving ideal, \(J'_d/S_1J'_{d-1}\). Occurrence of a
proposed pair of opposite limits remains a separate realization question.
[Closed incidence and both full limits](../../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits) ·
[Moving-ideal generator test](../../arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test).

