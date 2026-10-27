# Independent integration audit: arbitrary-degree residual absorption

Date: 2026-10-27. Reviewer: characteristic-literature review agent, with a focused independent [formal addendum audit](2026-10-27-absorption-formal-addendum-audit.md). **Status: PASS for the synthesis and the explicitly reviewed source additions, with the notation corrections below incorporated.** This is provisional review evidence, not canonical promotion or a claim of literature novelty.

Reviewed synthesis: [Arbitrary-degree residual absorption](2026-10-27-arbitrary-degree-absorption-synthesis.md).

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), the [contribution protocol](../CONTRIBUTING_AGENT.md), and the source notes and independent audits linked by the synthesis. No accepted proof or inherited computation was rerun. This review reconstructs the implications and tests scope boundaries rather than inferring correctness from agent agreement.

## 1. The positive operation and its quantifiers

For a smooth containing surface \(S\), global generation of \(I_C(3)\) gives the globally generated bundle \(3H-C\). Given \(1\le m<n\), the sufficient bound \(b\ge3n+1\) makes \(bH-rC\) very ample for \(r=m,n\). General residual sections \(\tau_r\) can be chosen smooth integral and with no \(C\)-component. The sections \(s_C^r\tau_r\) have different exact orders on \(C\), hence are linearly independent.

It follows directly that
\[
s_C^n\tau_n+t\,s_C^m\tau_m
\]
is nonzero at every finite parameter and has exact generic \(C\)-order \(m\) whenever \(t\ne0\), and \(n\) at zero. The hypersurface restriction sequence lifts both sections to actual degree-\(b\) homogeneous forms because \(H^1(\mathbf P^3,\mathcal O(b-a))=0\). Nonzero restriction to the integral \(S\) proves properness of every finite pair. No extra assumption \(b\ge a\) is necessary.

Removing the fixed lower factor \(s_C^m\) gives a relative Cartier divisor in a fixed line bundle. Its special scheme is the Cartier sum \((n-m)C+D_n\). This family is flat and has the genuine product-ideal gluing; it is not only a cycle equality. Its projective pencil contains the chosen smooth integral \(D_m\) at infinity, so smooth integral residuals occur for general finite nonzero parameters, rather than every such parameter.

The synthesis correctly claims a construction of **chosen families for arbitrary finite multiplicity increases**. It does not assert that an arbitrary supplied residual can be absorbed, that the starting curve \(D_m\) can be prescribed freely, or that all nonzero residual fibers are smooth. The sufficient degree bound depends on \(n\); no fixed-degree path to sole support or uniform degree bound follows. The extension with a generated ideal in degree \(\delta\) is the same proof with \(b\ge\delta n+1\).

## 2. Smooth-along-C capacity and the normal Cartier-index extension

For an integral hypersurface \(S\) smooth along every point of \(C\), \(C\) is a global Cartier divisor even if \(S\) is singular elsewhere. The residual after removing exact multiplicity is an effective Cartier divisor \(D=bH-mC\). The generated bundle \(3H-C\) is nef, so its degree on \(D\) is nonnegative. The normal sequence gives \(C^2=14-4a\), with no balanced-splitting assumption. Thus
\[
0\le b(3a-4)-m(4a-2)
\]
and the integer-\(a\ge2\) comparison gives \(\deg D\ge ab/3\). The sharpness factorization on the smooth quadric is explicitly retained in the source and audit. This uniform fraction applies in the stated carrier class, in every characteristic; it is not a bound for arbitrary on-curve singularities.

I also reconstructed the later normal \(\mathbf Q\)-Cartier corollary in the [deformation source](2026-10-27-absorption-deformation-interface.md). On an already specified normal integral characteristic-zero surface, choose \(h>0\) with \(hC\) Cartier. It is effective because its Weil coefficients are nonnegative and normality turns the corresponding rational local functions into regular ones. Serre generation supplies some \(\delta\) with \(\delta H-hC\) generated. For \(b\ge\delta v+1\), the systems \(bH-rhC\), \(r=u,v\), are very ample.

Normal surfaces have a finite singular locus. General members of these systems avoid it and are smooth integral by the usual smooth-locus Bertini argument. Interpolation consequently gives exact multiplicity \(hu\) for every nonzero parameter and \(hv\) at zero, with the same global lifting and fixed-lower residual construction. This is an index-compatible operation on a supplied carrier. It neither constructs a new carrier for \(C_0\), supplies a uniform effective \(\delta\), nor extends the one-third bound to singular-along-\(C\) carriers.

