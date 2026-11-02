STCI Toric Geometry — Mathematical Handoff

Purpose

This note preserves the mathematical content of a conversation about the fixed rational quartic

[
C_0=[s^4^3t^3^4]\subset \mathbf P^3
]

and a toric/group-scheme interpretation of the positive-characteristic set-theoretic complete-intersection (STCI) constructions.

The goal is to make the discussion portable to a new conversation without requiring the original transcript.

The note distinguishes:

Established facts already present in the STCI project or standard toric geometry.

Direct deductions made from those facts during the discussion.

Research directions/speculation suggested by the resulting picture.

1. The fixed curve and its intrinsic torus

The fixed curve is

[
C_0=[s^4^3t^3^4]\subset\mathbf P^3.
]

On the dense chart (s\ne0), set

[
u=t/s.
]

Then

[
C_0^\circ={[1:u^3^4]\in\mathbf G_m}.
]

Thus (C_0) is a projective toric curve. Its intrinsic torus is (\mathbf G_m), acting by

[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3].
]

The coordinate weights are therefore

[
\boxed{(0,1,3,4)}.
]

Equivalently, (C_0) is the projective monomial curve associated to

[
A_C={0,1,3,4}\subset\mathbf Z.
]

Its ideal is binomial. One convenient generating set is

[
\begin{aligned}
q&=x_0x_3-x_1x_2,\
A&=x_1^3-x_0^2x_2,\
B&=x_1^2x_3-x_0x_2^2,\
D&=x_2^3-x_1x_3^2.
\end{aligned}
]

2. Torsors and simply transitive actions

If a group (G) acts freely and transitively on a set (S), then (S) is a (G)-torsor (or principal homogeneous space).

After choosing a basepoint (x_0\in S),

[
G\longrightarrow S,\qquad g\mapsto g\cdot x_0
]

is a bijection.

The choice of basepoint is what turns the torsor into an identified copy of (G); without it there is no preferred identity element in (S).

This language becomes useful for the finite families of curves appearing in the characteristic-(p) construction.

3. A transverse family of toric translates of (C_0)

For (a\in\mathbf G_m), define

[
\boxed{
C_a=[s^4^3t,st^3^4].
}
]

Equivalently, on the dense torus,

[
C_a^\circ={[1:u u^3^4]\in\mathbf G_m}.
]

Each (C_a) is a diagonal projective translate of (C_0):

[
C_a=\operatorname{diag}(1,1,a,1),C_0.
]

Therefore every (C_a) is itself a toric curve with the same intrinsic torus weights

[
\boxed{(0,1,3,4)}.
]

There are two commuting multiplicative actions:

Intrinsic torus

[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3].
]

This acts within each (C_a).

Transverse torus

[x_0:x_1 x_2].
]

This acts among the curves:

[
a\cdot C_b=C_{ab}.
]

Thus the family ({C_a}) is a transverse (\mathbf G_m)-orbit.

For a finite subgroup scheme (\mu_N\subset\mathbf G_m), the curves

[
{C_\zeta:\zeta\in\mu_N}
]

form the corresponding torsion orbit. Over characteristic zero, where (\mu_N) is reduced, its geometric points form a simply transitive (\mu_N)-set after choosing (C_1=C_0).

4. The quartic toric carrier

The family (C_a) sweeps out the quartic surface

[
\boxed{
S_+=V(F),\qquad
F=x_1^4-x_0^3x_3.
}
]

Indeed, every point

[
[1:u u^3^4]
]

satisfies

[
x_1^4=u^4=x_3=x_0^3x_3.
]

The dense torus of (S_+) has parametrization

[
\boxed{
(u,z)\longmapsto[1:u u^3^4],
\qquad (u,z)\in\mathbf G_m^2.
}
]

Here:

(u) is the intrinsic coordinate along (C_z);

(z) is the transverse coordinate labeling the curve.

Thus

[
T_{S_+}\simeq\mathbf G_{m,u}\times\mathbf G_{m,z}.
]

The four projective coordinates have two-dimensional character weights

