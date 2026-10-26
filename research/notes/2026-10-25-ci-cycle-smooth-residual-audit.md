# Independent audit of the explicit smooth residual example

Date: 2026-10-25. Reviewer: independent audit agent from the cycle notebook
team. Status: reviewed exact characteristic-zero coordinate example; not a
canonical promotion or a classification of complete intersections.

This audit follows [the repository retrieval protocol](../INDEX.md).
The existing geometry of the marked quartic is used as a premise, with
[R0021](../results/quartic_mu4_degeneration.md) fixing the original reference
pair. This audit concerns new computations, not a replay of that accepted
result. The broad adaptive residual question remains as stated in the
[valuative continuation](2026-10-25-ci-cycle-adaptive-valuative-notebook.md).

**Outcome.** The final explicit pair over \(\mathbf Q\) has exactly the
scheme union of \(C\) and a smooth geometrically integral residual curve
\(D\) of degree twelve and genus sixteen. Their scheme intersection consists
of eighteen distinct geometric points and avoids both distinguished endpoints.
Thus the smooth-residual comparison picture now has one reproducible exact
example; it is no longer only a general-pair deduction or an unexecuted
experiment. The assertions below use exact rational computations and their
geometric interpretation. No finite-field lifting is involved.

## 1. The precise final pair

Use
\[
C=[s^4:s^3t:st^3:t^4],\qquad
Q=x_0x_3-x_1x_2,
\]
\[
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,\quad
A=x_1^3-x_0^2x_2,\quad D_3=x_2^3-x_1x_3^2,
\]
and the actual quadrics
\[
H_0=x_0^2+x_1^2+x_2^2+x_3^2+x_0x_2+2x_1x_3,
\]
\[
H_1=2x_0^2+3x_1^2+5x_2^2+7x_3^2
    +x_0x_1+x_0x_3+x_1x_2+3x_2x_3.
\]
The audited pair is
\[
f=F+QH_0+2x_0A,\qquad
g=G+QH_1+3x_3D_3.
\]
All its coefficients lie in \(\mathbf Q\), both forms have degree four,
and every summand vanishes on the actual fixed curve. This is a pair of
global homogeneous forms, not a prescription of rational-function-valued
normal symbols.

In \(S=\mathbf Q[x_0,x_1,x_2,x_3]\), put
\[
J=(f,g),\qquad K=\operatorname{sat}(J:I_C),\qquad
T=\operatorname{sat}(K+I_C).
\]
The saturation is with respect to the irrelevant ideal. The recorded curve
ideal is
\[
I_C=(Q,A,x_0x_2^2-x_1^2x_3,D_3).
\]
It was already checked in the deformation laboratory; the current computation
uses that actual ideal throughout.

## 2. Independent exact reconstruction

The reviewer constructed a separate rational Macaulay2 computation from the
displayed equations before replaying the durable verifier. It checked:

- \(J\) has codimension two and degree sixteen.
- \(K\) is saturated, defines a projective scheme of dimension one, has degree twelve, and Hilbert
  polynomial \(12n-15\).
- The exact ideal identity \(J=I_C\cap K\) holds.
- The saturated ideal
  \(K+I_2(\operatorname{Jac}K)\) is the unit ideal.
- \(T\) has degree eighteen and
  \(\operatorname{sat}(T+I_3(\operatorname{Jac}T))=(1)\).
- Neither endpoint point ideal meets \(T\) projectively.
- \(H^0(\operatorname{Proj}(S/K),\mathcal O)=\mathbf Q\).

The independent suite returned
\[
\operatorname{codim}J=2,\quad \deg D=12,\quad
P_D=-27P_0+12P_1=12n-15,\quad
\deg T=18,\quad H^0(\mathcal O_D)=\mathbf Q^1.
\]
Here Macaulay2 uses \(P_0(n)=1\), \(P_1(n)=n+1\). Its sheaf cohomology
output is a rank-one module over \(\mathbf Q\); the Krull dimension of that
module is zero and must not be used as its vector-space dimension.

The durable
[Macaulay2 verifier](../computations/verify_ci_smooth_residual_example_2026_10_25.m2)
was then read and replayed. It contains the same final equations and all the
substantive assertions above. Its conclusion matches the independent
reconstruction.

## 3. Why the computations imply geometric smoothness and irreducibility

The residual construction is linkage to the locally Cohen–Macaulay curve
\(C\) inside a proper complete intersection. Its residual is an unmixed curve;
the checked union identity additionally excludes a hidden failure to recover
the total scheme. The Jacobian test uses the minors of size two, corresponding
to codimension two in projective three-space. Saturating to the unit ideal
means that the projective singular locus is empty. It is not merely the
absence of rational singular points.

This is an exact test over \(\mathbf Q\), a perfect field. The Jacobian
identities remain valid after extending scalars, so \(D\) is geometrically
smooth. The origin of the homogeneous affine cone is irrelevant to
projective smoothness and is precisely why saturation is used.