These statements concern different scopes: the explicit \(3n+1\) threshold and numerical residual floor belong to smooth-on-\(C\) geometry, while the normal Cartier-index extension depends on carrier-specific generation.

## 3. Full primary versus flat lower witness

In the constructed family the full primary component is \(mC\) for nonzero parameter and \(nC\) at zero. Its degree increases from \(4m\) to \(4n\), so it cannot itself be a flat projective family with fixed Hilbert polynomial. The fixed lower witness \(mC\) can remain flat and contained in all fibers; at zero it ceases to be the full component.

The synthesis therefore correctly separates:

* a flat family of total complete intersections;
* a flat residual closure after removal of a fixed lower witness;
* full primary extraction performed separately in each fiber.

No commuting-primary-extraction or flat-equation-module assertion is imported into the jump. The compatible-component flatness theorem in the [discrepancy literature review](2026-10-27-absorption-discrepancy-literature.md) requires precisely the extra family hypotheses which fail at such a jump.

## 4. Attachment identity and the meaning of the third term

The [attachment-module audit](2026-10-27-absorption-attachment-module-audit.md) reconstructs a fiberwise theorem for an actual proper CI and its **full** primary component \(T\):
\[
C\cap D=
\operatorname{div}(\operatorname{tors}\mathcal E_T)
+\operatorname{div}(\det\bar\rho).
\]

The source map is generically an isomorphism because the full component agrees with the supplied CI at its marked generic point. Its determinant is consequently nonzero as a section; this differs from the contact test for an arbitrary lower thickening. The module torsion detects non-lci points of \(T\) and is not identified with R-0030's filtered comparison defect.

The synthesis correctly combines the marked attachment formula with standard full-scheme linkage:
\[
\operatorname{length}(\operatorname{tors}\mathcal E_T)
+\deg\operatorname{div}(\det\bar\rho)
+\epsilon_{\mathrm{normal}}
=(a+b-4)\deg T-2p_a(T)+2.
\]
Here \(\epsilon_{\mathrm{normal}}=\operatorname{length}(I_C\mathcal O_{T\cap D})\). The quotient by this ideal is \(\mathcal O_{C\cap D}\), which may itself be tangentially nonreduced; the ideal is therefore not the full nilradical in general.

The local control illustrates the distinction exactly: the full finite ring is \(k[[t,y]]/(t^2,y^3)\), of length six; its quotient defining marked attachment is \(k[[t]]/(t^2)\), of length two; the marked normal ideal has length four. Its torsion-free determinant is a unit and the module torsion supplies the entire marked attachment. These numbers disprove a determinant-only detector, rather than establish positivity for every pair.

The combined formula remains an identity for actual fibers. It does not prescribe the residual scheme, identify attachment with summed branch contacts, or give a universal positive lower bound when the residual is allowed to vanish.

## 5. Actual equation motion: first order and Artin steps

The tangent incidence in the [formal lifting source](2026-10-27-absorption-formal-lifting-interface.md) has source
\[
H^0\mathcal Hom_X(J/I^N,I/J).
\]
The two fixed outer incidences force exactly this domain and target. Evaluation on the actual \(F,G\), followed by the connecting maps for \(0\to J(d)\to I(d)\to(I/J)(d)\to0\), gives the two global section-lifting obstructions in \(H^1(J(a))\oplus H^1(J(b))\). Their vanishing is necessary and sufficient for a first-order coefficient correction through the specified motion. It neither integrates the thickening tangent nor guarantees generation of its ideal.