[
\boxed{
m_0=(0,0),\quad
m_1=(1,0),\quad
m_2=(3,1),\quad
m_3=(4,0).
}
]

The relation

[
4m_1=3m_0+m_3
]

gives the toric binomial

[
x_1^4-x_0^3x_3=0.
]

So the familiar quartic carrier in the positive-characteristic construction is naturally the projective toric compactification obtained by adjoining the transverse torus direction to the intrinsic torus of (C_0).

5. Automorphisms of (C_0)

The embedding is defined by the four-dimensional subspace

[
V_0=\langle s^4,s^3t,st^3,t^4\rangle
\subset H^0(\mathbf P^1,\mathcal O(4)).
]

This is the hyperplane obtained by omitting (s^2t^2).

The automorphisms of (\mathbf P^1) preserving this linear system preserve the unordered pair

[
{0,\infty}.
]

They are

[
u\mapsto au
]

and

[
u\mapsto a/u.
]

Thus, in characteristic zero (and with the usual caveats in small characteristic),

[
\boxed{
\operatorname{Aut}_{\mathbf P^3}(C_0)
\simeq
\mathbf G_m\rtimes C_2.
}
]

The identity component is the intrinsic torus (T_C).

The nontrivial involution can be represented by coordinate reversal

[
\boxed{
\iota:[x_0:x_1:x_2]
\mapsto
[x_3:x_2:x_1].
}
]

On the dense torus of (C_0), this induces

[
u\mapsto u^{-1}.
]

Consequently the (PGL_4)-orbit of (C_0) has the homogeneous-space description

[
PGL_4\cdot C_0
\simeq
PGL_4/(\mathbf G_m\rtimes C_2),
]

so its dimension is

[
15-1=14.
]

6. The opposite quartic carrier

Coordinate reversal does not preserve (S_+). Instead it exchanges (S_+) with

[
\boxed{
S_-=V(G_4),\qquad
G_4=x_2^4-x_0x_3^3.
}
]

Indeed,

x_2^4-x_3^3x_0.
]

Thus

[
\boxed{\iota(S_+)=S_-}.
]

The corresponding opposite transverse family is

[
\boxed{
C_a^-=[s^4,s^3t^3^4].
}
]

Its transverse torus scales (x_1), whereas the transverse torus of (S_+) scales (x_2).

Thus the inversion symmetry of (C_0) exchanges the two transverse directions:

[
T_+\longleftrightarrow T_-.
]

This gives a useful symmetric picture:

[
S_+\xleftrightarrow{\ \iota\ }S_-,
\qquad
C_0\xrightarrow{\ \iota\ }C_0.
]

7. The ((4,4)) intersection as a torsion orbit

Consider

[
F=x_1^4-x_0^3x_3,
\qquad
G_4=x_2^4-x_0x_3^3.
]

On the chart (x_0=1), (F=0) gives

[
x_3=x_1^4.
]

Then (G_4=0) becomes

[
x_2^4=x_1^{12},
]

or

\prod_{\zeta^4=1}(x_2-\zeta x_1^3).
]

Hence in characteristic zero the reduced complete intersection is

\bigcup_{\zeta\in\mu_4}C_\zeta
}
]

set-theoretically.

On the ruled model used in the STCI project, the same equation appears as

[
q^4-h^4=0,
]

with sections

[
q=\zeta h.
]

Thus the classical four-section picture is precisely the compactification of the (\mu_4)-torsion orbit in the transverse torus.

8. Characteristic two as group-scheme collapse

In characteristic two,

[
z^4-1=(z-1)^4.
]

The group scheme

[
\mu_4=\operatorname{Spec}k[z,z^{-1}]/(z^4-1)
]

is nonreduced. It has length four but only one geometric point.

Accordingly,

[
q^4-h^4=(q-h)^4.
]

Thus the four characteristic-zero sections coalesce scheme-theoretically into a fourth-order thickening of the single section (C_0), while the reduced support is just (C_0).

This explains the characteristic-two STCI

I_{C_0}.
}
]

Conceptually:

The two inversion-conjugate toric quartic carriers intersect in a transverse (\mu_4)-torsion orbit in characteristic zero. In characteristic two, (\mu_4) becomes infinitesimal and that orbit collapses set-theoretically onto (C_0).

9. The general Frobenius mate as a character equation

The STCI project uses the general binomial construction

[
F=x_1^4-x_0^3x_3
]

and

[
\boxed{
G_N=x_2^N-x_0^b x_1^a x_3^{2a+3b},
}
]

where

[
\boxed{N=3a+4b,\qquad a,b\ge0.}
]

Restrict this equation to the dense torus of (S_+):

[
x_0=1,\qquad
x_1=u,\qquad
x_2=z u^3,\qquad
x_3=u^4.
]

Then

[
x_2^N=z^Nu^{3N}.
]

The second monomial becomes

u^{9a+12b}.
]

Since

[
3N=3(3a+4b)=9a+12b,
]

we obtain

u^{3N}(z^N-1).
}
]

Since (u) is invertible on the dense torus,

[
G_N=0
\quad\Longleftrightarrow\quad
\boxed{z^N=1}.
]

This is a central conceptual observation.

Let

[
\chi:T_{S_+}\to\mathbf G_m,
\qquad
\chi(u,z)=z
]

be the transverse character. Then the mate cuts out

\mathbf G_{m,u}\times\mu_N.
]

In characteristic zero its connected components are

[
\mathbf G_{m,u}\times{\zeta},
\qquad \zeta\in\mu_N,
]

whose projective closures are precisely the curves (C_\zeta).

Therefore the positive-characteristic binomial construction is naturally:

[
\boxed{
\text{toric carrier}
+
\text{transverse character equation }\chi^N=1.
}
]

10. Character-lattice interpretation

The character lattice of the dense torus is

[
M=\mathbf Z e_u\oplus\mathbf Z e_z.
]

The coordinate weights are

[
(0,0),(1,0),(3,1),(4,0).
]

The first monomial of (G_N) has character weight

[
N(3,1)=(3N,N).
]

The second monomial has weight

(9a+12b,0)

(3N,0).
]

Their difference is

[
\boxed{(0,N)=N e_z}.
]

So the binomial is exactly the compactified equation corresponding to the transverse character (z^N).

This explains why the intrinsic (u)-dependence cancels: the two monomials have the same intrinsic torus weight and differ only in transverse character.

11. Why the numerical semigroup (\langle3,4\rangle) appears

On the dense torus, the equation

[
z^N=1
]

makes sense for every positive integer (N).

But not every such character equation descends to an honest homogeneous polynomial on the chosen nonnormal projective carrier (S_+).

For the displayed binomial construction, descent requires

[
N=3a+4b
]

with (a,b\ge0), i.e.

[
\boxed{
N\in\langle3,4\rangle.
}
]

Thus the numerical semigroup

{0,3,4,6,7,8,\ldots}
]

can be interpreted as a descent semigroup for transverse characters.

This is compatible with the stronger normalization argument in the STCI project. On the appropriate normalization of the quartic carrier, the inverse image of (C_0) is defined by a function of the form

[
\phi=z-s^3t.
]

A mate of degree (N) must pull back, up to scalar, to

[
\phi^N.
]

The question becomes whether this power belongs to the nonnormal coordinate subring. The same semigroup (\langle3,4\rangle) governs that descent.

So the semigroup is not merely an artifact of solving an exponent equation: it measures which powers of the transverse character/function descend through the nonnormal toric compactification.

12. General characteristic-(p) collapse

Take

[
N=p^r.
]

In characteristic zero,

\prod_{\zeta\in\mu_N}(z-\zeta)
]

has (N) distinct roots, so the reduced intersection contains (N) distinct toric curves

[
C_\zeta.
]

In characteristic (p),

[
z^{p^r}-1=(z-1)^{p^r}.
]

Thus

[
\mu_{p^r}
]

is an infinitesimal group scheme supported at the identity.

Consequently

[
\mathbf G_m\times\mu_{p^r}
]

is an infinitesimal thickening of

[
\mathbf G_m\times{1}.
]

After projective compactification, the reduced support is

[
\boxed{C_0}.
]

