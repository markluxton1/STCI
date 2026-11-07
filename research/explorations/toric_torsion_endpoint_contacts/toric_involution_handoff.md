# Toric carriers, transverse torsion, and involution

**Status:** Exploratory source document; not theorem authority.
**Date:** 2026-11-02
**Source:** ChatGPT mathematical exploration.
**Consolidated account:** [Toric torsion and endpoint contacts](../../synthesis/toric_torsion_and_endpoint_contacts.md)

This is a restored and corrected edition of an exploratory source, not a
verbatim transcript or a result. The [received version](https://github.com/markluxton1/STCI/blob/b647c18cffa39a0897acd1d989ee779dd0e0b650/research/explorations/toric_torsion_endpoint_contacts/toric_involution_handoff.md)
already contained stripped delimiters and missing mathematical symbols; the
saved earlier versions contain the same damage. Coordinates, maps and other
recoverable formulas below have been reconstructed from the fixed embedding,
the surrounding derivation and the linked current proof homes. No intact
original was available for comparison.

## Restoration and corrections — 2026-11-02

The missing four-coordinate parametrizations, torus actions, reversal map,
factorizations, radical equation and character restrictions have been
reconstructed. Section 11 now separates the binomial semigroup from the
characteristic-dependent power-descent criterion. Sections 16–20 and the
continuation prompt distinguish the existing reviewed invariant-
carrier theorem from open comparisons, and replace the incorrect support-
loss warning by the full-ideal versus two-extreme-forms distinction.
The characteristic-two fourth-order description is restricted to the ruled
section and generic transverse length, without identifying endpoint algebras.

The mathematical discussion and useful failed proposals are retained, with
corrections identified explicitly. Historical research suggestions do not
override [repository governance](../../../AGENTS.md). Consult the
[consolidated account](../../synthesis/toric_torsion_and_endpoint_contacts.md)
and its current proof links before relying on a claim.

---

STCI Toric Geometry — Mathematical Handoff

Purpose

This note preserves the mathematical content of a conversation about the fixed rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3
\]

and a toric/group-scheme interpretation of the positive-characteristic set-theoretic complete-intersection (STCI) constructions.

The goal is to make the discussion portable to a new conversation without requiring the original transcript.

The note distinguishes:

Established facts already present in the STCI project or standard toric geometry.

Direct deductions made from those facts during the discussion.

Research directions/speculation suggested by the resulting picture.

## 1. The fixed curve and its intrinsic torus

The fixed curve is

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

On the dense chart \(s\ne0\), set

\[
u=t/s.
\]

Then

\[
C_0^\circ=\{[1:u:u^3:u^4]\mid u\in\mathbf G_m\}.
\]

Thus \(C_0\) is a projective toric curve. Its intrinsic torus is \(\mathbf G_m\), acting by

\[
\lambda\cdot[x_0:x_1:x_2:x_3]
=[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3].
\]

The coordinate weights are therefore

\[
\boxed{(0,1,3,4)}.
\]

Equivalently, \(C_0\) is the projective monomial curve associated to

\[
A_C=\{0,1,3,4\}\subset\mathbf Z.
\]

Its ideal is binomial. One convenient generating set is

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,\\
A&=x_1^3-x_0^2x_2,\\
B&=x_1^2x_3-x_0x_2^2,\\
D&=x_2^3-x_1x_3^2.
\end{aligned}
\]

## 2. Torsors and simply transitive actions

If a group \(G\) acts freely and transitively on a set \(S\), then \(S\) is a \(G\)-torsor (or principal homogeneous space).

After choosing a basepoint \(x_0\in S\),

\[
G\longrightarrow S,\qquad g\mapsto g\cdot x_0
\]

is a bijection.

The choice of basepoint is what turns the torsor into an identified copy of \(G\); without it there is no preferred identity element in \(S\).

This language becomes useful for the finite families of curves appearing in the characteristic-\(p\) construction.

## 3. A transverse family of toric translates of \(C_0\)

For \(a\in\mathbf G_m\), define

\[
\boxed{
C_a=[s^4:s^3t:a\,st^3:t^4].
}
\]

Equivalently, on the dense torus,

\[
C_a^\circ=\{[1:u:a u^3:u^4]\mid u\in\mathbf G_m\}.
\]

Each \(C_a\) is a diagonal projective translate of \(C_0\):

\[
C_a=\operatorname{diag}(1,1,a,1)\cdot C_0.
\]

