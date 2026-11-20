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

Independent correctness review checked the two exact sequences, grading
shift and support restriction on November 20, 2026.