This yields the conceptual form of the positive-characteristic STCI mechanism:

[
\boxed{
\begin{array}{c}
\text{nonnormal projective toric carrier }S_+\
\cup\
T_{S_+}=\mathbf G_m\times\mathbf G_m\
\downarrow\quad \chi^N=1\
\mathbf G_m\times\mu_N\
\downarrow\quad\text{compactification}\
\displaystyle\bigcup_{\zeta\in\mu_N}C_\zeta\
\downarrow\quad N=p^r,\ \operatorname{char}k=p\
C_0\text{ as reduced support}.
\end{array}
}
]

A useful shorthand is:

[
\boxed{
\text{toric carrier}
+
\text{torsion subgroup scheme}
+
\text{Frobenius collapse}.
}
]

13. Boundary behavior

The torus calculation alone is not enough to prove the projective STCI statement, because projective closure could introduce unwanted boundary components.

For the explicit construction, the boundary is controlled.

If

[
x_0=0,
]

then

[
F=x_1^4
]

forces

[
x_1=0.
]

The mate then forces

[
x_2=0.
]

Thus the only boundary point is

[
[0:0:0:1],
]

which is already the endpoint of every (C_\zeta).

Therefore the torsion-orbit description is genuinely projective for the explicit binomial construction, not merely a dense-torus heuristic.

14. Relation with the (PGL_4)-orbit

Every (C_a) is a projective translate of (C_0), so

[
a\mapsto C_a
]

defines a one-dimensional subvariety of

[
PGL_4\cdot C_0
\simeq
PGL_4/\operatorname{Stab}(C_0).
]

The finite collection

[
{C_\zeta:\zeta\in\mu_N}
]

is the (N)-torsion subset of this transverse (\mathbf G_m)-orbit.

This is stronger than saying that the curves are abstractly isomorphic. They are specific points in the same projective-equivalence orbit, obtained by a one-parameter diagonal subgroup of (PGL_4).

There is also a larger diagonal maximal torus

[
T_{\mathrm{diag}}\simeq(\mathbf G_m)^3\subset PGL_4.
]

The intrinsic torus (T_C), the (x_2)-scaling transverse torus (T_+), and the (x_1)-scaling opposite transverse torus (T_-) are naturally visible inside it. Coordinate reversal normalizes the diagonal torus and exchanges the two transverse directions.

This suggests studying the normalizer

[
T_{\mathrm{diag}}\rtimes\langle\iota\rangle
]

as an ambient symmetry group for the special quartic constructions.

15. What this may tell us about the characteristic-zero STCI problem

The characteristic-zero question is whether there exist homogeneous forms (F,G) with

[
V(F,G)_{\mathrm{red}}=C_0.
]

The toric interpretation suggests reframing the positive-characteristic result:

the carrier has a transverse multiplicative coordinate;

the mate becomes a power/character equation in that coordinate;

in characteristic zero, a nontrivial equation (z^N=1) produces multiple distinct translates;

in characteristic (p), Frobenius collapses those translates scheme-theoretically.

Thus any characteristic-zero construction using the same mechanism fails automatically: finite multiplicative torsion remains reduced.

This suggests a possible obstruction principle:

For sufficiently equivariant carriers containing (C_0), the mate problem may reduce after normalization to a character or power equation. In characteristic zero, such an equation necessarily creates additional translates/components unless its degree is trivial.

This is a research direction, not an established theorem.

16. Equivariant carriers as a tractable subclass

Because (C_0) is invariant under its intrinsic torus (T_C), the vector spaces

[
H^0(\mathcal I_{C_0}(d))
]

carry (T_C)-representations.

A carrier (F) that is a torus weight vector defines a (T_C)-invariant hypersurface.

The quartic carrier

[
x_1^4-x_0^3x_3
]

is exactly such an equivariant carrier.

A potentially useful program is therefore:

Decompose
[
H^0(\mathcal I_C(d))
]
into intrinsic-torus weight spaces.

Classify integral or otherwise relevant carriers represented by weight vectors.

Analyze their normalizations as equivariant surfaces.