Therefore every \(C_a\) is itself a toric curve with the same intrinsic torus weights

\[
\boxed{(0,1,3,4)}.
\]

There are two commuting multiplicative actions:

Intrinsic torus

\[
\lambda\cdot[x_0:x_1:x_2:x_3]
=[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3].
\]

This acts within each \(C_a\).

Transverse torus

\[
a\cdot[x_0:x_1:x_2:x_3]=[x_0:x_1:a x_2:x_3].
\]

This acts among the curves:

\[
a\cdot C_b=C_{ab}.
\]

Thus the family \(\{C_a\}\) is a transverse \(\mathbf G_m\)-orbit.

For a finite subgroup scheme \(\mu_N\subset\mathbf G_m\), the curves

\[
\{C_\zeta:\zeta\in\mu_N\}
\]

form the corresponding torsion orbit. Over characteristic zero, where \(\mu_N\) is reduced, its geometric points form a simply transitive \(\mu_N\)-set after choosing \(C_1=C_0\).

## 4. The quartic toric carrier

The family \(C_a\) sweeps out the quartic surface

\[
\boxed{
S_+=V(F),\qquad
F=x_1^4-x_0^3x_3.
}
\]

Indeed, every point

\[
[1:u:a u^3:u^4]
\]

satisfies

\[
x_1^4=u^4=x_3=x_0^3x_3.
\]

The dense torus of \(S_+\) has parametrization

\[
\boxed{
(u,z)\longmapsto[1:u:z u^3:u^4],
\qquad (u,z)\in\mathbf G_m^2.
}
\]

Here:

\(u\) is the intrinsic coordinate along \(C_z\);

\(z\) is the transverse coordinate labeling the curve.

Thus

\[
T_{S_+}\simeq\mathbf G_{m,u}\times\mathbf G_{m,z}.
\]

The four projective coordinates have two-dimensional character weights

\[
\boxed{
m_0=(0,0),\quad
m_1=(1,0),\quad
m_2=(3,1),\quad
m_3=(4,0).
}
\]

The relation

\[
4m_1=3m_0+m_3
\]

gives the toric binomial

\[
x_1^4-x_0^3x_3=0.
\]

So the familiar quartic carrier in the positive-characteristic construction is naturally the projective toric compactification obtained by adjoining the transverse torus direction to the intrinsic torus of \(C_0\).

## 5. Automorphisms of \(C_0\)

Assume characteristic zero for the stabilizer and orbit assertions in this
section. No small-characteristic stabilizer classification is asserted here.

The embedding is defined by the four-dimensional subspace

\[
V_0=\langle s^4,s^3t,st^3,t^4\rangle
\subset H^0(\mathbf P^1,\mathcal O(4)).
\]

This is the hyperplane obtained by omitting \(s^2t^2\).

The automorphisms of \(\mathbf P^1\) preserving this linear system preserve the unordered pair

\[
\{0,\infty\}.
\]

They are

\[
u\mapsto au
\]

and

\[
u\mapsto a/u.
\]

Thus, in characteristic zero,

\[
\boxed{
\operatorname{Aut}_{\mathbf P^3}(C_0)
\simeq
\mathbf G_m\rtimes C_2.
}
\]

The identity component is the intrinsic torus \(T_C\).

The nontrivial involution can be represented by coordinate reversal

\[
\boxed{
\iota:[x_0:x_1:x_2:x_3]
\mapsto
[x_3:x_2:x_1:x_0].
}
\]

On the dense torus of \(C_0\), this induces

\[
u\mapsto u^{-1}.
\]

Consequently the \(PGL_4\)-orbit of \(C_0\) has the homogeneous-space description

\[
PGL_4\cdot C_0
\simeq
PGL_4/(\mathbf G_m\rtimes C_2),
\]

so its dimension is

\[
15-1=14.
\]

## 6. The opposite quartic carrier

Coordinate reversal does not preserve \(S_+\). Instead it exchanges \(S_+\) with

\[
\boxed{
S_-=V(G_4),\qquad
G_4=x_2^4-x_0x_3^3.
}
\]

Indeed,

\[
\iota^*F=x_2^4-x_3^3x_0.
\]

Thus

\[
\boxed{\iota(S_+)=S_-}.
\]

The corresponding opposite transverse family is

\[
\boxed{
C_a^-=[s^4:a\,s^3t:st^3:t^4].
}
\]