Smoothness alone would not prove geometric irreducibility: disjoint smooth
components could remain. The separate computation of \(H^0(\mathcal O_D)\)
closes that gap. Flat base change of cohomology under field extension gives
\[
H^0(D_{\overline{\mathbf Q}},\mathcal O)
=H^0(D,\mathcal O)\otimes_{\mathbf Q}\overline{\mathbf Q}
=\overline{\mathbf Q}.
\]
Thus \(D\) is geometrically connected. For the standard equivalence between
this global-section condition and geometric connectedness in the proper,
geometrically reduced setting, see
[Stacks, Lemma 33.9.5](https://stacks.math.columbia.edu/tag/0FD2).
A smooth curve over an algebraically closed field is regular, so distinct
irreducible components are disjoint. Connectedness then implies a single
irreducible component. This establishes geometric integrality, rather than
only primality over \(\mathbf Q\).

The Hilbert polynomial now yields genus sixteen because \(D\) is a smooth
connected curve. No inference of smoothness from its numerical polynomial
was made.

## 4. Eighteen reduced attachments really give eighteen nodes

The ideal \(T\) is the actual scheme intersection \(C\cap D\). Its projective
zero-dimensional scheme has degree eighteen. The rank-three Jacobian test,
again with projective saturation, proves geometric reducedness. Hence over
\(\overline{\mathbf Q}\) it consists of eighteen distinct points.

Both curves are smooth. At each attachment, reduced intersection length one
implies distinct tangent directions: if the residual tangent agreed with the
marked tangent, every normal equation of \(C\) would vanish to at least order
two on that residual branch. A length-one pullback would be impossible.
Their union therefore has an ordinary transverse node at each attachment.
The ideal equality \(J=I_C\cap K\) proves that this union is the full original
complete intersection.

The genus accounting independently matches:
\[
p_a(C\cup D)=0+16+18-1=33.
\]
There are no other singularities of this union because both components are
smooth and they are disjoint away from \(T\).

## 5. A separate check from the global first-normal sections

On \(x_0=1\), let \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\). Restricting the
two quadrics to \(C\) gives
\[
h_0=1+u^2+u^3+2u^5+u^6+u^8,
\]
\[
h_1=2+u+3u^2+2u^4+5u^6+3u^7+7u^8.
\]
The first-normal rows of the final pair are
\[
\sigma_f=(h_0-1)X+(-uh_0-2)Y,
\]
\[
\sigma_g=(h_1-3u^8-6u^9)X+
                 (4u^9+9u^{10}-uh_1)Y.
\]
The reviewer expanded their determinant independently, obtaining
\[
\Delta(u)=(u+2)h_1+u^9(1+3u)h_0-6u^8-16u^9-9u^{10}.
\]
Its constant coefficient is four and its leading coefficient in degree
eighteen is three. Thus neither \(p\), represented by \(u=0\), nor \(q\),
represented by \(u=\infty\), is a zero of its degree-eighteen homogenization.
The nonzero determinant also independently gives generic transverse
multiplicity one along \(C\).

The standard-library
[boundary verifier](../computations/verify_ci_smooth_residual_boundary_2026_10_25.py)
constructs the actual homogeneous forms, derives their first symbols, compares
the determinant with this formula, and checks
\(\gcd(\Delta,\Delta')=1\) over \(\mathbf Q\). Its
[JSON evidence](../computations/ci_smooth_residual_boundary_2026_10_25.json)
records the nineteen coefficients. This is independent complementary evidence
for eighteen simple attachments and for endpoint avoidance; the projective
residual smoothness comes from the separate Jacobian and cohomology checks.

## 6. Rejected candidates and exact scope

The preliminary pair \(F+QH_0,G+QH_1\) also passed the smooth residual checks,
but retains simple attachments at both endpoints. It is useful as a comparison
and was independently checked before the final endpoint-free pair.

Adding \(x_0A\) and \(x_3D_3\), both with coefficient one, is an unsuccessful
intermediate candidate for an irreducible residual. It contains the line
\(x_0+x_1=x_2+x_3=0\). On that line \(Q=0\), \(F+x_0A=0\), and
\(G+x_3D_3=0\). The final coefficients two and three avoid this failure.
The rejected case should remain a documented diagnostic rather than an
unmentioned failed search.

The final example provides a single benchmark for the deformation notebook.
It neither classifies all pairs, proves properties for every point of a
parameter space, nor controls arbitrary bidegrees. It does concretely show
that all eighteen residual attachment points can move away from the two
distinguished endpoints while retaining \(C\).

Reproduce the durable checks from the repository root:

~~~sh
/opt/homebrew/bin/M2 --script research/computations/verify_ci_smooth_residual_example_2026_10_25.m2
python3 research/computations/verify_ci_smooth_residual_boundary_2026_10_25.py
~~~

These exact computations and the geometric bridges above pass independent
review. The user’s universal residual-component aim remains open; no canonical
record or inherited proof is changed by this audit.