Determine whether a supported mate necessarily becomes a character/power equation in a transverse coordinate.

Prove a characteristic-zero obstruction for this equivariant subclass.

If successful, this would show that any characteristic-zero STCI must necessarily break the intrinsic torus symmetry.

That would be meaningful progress even without solving the fully general problem.

17. Possible torus degeneration of an arbitrary hypothetical pair

Suppose hypothetically that

[
V(F,G)_{\mathrm{red}}=C_0
]

in characteristic zero.

Since (C_0) is (T_C)-invariant, both (F) and (G) lie in the invariant ideal (I(C_0)), and each can be decomposed into torus weight components:

[
F=\sum_\chi F_\chi,
\qquad
G=\sum_\psi G_\psi.
]

This raises the possibility of using a one-parameter subgroup of (T_C) to degenerate the pair toward extreme weight components:

[
(F,G)
\rightsquigarrow
(F_{\chi_0},G_{\psi_0}).
]

If one could control the relevant support or multiplicity data under such a degeneration, the general problem might reduce to an equivariant problem.

The hoped-for schematic route would be

[
\boxed{
\text{arbitrary hypothetical STCI pair}
\longrightarrow
\text{torus degeneration}
\longrightarrow
\text{equivariant carrier/mate}
\longrightarrow
\text{character-lattice obstruction}.
}
]

However, this contains a serious unresolved step:

[
\boxed{
\text{reduced set-theoretic support need not behave well under degeneration.}
}
]

Initial ideals, flat degenerations, embedded multiplicities, and extra components can change in ways that destroy the STCI property.

The STCI project already contains filtration/initial-ideal calculations warning against assuming otherwise.

Therefore the precise research question is not merely whether a torus degeneration exists—it does—but:

Which invariant of a hypothetical STCI pair survives an intrinsic-torus degeneration strongly enough to force an equivariant contradiction?

Candidates might include normalization data, conductor data, intersection multiplicity, Rees valuations, cycles, or suitable equivariant initial structures rather than reduced support itself.

18. A possible broader obstruction theorem

One concrete theorem to investigate is:

Candidate equivariant obstruction.
Let (S\subset\mathbf P^3) be an integral carrier containing (C_0) and invariant under the intrinsic torus (T_C). Under suitable normality/nonnormality and boundary hypotheses, no hypersurface (H) can satisfy
[
V(S,H)_{\mathrm{red}}=C_0
]
over an algebraically closed field of characteristic zero.

This statement is not proved by the discussion.

The quartic toric carrier provides a model where it is true and where the obstruction can be understood completely through the transverse character and normalization semigroup.

The next task would be to determine how much of that mechanism survives for arbitrary (T_C)-equivariant carriers.

19. Established facts vs. deductions vs. speculation

Established / repository-backed

(C_0=[s^4^3t^3^4]).

Its intrinsic weights are ((0,1,3,4)).

Its ideal is binomial.

The quartic carrier
[
S_+=V(x_1^4-x_0^3x_3)
]
occurs in the positive-characteristic construction.

The opposite quartic
[
S_-=V(x_2^4-x_0x_3^3)
]
occurs in the characteristic-two ((4,4)) construction.

In characteristic zero the ((4,4)) intersection decomposes into four sections/components indexed by fourth roots of unity.

In characteristic two these collapse scheme-theoretically to a fourth-order thickening with reduced support (C_0).

The general binomial mate has the form
[
x_2^N-x_0^b x_1^a x_3^{2a+3b},
\qquad N=3a+4b.
]

The semigroup (\langle3,4\rangle) governs descent on the fixed quartic carrier.

The overall characteristic-zero STCI problem remains open.

Direct deductions from those facts

(S_+) is the toric surface with dense torus parametrization
[
(u,z)\mapsto[1:u u^3^4].
]

Its character weights are
[
(0,0),(1,0),(3,1),(4,0).
]

The family (C_a) is the family of closures of (z=a).

The general mate restricts to
[
u^{3N}(z^N-1).
]

Hence the general construction is a compactified transverse torsion equation.

Coordinate reversal exchanges (S_+) and (S_-).