I independently reconstructed the later §4 Artin step. For a small extension \(B'\to B\), with square-zero kernel \(A\) annihilated by the maximal ideal, assume a marked flat \(T_B\) has already been lifted to \(T_{B'}\). Its ideal is \(B'\)-flat: both ambient structure sheaf and quotient are flat, so the ideal sequence remains exact after base change. It gives
\[
0\to J(a)\otimes_k A\to J_{B'}(a)\to J_B(a)\to0.
\]
The resulting connecting class of a selected \(F_B\) lies in \(H^1(J(a))\otimes_k A\), vanishes exactly when that equation lifts, and leaves a torsor under \(H^0(J(a))\otimes_k A\). The equation \(G_B\) has an independent analogous class. These are conditional lifting statements after the lower ideal lift has been chosen, not a claim that the Quot deformation is unobstructed.

The source separately uses \(H^1(IJ(d))\) to lift a proposed class of \(J/IJ\) through a fixed lower embedding. That group must not be replaced by the moving-equation obstruction \(H^1(J(d))\). The synthesis keeps the distinction.

## 6. The fixed-quartic ribbon control and the Ext subscript correction

In characteristic zero, for \(T=2C\) in the containing smooth quadric, the sequence
\[
0\to K=\mathcal O_{\mathbf P^1}(-8)
\to E=\mathcal O_{\mathbf P^1}(-7)^2
\to L=\mathcal O_{\mathbf P^1}(-6)\to0
\]
identifies the marked ribbon motions with \(H^0\mathcal Hom_C(K,L)=H^0\mathcal O(2)\). Surjections \(E\to L\), modulo scalar, give an open subset of \(\mathbf P^3\), so these motions genuinely integrate as ribbons.

The relevant vanishing is \(\operatorname{Ext}^1_C(K,L)=H^1\mathcal O(2)=0\), **not** the ambient \(\operatorname{Ext}^1_X(i_*K,i_*L)\). The latter has normal-direction contributions; for this curve they give \(H^0(\mathcal O(2)\otimes N_{C/X})\), of dimension twenty. Quotients of the sheaf \(E\), which is annihilated by \(I_C\), can be treated directly on \(C\), so the corrected subscript preserves the ribbon argument. The source now explicitly incorporates this correction and restricts its opening general-characteristic claim to §§2–4; §5 is the fixed characteristic-zero control.

The unique containing quadric gives \(H^0(I(2))=H^0(J(2))=kq\). Its image in \(H^0(L(2))=H^0\mathcal O(2)\) is zero, and \(H^1(I(2))=0\), so the connecting map to \(H^1(J(2))\) is an isomorphism. Since \(q\) trivializes \(K(2)\), evaluation on \(q\) identifies the three-dimensional ribbon tangent space with this nonzero obstruction space. Thus every nonzero ribbon motion fails to move with an actual degree-two carrier through the fixed \(C\).

For the actual pair \((q,f^2)\), \(f=x_0^2x_2-x_1^3\), the second equation lies in \(I^2\) and is killed by every such tangent. The source's factorization on the quadric gives full primary component \(2C\) and residual \(4\ell\). This single control disproves a specific global-lifting inference; it is not a reopened low-degree STCI case.

## 7. Characteristic mechanisms and literature boundaries

The [conductor audit](2026-10-27-absorption-characteristic-conductor-audit.md) has been incorporated. The semi-invariant lemma now takes a normal finitely generated \(k\)-domain, so its finite invariant quotient is justified. The all-\(N\) Frobenius calculation, nonuniform exponent warning, classical characteristic-zero corrected square, and conditional defect cancellation are accurately summarized.

The synthesis preserves all construction provisos: an actual admissible carrier, full inverse support, global divisor/class relations and the correct ambient twist must still be supplied. It claims no new characteristic-zero quartic carrier, no effective uniform Cartier-index generation threshold, and no unrestricted STCI conclusion.

The [primary discrepancy assessment](2026-10-27-absorption-discrepancy-literature.md) distinguishes the nonreduced CM genus/linkage result from reduced Jacobian/Milnor claims, and the compatible flat-component theorem from arbitrary extraction across a jump. Those are standard literature inputs, not new proposed theorems.

## 8. Review outcome

The synthesis and the source additions explicitly reconstructed above pass with their stated scopes. The correction to the ambient-versus-curve Ext notation and the finite-invariant-quotient hypothesis is incorporated; no substantive construction has been lost. The work establishes chosen partial-absorption families and exact interfaces for attachment and equation lifting. It does not prove all residuals absorb, produce a fixed-degree supported endpoint, make primary extraction flat, or decide the characteristic-zero problem.

This audit covers the currently written normal \(\mathbf Q\)-Cartier extension described in §2. A further proposed non-\(\mathbf Q\)-Cartier Serre-generation remark would require its own explicit statement and review; it is not silently included here.