Its transverse torus scales \(x_1\), whereas the transverse torus of \(S_+\) scales \(x_2\).

Thus the inversion symmetry of \(C_0\) exchanges the two transverse directions:

\[
T_+\longleftrightarrow T_-.
\]

This gives a useful symmetric picture:

\[
S_+\xleftrightarrow{\ \iota\ }S_-,
\qquad
C_0\xrightarrow{\ \iota\ }C_0.
\]

## 7. The \((4,4)\) intersection as a torsion orbit

Consider

\[
F=x_1^4-x_0^3x_3,
\qquad
G_4=x_2^4-x_0x_3^3.
\]

On the chart \(x_0=1\), \(F=0\) gives

\[
x_3=x_1^4.
\]

Then \(G_4=0\) becomes

\[
x_2^4=x_1^{12},
\]

or

\[
x_2^4-x_1^{12}=\prod_{\zeta^4=1}(x_2-\zeta x_1^3).
\]

Hence in characteristic zero the reduced complete intersection is

\[
\boxed{V(F,G_4)_{\mathrm{red}}=\bigcup_{\zeta\in\mu_4}C_\zeta.}
\]

set-theoretically.

On the ruled model used in the STCI project, the same equation appears as

\[
q^4-h^4=0,
\]

with sections

\[
q=\zeta h.
\]

Thus the classical four-section picture is precisely the compactification of the \(\mu_4\)-torsion orbit in the transverse torus.

## 8. Characteristic two as group-scheme collapse

In characteristic two,

\[
z^4-1=(z-1)^4.
\]

The group scheme

\[
\mu_4=\operatorname{Spec}k[z,z^{-1}]/(z^4-1)
\]

is nonreduced. It has length four but only one geometric point.

Accordingly,

\[
q^4-h^4=(q-h)^4.
\]

On the ruled model the section equation becomes the fourth power shown
above. Downstairs the reduced support is \(C_0\), with generic transverse
length four; this does not identify the full endpoint local algebra with a
primitive fourth-order thickening. See the prescribed
[mu4 result](../../results/quartic_mu4_degeneration.md).

This explains the characteristic-two STCI

\[
\boxed{\sqrt{(F,G_4)}=I_{C_0}.}
\]

Conceptually:

The two inversion-conjugate toric quartic carriers intersect in a transverse \(\mu_4\)-torsion orbit in characteristic zero. In characteristic two, \(\mu_4\) becomes infinitesimal and that orbit collapses set-theoretically onto \(C_0\).

## 9. The general Frobenius mate as a character equation

The STCI project uses the general binomial construction

\[
F=x_1^4-x_0^3x_3
\]

and

\[
\boxed{
G_N=x_2^N-x_0^b x_1^a x_3^{2a+3b},
}
\]

where

\[
\boxed{N=3a+4b,\qquad a,b\ge0.}
\]

Restrict this equation to the dense torus of \(S_+\):

\[
x_0=1,\qquad
x_1=u,\qquad
x_2=z u^3,\qquad
x_3=u^4.
\]

Then

\[
x_2^N=z^Nu^{3N}.
\]

The second monomial becomes

\[
(x_0^b x_1^a x_3^{2a+3b})|_{T_{S_+}}
=u^{a+4(2a+3b)}=u^{9a+12b}.
\]

Since

\[
3N=3(3a+4b)=9a+12b,
\]

we obtain

\[
\boxed{G_N|_{T_{S_+}}=u^{3N}(z^N-1).}
\]

Since \(u\) is invertible on the dense torus,

\[
G_N=0
\quad\Longleftrightarrow\quad
\boxed{z^N=1}.
\]

This is a central conceptual observation.

Let

\[
\chi:T_{S_+}\to\mathbf G_m,
\qquad
\chi(u,z)=z
\]

be the transverse character. Then the mate cuts out

\[
\mathbf G_{m,u}\times\mu_N.
\]

In characteristic zero its connected components are

\[
\mathbf G_{m,u}\times\{\zeta\},
\qquad \zeta\in\mu_N,
\]

whose projective closures are precisely the curves \(C_\zeta\).

Therefore the positive-characteristic binomial construction is naturally:

\[
\boxed{
\text{toric carrier}
+
\text{transverse character equation }\chi^N=1.
}
\]

## 10. Character-lattice interpretation

The character lattice of the dense torus is

\[
M=\mathbf Z e_u\oplus\mathbf Z e_z.
\]