The characteristic-two pair can be understood as the intersection of inversion-conjugate toric carriers whose transverse (\mu_4)-orbit becomes infinitesimal.

Speculative / research directions

Every sufficiently equivariant carrier may admit a comparable character-lattice obstruction.

Any characteristic-zero STCI may therefore have to break the intrinsic torus symmetry.

A torus degeneration of an arbitrary hypothetical pair might reduce the general problem to the equivariant case if an appropriate invariant survives degeneration.

The correct surviving invariant may involve normalization, conductors, Rees valuations, or intersection cycles rather than reduced support.

These should not be treated as established theorems without further proof.

20. Immediate calculations worth doing next

A productive continuation would be:

Compute the full (T_C)-weight decomposition
[
H^0(\mathcal I_C(d))
]
for small (d), especially (d=2,3,4,5).

Classify the torus-eigenvector carriers in those degrees up to
[
\operatorname{Aut}_{\mathbf P^3}(C_0)
\simeq\mathbf G_m\rtimes C_2.
]

For each integral equivariant carrier:

compute normalization;

identify the dense torus or complexity-one action;

identify the inverse image of (C_0);

characterize supported mates as functions/divisors upstairs;

determine the descent semigroup.

Determine whether the quartic (\langle3,4\rangle) phenomenon is one instance of a general weight-semigroup obstruction.

Compare this framework with the existing STCI project's:

quartic carrier exclusions;

normal-filtration calculations;

conductor arguments;

equivariant degree bounds;

mixed-characteristic obstructions.

Investigate whether the two opposite quartic carriers are extremal members of a larger orbit/configuration under the normalizer of the intrinsic torus.

Formulate precisely what data from an STCI pair can survive a one-parameter torus degeneration.

21. Compact conceptual summary

The central picture reached in the discussion is:

[
\boxed{
C_0\subset S_+
}
]

where (C_0) is a toric curve and (S_+) is a nonnormal toric quartic surface.

The dense torus of (S_+) is

\mathbf G_{m,\mathrm{intrinsic}}
\times
\mathbf G_{m,\mathrm{transverse}}.
]

The curves

[
C_a
]

are the compactifications of the slices

[
z=a.
]

A positive-characteristic mate is, on the dense torus, exactly

[
z^{p^r}=1.
]

Thus in characteristic zero it selects the distinct torsion translates

[
{C_\zeta:\zeta\in\mu_{p^r}},
]

whereas in characteristic (p),

[
\mu_{p^r}
]

is infinitesimal and supported at the identity, so all of those translates collapse set-theoretically to (C_0).

The semigroup condition governing the explicit homogeneous mate records whether that transverse character equation descends through the chosen nonnormal projective compactification.

This suggests that the positive-characteristic STCI is fundamentally a toric torsion/Frobenius phenomenon, and that the characteristic-zero problem may be attacked by understanding whether every sufficiently symmetric carrier forces an analogous transverse-character description.

22. Prompt for continuation in a new conversation

Paste or upload this note and use the following prompt:

We are studying the characteristic-zero STCI problem for
[
C_0=[s^4^3t^3^4]\subset\mathbf P^3.
]
Treat the attached STCI toric-geometry handoff as context. In particular, we have reinterpreted the positive-characteristic quartic-carrier construction as a transverse character equation (z^N=1) on the dense (\mathbf G_m^2) of the toric carrier (S_+=V(x_1^4-x_0^3x_3)), with (\mu_{p^r}) collapsing under Frobenius. Coordinate reversal exchanges (S_+) with (S_-=V(x_2^4-x_0x_3^3)).

I want to investigate whether this gives a route toward the general characteristic-zero problem. Start by computing the intrinsic-(\mathbf G_m) weight decomposition of (H^0(\mathcal I_{C_0}(d))) in low degrees and classifying torus-equivariant integral carriers up to (\operatorname{Aut}_{\mathbf P^3}(C_0)). Then assess whether their normalizations lead to a general character/semigroup obstruction for supported mates. Keep established results separate from conjectural deductions, and do not assume reduced support survives torus degeneration.
