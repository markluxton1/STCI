# The second coregularity defect on the actual intersection

Let \(S=k[x_0,x_1,x_2,x_3]\), let \(I\) be homogeneous, and put
\(M=H_I^2(S)\). Assume \(H_I^1(S)=H_I^3(S)=0\), and let
\(f,g\in I\) be a homogeneous regular sequence of degrees \(a,b\).
If \(fM=M\), then, with \(K_f=0:_M f\),
\[
 \mathcal D(f,g):=K_f/gK_f
       \simeq H_I^1(S/(f,g))(a).
\]
The grading shift is by the **first** degree \(a\); no extra shift by
\(b\) occurs. The statement is characteristic-free and concerns the
actual intersection, with any residual support it has.

Apply local cohomology first to
\(0\to S(-a)\xrightarrow f S\to S/f\to0\). The assumptions give
\(H_I^1(S/f)=K_f(-a)\) and \(H_I^2(S/f)=0\). Applying it to
\(0\to(S/f)(-b)\xrightarrow g S/f\to S/(f,g)\to0\) then gives
\(H_I^1(S/(f,g))=K_f(-a)/gK_f(-a-b)=\mathcal D(f,g)(-a)\).
This is the two-step long-exact-sequence mechanism behind
[Hartshorne--Polini, Theorem 3.1](https://arxiv.org/pdf/1907.05472),
specialized with its grading retained.

The first-coregularity hypothesis has a precise role. Without assuming
\(fM=M\), put \(C_f=M/fM\). The same first sequence gives
\(H_I^2(S/f)=C_f\), so the second gives the canonical exact sequence
\[
 0\longrightarrow(K_f/gK_f)(-a)
 \longrightarrow H_I^1(S/(f,g))
 \longrightarrow(0:_{C_f}g)(-b)\longrightarrow0.                \tag{1}
\]
The last annihilator vanishes exactly when \(C_f=0\): this quotient
of local cohomology is \(I\)-power torsion, so \(g\in I\) acts
locally nilpotently. Any nonzero element killed by a smallest positive
power of \(g\) supplies a nonzero element of \(0:_{C_f}g\).
Thus (1) separates the two failures without weakening first-element
coregularity. The two shifts have different origins. It retains the regular-pair
and \(H_I^1(S)=H_I^3(S)=0\) hypotheses; it adds no identification
with a conductor or normal-symbol module.

Writing \(E=S/(f,g)\) and \(U=\operatorname{Spec}E\setminus V(I)\),
the localization sequence
\[
0\to H_I^0(E)\to E\to\Gamma(U,\mathcal O_U)\to H_I^1(E)\to0
\]
interprets the defect as functions on the residual complement that fail
to extend over the actual intersection. It is not a normal-symbol
defect inferred from a dimension comparison.

## What a supported conductor can and cannot retain

Every finite module supported inside the affine cone \(V(I)\) is
annihilated by a power of \(I\); its higher local cohomology with
support in \(I\) vanishes. Thus applying \(H_I^1\) directly to
finite modules in a selected-conductor sequence **after sole support
has been imposed** cannot by itself produce a nonzero detector of
\(\mathcal D(f,g)\). This does not prohibit maps through ambient
modules or a comparison before the residual support is removed.

For the fixed quartic, the smooth quadric and cuspidal cubic are
individually coregular while their pair retains a double line. This
[existing counterexample](../equations/global_equations_and_constructions.md#homogeneous-local-cohomology-and-the-second-equation)
is a possible bounded source for computing the module above. No such
calculation, comparison to the full filtered equation module, or
nonvanishing theorem for all pairs is asserted here.

Independent correctness review checked the two exact sequences, the
general form (1), grading shifts and support restriction on November 20,
2026.


A concrete global check is the
[fixed toric (4,6) triple TS5--TS7](../torus/fixed_carrier_chow_arrangements.md#an-actual-non-lci-curvilinear-triple-the-conormal-torsion-is-visible).
Its actual proper pair has first
attachment annihilator lengths seven
and nine at the two endpoints.
At the cuspidal endpoint the full
primary has conormal torsion length
two and a determinant contribution
five. These numbers are computed
from the explicit homogeneous
equations and local Hilbert--Burch
matrix; they do not require assuming
a local-cohomology model to derive
the attachment lengths. This
calibrates the general comparison
proved and reviewed below.

In the generically curvilinear
multiplicity-three branch, the
[Bănică--Forster triple / source
comparison TR1--TR4](../residuals/layerwise_attachment_and_triples.md#triples-the-full-attachment-has-only-two-independent-divisors)
determines the first attachment
quotient length divisor as
\(\tau+\eta\), where \(\tau=D_2\)
is the intrinsic second saturated
normal defect and \(\eta\) is the
actual equation determinant divisor.
LC-A1 then identifies its canonical
dual with the first local annihilator
layer of \(\mathcal H_C^1(\mathcal O_Y)\).
This is an **actual-pair** comparison:
it does not identify the full graded
Hartshorne--Polini module at the
cone vertex or prove every such
pair has nonzero \(\tau+\eta\).
When a sole-supported pair exists
the two divisors both vanish.
The local normal form is classical;
the dual comparison and global
attachment apply to its full
primary.

## Actual attachment equation modules are the dual annihilator layers

**Application of ordinary local duality.** The actual linkage quotient,
Matlis-dual annihilator layers and adjunction twist were independently
reconstructed in the renewed November 23 F3/F7/F9 reassessment and checked
by the integrating lead. This review concerns the projective comparison
below, not recovery of the full graded module at the cone vertex. The [full-primary attachment](../residuals/residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor)
provides the previously missing bridge from the actual
equation module to the ordered-pair local cohomology. This
does not require a carrier normalization, a first-symbol
hypothesis, or curvilinearity.

Let \(L=(f,g)\) define an actual proper projective CI \(Y\)
containing the fixed smooth curve \(C\); denote its full
primary component by \(T\) and its linked genuine residual
by \(R\). In homogeneous coordinates set \(I=I_C,\ J=I_T\).
Use saturated sheaf ideals when passing to projective
stalks. For \(n\ge1\) define
\[
 Q_n=J/(L+I^nJ)
\]
as a sheaf (so \(Q_1\) is precisely the actual attachment
equation module of the cited argument).
These sheaves are supported on \(C\cap R\), not arbitrary
normal-symbol syzygy modules. Classical linkage identifies
\[
 J/L\simeq\omega_R\otimes\omega_Y^{-1}|_R .
\]
Taking the quotient by \(I^n\) of this module isomorphism gives \(Q_n\simeq(\omega_R/I^n\omega_R)\otimes\omega_Y^{-1}\).
The parent canonical module on \(R\) is essential;
it cannot be replaced by a finite conductor on \(C\).

The sequence \(0\to I_{R/Y}\to\mathcal O_Y\to\mathcal O_R\to0\)
has first term supported on \(C\); its higher local
cohomology with respect to \(C\) vanishes. Therefore
\[
 \mathcal H_C^1(\mathcal O_Y)\simeq
             \mathcal H_C^1(\mathcal O_R).
\]
At each attachment point \(P\), put \(B=\mathcal O_{R,P}\).
The ideal \(I_CB\) is maximal-ideal-primary since \(R\)
has no \(C\)-component, and \(B\) is one-dimensional
Cohen--Macaulay. Hence the last stalk is \(H^1_{\mathfrak m}(B)\).
Writing \(D_P(-)\) for local Matlis duality using the
injective hull of the residue field, Grothendieck local
duality gives
\(D_P(H^1_{\mathfrak m}(B))=\widehat{\omega_B}\).
Taking annihilators and using the exact finite-length
duality (the resulting modules are already complete)
now yields
\[
 \boxed{\, (Q_n\otimes\omega_Y)_P
 \ \simeq\ D_P\big(0:_{\mathcal H_C^1(\mathcal O_Y)_P}
                         I_C^n\big).\,}                 \tag{LC-A1}
\]
Equivalently, work directly over the completed \(B\);
\(\operatorname{Hom}_B(B/I^nB,H^1_{\mathfrak m}(B))\)
is dual to \(\widehat{\omega_B}\otimes B/I^nB\).
The finite canonical quotient is unchanged by completion.
This is an identification up to the chosen canonical
module normalization, with the displayed invertible
adjunction twist retained. The transition maps
\(Q_{n+1}\to Q_n\) are dual to inclusion of the
annihilator layers. Since local cohomology is
\(I\)-power torsion, all these layers exhaust the
projective stalk. In particular the *first* layer
already detects nonvanishing at the stalk, by the
torsion property, and its length is exactly
\(\operatorname{length}(C\cap R)_P\) by the existing
attachment theorem. The higher layers describe the
entire local module via a direct limit, not just its
support.

For the homogeneous module, localization in a standard
projective affine chart and taking degree zero identifies
the sheafification of \(H_I^1(S/(f,g))\) with
\(\mathcal H_C^1(\mathcal O_Y)\); this follows from
the Čech complex with homogeneous generators of \(I\).
Under the first-element coregularity and ambient
vanishing hypotheses earlier in this argument, this is
also the sheafification of
\(\mathcal D(f,g)(-\deg f)\).
Thus LC-A1 identifies the actual attachment equation
module with the dual of a finite annihilator layer
of the actual coregularity defect at each projective
attachment, with twists. Without first-element
coregularity it concerns the full \(H_I^1(S/(f,g))\),
not just its submodule \(\mathcal D(f,g)\).

The first-layer support criterion and connectedness
show that \(Q_1=0\) iff \(Y_{\rm red}=C\); hence for
actual proper pairs \(Q_1=0\) iff the full homogeneous
\(H_I^1(S/(f,g))=0\). The implication uses global
connectedness (or radical equality), not mere
sheafification, which in general could lose a module
at the cone vertex. No assertion that LC-A1 recovers
the entire graded homogeneous module including vertex
data is made. Under first-element coregularity the
same vanishing tests the second condition. Without
that hypothesis, it cannot be used to infer
\(\mathcal D(f,g)\ne0\) separately.

The already-established inputs are Hartshorne--Polini,
[*Quasi-cyclic modules and coregular sequences*](https://arxiv.org/abs/1907.05472),
Grothendieck local duality ([Stacks 0A81](https://stacks.math.columbia.edu/tag/0A81),
especially Lemma 47.18.4, and [0DW3](https://stacks.math.columbia.edu/tag/0DW3)),
and ordinary liaison's residual canonical module.
The new comparison is the application to the *actual*
full-primary equation module and all its \(I\)-normal
powers, not an extension of the coregularity theorem.
The open research question has changed: find a uniform
positive lower bound on the actual attachment equation
module (or rule out its vanishing) by global equation
lifts or geometric obstructions. It is no longer
necessary to seek a map from a purely local conductor
module to the first pairwise defect. A finite module
supported on \(C\) has zero higher \(I\)-local
cohomology; LC-A1 uses Matlis duality of the canonical
module on the residual, and only then restriction.
This is characteristic-free with the stated
coregularity hypotheses for that interpretation.