The coordinate weights are

\[
(0,0),(1,0),(3,1),(4,0).
\]

The first monomial of \(G_N\) has character weight

\[
N(3,1)=(3N,N).
\]

The second monomial has weight

\[
(9a+12b,0)=(3N,0).
\]

Their difference is

\[
\boxed{(0,N)=N e_z}.
\]

So the binomial is exactly the compactified equation corresponding to the transverse character \(z^N\).

This explains why the intrinsic \(u\)-dependence cancels: the two monomials have the same intrinsic torus weight and differ only in transverse character.

## 11. Why the numerical semigroup \(\langle3,4\rangle\) appears

On the dense torus, the equation

\[
z^N=1
\]

makes sense for every positive integer \(N\).

But not every such character equation descends to an honest homogeneous polynomial on the chosen nonnormal projective carrier \(S_+\).

For the displayed binomial construction, descent requires

\[
N=3a+4b
\]

with \(a,b\ge0\), i.e.

\[
\boxed{
N\in\langle3,4\rangle.
}
\]

Thus the numerical semigroup

\[
\langle3,4\rangle=\{0,3,4,6,7,8,\ldots\}
\]

can be interpreted as a descent semigroup for transverse characters.

The condition \(N\in\langle3,4\rangle\) characterizes the displayed
homogeneous binomial. It must be distinguished from descent of a power
whose entire support is the original quartic.

For that stronger comparison use the opposite carrier \(S_-\), as in the
[current fixed-carrier proof](../../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
Its normalization has coordinate subring

\[
R[z]=k[s^4,st^3,t^4,z],\qquad \phi=z-s^3t.
\]

A degree-\(N\) sole-support mate pulls back to a scalar multiple of \(\phi^N\).
The exact descent criterion on this fixed carrier is

\[
\phi^N\in R[z]
\quad\Longleftrightarrow\quad
p^{v_p(N)}\in\langle3,4\rangle
\qquad(\operatorname{char}k=p>0).
\]

In characteristic zero no positive power descends: its coefficient
\(-N s^3t\) at \(z^{N-1}\) is nonzero and is not in \(R\). Thus the numerical
semigroup alone is not a characteristic-free singleton-support criterion.
Coordinate reversal transports this fixed-carrier statement to \(S_+\).

## 12. General characteristic-\(p\) collapse

Keep the admissibility condition \(N\in\langle3,4\rangle\) from
Section 11, and take

\[
N=p^r.
\]

In characteristic zero,

\[
z^N-1=\prod_{\zeta\in\mu_N}(z-\zeta)
\]

has \(N\) distinct roots, so the reduced intersection contains \(N\) distinct toric curves

\[
C_\zeta.
\]

In characteristic \(p\),

\[
z^{p^r}-1=(z-1)^{p^r}.
\]

Thus

\[
\mu_{p^r}
\]

is an infinitesimal group scheme supported at the identity.

Consequently

\[
\mathbf G_m\times\mu_{p^r}
\]

is an infinitesimal thickening of

\[
\mathbf G_m\times\{1\}.
\]

After projective compactification, the reduced support is

\[
\boxed{C_0}.
\]

This yields the conceptual form of the positive-characteristic STCI mechanism:

\[
\boxed{
\begin{array}{c}
\text{nonnormal projective toric carrier }S_+\\
\cup\\
T_{S_+}=\mathbf G_m\times\mathbf G_m\\
\downarrow\quad \chi^N=1\\
\mathbf G_m\times\mu_N\\
\downarrow\quad\text{compactification}\\
\displaystyle\bigcup_{\zeta\in\mu_N}C_\zeta\\
\downarrow\quad N=p^r,\ \operatorname{char}k=p\\
C_0\text{ as reduced support}.
\end{array}
}
\]

A useful shorthand is:

\[
\boxed{
\text{toric carrier}
+
\text{torsion subgroup scheme}
+
\text{Frobenius collapse}.
}
\]

## 13. Boundary behavior

The torus calculation alone is not enough to prove the projective STCI statement, because projective closure could introduce unwanted boundary components.

For the explicit construction, the boundary is controlled.

If

\[
x_0=0,
\]

then

\[
F=x_1^4
\]

forces

\[
x_1=0.
\]

The mate then forces

\[
x_2=0.
\]

Thus the only boundary point is

\[
[0:0:0:1],
\]

which is already the endpoint of every \(C_\zeta\).

Therefore the torsion-orbit description is genuinely projective for the explicit binomial construction, not merely a dense-torus heuristic.

## 14. Relation with the \(PGL_4\)-orbit

Every \(C_a\) is a projective translate of \(C_0\), so

\[
a\mapsto C_a
\]

defines a one-dimensional subvariety of

\[
PGL_4\cdot C_0
\simeq
PGL_4/\operatorname{Stab}(C_0).
\]

The finite collection

\[
\{C_\zeta:\zeta\in\mu_N\}
\]

is the \(N\)-torsion subset of this transverse \(\mathbf G_m\)-orbit.

This is stronger than saying that the curves are abstractly isomorphic. They are specific points in the same projective-equivalence orbit, obtained by a one-parameter diagonal subgroup of \(PGL_4\).

There is also a larger diagonal maximal torus

\[
T_{\mathrm{diag}}\simeq(\mathbf G_m)^3\subset PGL_4.
\]

The intrinsic torus \(T_C\), the \(x_2\)-scaling transverse torus \(T_+\), and the \(x_1\)-scaling opposite transverse torus \(T_-\) are naturally visible inside it. Coordinate reversal normalizes the diagonal torus and exchanges the two transverse directions.

This suggests studying the ambient symmetry subgroup

\[
T_{\mathrm{diag}}\rtimes\langle\iota\rangle
\]

as an ambient symmetry group for the special quartic constructions.

## 15. What this may tell us about the characteristic-zero STCI problem

The characteristic-zero question is whether there exist homogeneous forms \(F,G\) with

\[
V(F,G)_{\mathrm{red}}=C_0.
\]

The toric interpretation suggests reframing the positive-characteristic result:

the carrier has a transverse multiplicative coordinate;

the mate becomes a power/character equation in that coordinate;

in characteristic zero, a nontrivial equation \(z^N=1\) produces multiple distinct translates;

in characteristic \(p\), Frobenius collapses those translates scheme-theoretically.

Thus any characteristic-zero construction using the same mechanism fails automatically: finite multiplicative torsion remains reduced.

This suggests a possible obstruction principle:

For sufficiently equivariant carriers containing \(C_0\), the mate problem may reduce after normalization to a character or power equation. In characteristic zero, such an equation necessarily creates additional translates/components unless its degree is trivial.

A uniform character-lattice explanation is a research direction. The invariant-carrier exclusion itself already has the reviewed proof cited in Section 16.

## 16. Equivariant carriers as a tractable subclass

Because \(C_0\) is invariant under its intrinsic torus \(T_C\), the vector spaces

\[
H^0(\mathcal I_{C_0}(d))
\]

carry \(T_C\)-representations.

A carrier \(F\) that is a torus weight vector defines a \(T_C\)-invariant hypersurface.

The quartic carrier

\[
x_1^4-x_0^3x_3
\]

is exactly such an equivariant carrier.

A potentially useful program is therefore:

Decompose
\[
H^0(\mathcal I_C(d))
\]
into intrinsic-torus weight spaces.

Classify integral or otherwise relevant carriers represented by weight vectors.

Analyze their normalizations as equivariant surfaces.

Determine whether a supported mate necessarily becomes a character/power equation in a transverse coordinate.

The obstruction originally proposed here is already covered by the
[weight-homogeneous-carrier theorem](../../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#the-bound-and-its-exact-large-prime-minimum):
in characteristic zero even one weight-homogeneous equation cannot have an
arbitrary sole-support mate. This is an independently reviewed
theorem. Classifying these carriers may retain
geometric value, but is not an outstanding step in proving that exclusion.
A hypothetical supported CI ideal therefore cannot itself be invariant;
its reduced curve remains invariant.

## 17. Possible torus degeneration of an arbitrary hypothetical pair

Suppose hypothetically that

\[
V(F,G)_{\mathrm{red}}=C_0
\]

in characteristic zero.

Since \(C_0\) is \(T_C\)-invariant, both \(F\) and \(G\) lie in the invariant ideal \(I(C_0)\), and each can be decomposed into torus weight components:

\[
F=\sum_\chi F_\chi,
\qquad
G=\sum_\psi G_\psi.
\]

This raises the possibility of using a one-parameter subgroup of \(T_C\) to degenerate the pair toward extreme weight components:

\[
(F,G)
\rightsquigarrow
(F_{\chi_0},G_{\psi_0}).
\]

If one could control the relevant support or multiplicity data under such a degeneration, the general problem might reduce to an equivariant problem.

The hoped-for schematic route would be

\[
\boxed{
\text{arbitrary hypothetical STCI pair}
\longrightarrow
\text{torus degeneration}
\longrightarrow
\text{equivariant carrier/mate}
\longrightarrow
\text{character-lattice obstruction}.
}
\]

The unresolved step is recovery of two-generation on the moving ideal,
not preservation of support by its full Hilbert limit.

For \(P=I_{C_0}\) and a supported ideal \(J\), choose \(N\) with

\[
P^N\subset J\subset P.
\]

The torus preserves \(P\), so every translate belongs to the fixed closed
Hilbert incidence \(C_0\subset Y\subset V(P^N)\). Both opposite full flat
limits retain reduced support \(C_0\) and the Hilbert polynomial. They may
acquire embedded structure and extra minimal generators. The ideal of the
two displayed extreme forms can have common surface factors and is not in
general the full limiting ideal. This is the distinction established in the
[current full-limit argument](../../synthesis/global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit).

The original schematic route to an equivariant carrier/mate therefore does
not follow from a full invariant ideal limit: that limit need not be a CI.
Normalization, conductor, cycles and Rees data can still be useful, provided
the relevant comparison is established. The
[attracting-strata framework](../../synthesis/torus_attracting_strata_and_generator_incidence.md)
tests two-generation on moving ideals; it does not require their fixed
limits to have two generators.

## 18. Historical obstruction proposal and its current disposition

The following was proposed in the exploration. Its exclusion conclusion is
already covered by the reviewed theorem cited in Section 16;
no additional normality or boundary hypothesis is needed for that theorem.

Candidate equivariant obstruction.
Let \(S\subset\mathbf P^3\) be an integral carrier containing \(C_0\) and invariant under the intrinsic torus \(T_C\). Under suitable normality/nonnormality and boundary hypotheses, no hypersurface \(H\) can satisfy
\[
V(S,H)_{\mathrm{red}}=C_0
\]
over an algebraically closed field of characteristic zero.

The original discussion supplied no proof; the current repository proof is the weight-homogeneous-carrier theorem, with its stated status.

The quartic toric carrier provides a model where it is true and where the obstruction can be understood completely through the transverse character and normalization semigroup.

A character-lattice explanation for other carriers is a possible geometric comparison, not a missing proof of the already covered invariant-carrier exclusion.

## 19. Established facts vs. deductions vs. speculation

Established / repository-backed

\(C_0=[s^4:s^3t:st^3:t^4]\).

Its intrinsic weights are \((0,1,3,4)\).

Its ideal is binomial.

The quartic carrier
\[
S_+=V(x_1^4-x_0^3x_3)
\]
occurs in the positive-characteristic construction.

The opposite quartic
\[
S_-=V(x_2^4-x_0x_3^3)
\]
occurs in the characteristic-two \((4,4)\) construction.

In characteristic zero the \((4,4)\) intersection decomposes into four sections/components indexed by fourth roots of unity.

In characteristic two the intersection has reduced support \(C_0\) and generic transverse length four, with endpoint structure retained separately.

The general binomial mate has the form
\[
x_2^N-x_0^b x_1^a x_3^{2a+3b},
\qquad N=3a+4b.
\]

The displayed binomial has degree \(N\in\langle3,4\rangle\); singleton-support power descent has the characteristic-dependent criterion of Section 11.

The overall characteristic-zero STCI problem remains open.

Direct deductions from those facts

\(S_+\) is the toric surface with dense torus parametrization
\[
(u,z)\mapsto[1:u:z u^3:u^4].
\]

Its character weights are
\[
(0,0),(1,0),(3,1),(4,0).
\]

The family \(C_a\) is the family of closures of \(z=a\).

The general mate restricts to
\[
u^{3N}(z^N-1).
\]

Hence the general construction is a compactified transverse torsion equation.

Coordinate reversal exchanges \(S_+\) and \(S_-\).

The characteristic-two pair can be understood as the intersection of inversion-conjugate toric carriers whose transverse \(\mu_4\)-orbit becomes infinitesimal.

Speculative comparisons and existing constraints

Every sufficiently equivariant carrier may admit a comparable character-lattice obstruction.

The existing theorem already excludes invariant supported CI ideals in characteristic zero; the reduced curve itself retains its intrinsic torus symmetry.

A full torus limit preserves support and Hilbert polynomial, but transferring an obstruction from its fixed ideal to a two-generated moving ideal remains unresolved.

Normalization, conductors, Rees valuations and intersection cycles may supply additional constraints beyond the support and Hilbert data already preserved.

The proposed character-lattice comparisons require proof. The existing invariant-carrier exclusion retains its independently reviewed status.

## 20. Historical calculation suggestions and current scope

The original exploration suggested the following calculations. They are
retained for their possible geometric value, not as a compulsory agenda or
a reason to reopen the invariant-carrier exclusion. Current selection and
moving-ideal incidence guidance is in [AGENTS.md](../../../AGENTS.md).

Compute the full \(T_C\)-weight decomposition
\[
H^0(\mathcal I_C(d))
\]
for small \(d\), especially \(d=2,3,4,5\).

Classify the torus-eigenvector carriers in those degrees up to
\[
\operatorname{Aut}_{\mathbf P^3}(C_0)
\simeq\mathbf G_m\rtimes C_2.
\]

For each integral equivariant carrier:

compute normalization;

identify the dense torus or complexity-one action;

identify the inverse image of \(C_0\);

characterize supported mates as functions/divisors upstairs;

determine the descent semigroup.

Determine whether the quartic \(\langle3,4\rangle\) phenomenon is one instance of a general weight-semigroup obstruction.

Compare this framework with the existing STCI project's:

quartic carrier exclusions;

normal-filtration calculations;

conductor arguments;

equivariant degree bounds;

mixed-characteristic obstructions.

Investigate whether the two opposite quartic carriers are extremal members of a larger orbit/configuration under the normalizer of the intrinsic torus.

Retain the full limiting ideal, its support, Hilbert polynomial and endpoint structure, and identify which additional data constrain two-generation on a moving attracting locus.

## 21. Compact conceptual summary

The central picture reached in the discussion is:

\[
\boxed{
C_0\subset S_+
}
\]

where \(C_0\) is a toric curve and \(S_+\) is a nonnormal toric quartic surface.

The dense torus of \(S_+\) is

\[
T_{S_+}=\mathbf G_{m,\mathrm{intrinsic}}
\times
\mathbf G_{m,\mathrm{transverse}}.
\]

The curves

\[
C_a
\]

are the compactifications of the slices

\[
z=a.
\]

A positive-characteristic mate is, on the dense torus, exactly

\[
z^{p^r}=1.
\]

Thus in characteristic zero it selects the distinct torsion translates

\[
\{C_\zeta:\zeta\in\mu_{p^r}\},
\]

whereas in characteristic \(p\),

\[
\mu_{p^r}
\]

is infinitesimal and supported at the identity, so all of those translates collapse set-theoretically to \(C_0\).

The semigroup condition governing the explicit homogeneous mate records whether that transverse character equation descends through the chosen nonnormal projective compactification.

For this explicit family the positive-characteristic STCI has a toric torsion/Frobenius interpretation. A uniform character description would explain more of the geometry behind the existing invariant-carrier exclusion; extending useful constraints to unrestricted moving ideals remains open.

## 22. Historical continuation prompt, with current qualifications

The source ended with a continuation prompt. Its mathematical context is retained below, updated to respect the current full-limit and invariant-carrier results:

We are studying the characteristic-zero STCI problem for
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
Treat the attached STCI toric-geometry handoff as context. In particular, we have reinterpreted the positive-characteristic quartic-carrier construction as a transverse character equation \(z^N=1\) on the dense \(\mathbf G_m^2\) of the toric carrier \(S_+=V(x_1^4-x_0^3x_3)\), with \(\mu_{p^r}\) collapsing under Frobenius. Coordinate reversal exchanges \(S_+\) with \(S_-=V(x_2^4-x_0x_3^3)\).

I want to investigate whether this gives a route toward the general characteristic-zero problem. Start by computing the intrinsic-\(\mathbf G_m\) weight decomposition of \(H^0(\mathcal I_{C_0}(d))\) in low degrees and classifying torus-equivariant integral carriers up to \(\operatorname{Aut}_{\mathbf P^3}(C_0)\). Then assess whether their normalizations lead to a general character/semigroup obstruction for supported mates. Keep existing reviewed results separate from conjectural deductions. Use the full supported Hilbert limit, which preserves reduced support and Hilbert polynomial; test two-generation on the moving ideals, and do not reopen the already covered invariant-carrier exclusion.
