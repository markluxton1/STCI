# A supported pencil needs its own principalization and fiber geometry

Finite generation of an ambient Cox ring controls complete linear
systems and rational contractions. A chosen two-section pencil may
need additional exceptional divisors. Affineness of a complement
pencil likewise does not identify its surface fibers with affine
planes or ruled surfaces. The following exact control and theorem
comparisons are reviewed provisional mathematics.

## Same support and equal degrees allow unbounded later contact

For every integer \(N\ge2\), take in \(\mathbf P^3\)
\[
P_N=X^N,\qquad Q_N=XZ^{N-1}+Y^N.
\tag{1}
\]
Both forms have degree N and their sole reduced common support is
\(L=V(X,Y)\). Indeed the first equation forces X=0, and the
second then forces Y=0. There is no residual curve downstairs.
At the generic point of L in the chart Z=1, put u=X, v=Y and
w=u+v^N. The full transverse ideal is exactly
\[
(u^N,u+v^N)=(w,v^{N^2}).\tag{2}
\]
This follows by reduction modulo w; it is an equality of ideals,
not just of radicals. Its colength is \(N^2\).

For \((w,v^M)\), the v-chart of the first ordinary point blowup
has w=vw_1 and total transform \(v(w_1,v^{M-1})\). Repeating
reduces M by one at each remaining base point. The final exceptional
valuation is
\[
\nu(w)=M,\qquad\nu(v)=1.
\]
It is the Rees valuation of this ideal: its normalized blowup is the
weighted point blowup with these weights. Taking M=N² in (2) gives
\[
\nu(w)=N^2,\quad\nu(v)=1,\quad\nu(u)=N.
\tag{3}
\]
The last equality uses \(u=w-v^N\) and \(N^2>N\).
Every normal principalizing modification dominates the normalized
ideal blowup, so it must retain this exceptional divisorial valuation.
A fixed finite modification has only finitely many exceptional
prime divisors; the valuations (3) are distinct as N varies.
Consequently no fixed finite modification of the blowup of the
reduced line principalizes all these pencils.

This control rules out a bound based only on the reduced support or
on a fixed finite ambient chamber list. It does not rule out a bound
that depends on the actual equation degrees. It also supplies no
supported pair for C0. The explicit ideal and valuation calculation
work in every characteristic; the Mori and resolution comparisons
below are used in characteristic zero.

## What a finite chamber decomposition controls

[Hu–Keel, Propositions 1.11 and 2.9](https://arxiv.org/pdf/math/0004017)
control complete linear systems and rational contractions on a Mori
dream space. A rational contraction is a further condition on a
rational map, not an automatic property of every chosen pencil.
Resolving that pencil can extract divisors mapping dominantly to its
parameter line. Thus the
[exact Cox presentation](cox_fiber_and_power_defects.md) does not
make its finite chamber list a simultaneous principalization of
arbitrary two-section subsystems.

[Włodarczyk, Theorem 1.0.1](https://www.math.purdue.edu/~wlodarcz/singularities/Resolution.pdf)
principalizes each specified ideal on a smooth variety in
characteristic zero. It gives no uniform estimate charging all later
contact against the original projective equation degrees. Example
(1) distinguishes this per-ideal existence theorem from a fixed
modification depending only on support.

## Affine complement morphisms retain unproved fiber hypotheses

For \(U=\mathbf P^3\setminus C_0\), the
[complement-pencil equivalence](global_equations_and_constructions.md#2-the-exact-complement-equivalence-and-its-topological-scope)
already proves that STCI is equivalent to a nonconstant morphism
\(f:U\to\mathbf P^1\), and that every such morphism is affine.
Its fibers are complements of C0 in the pencil hypersurfaces.
Neither affine-plane fibers nor negative logarithmic Kodaira dimension
follows from this equivalence.

[Dubouloz–Kishimoto, Theorem 6](https://arxiv.org/pdf/1408.1328)
starts with a dominant affine morphism of normal varieties over a
field of infinite transcendence degree over Q whose general closed
fibers are smooth geometrically connected affine surfaces of negative
logarithmic Kodaira dimension. Its output shrinks the base and makes
a finite étale base change before factoring through an affine-line
fibration. It neither constructs f nor supplies the missing negative
Kodaira-dimension hypothesis for the pencil fibers.

[Gurjar–Masuda–Miyanishi, Theorem 2.8](https://sci-tech.ksc.kwansei.ac.jp/~kayo/cmn/papers/lnd_def_final_02.pdf)
starts with a smooth morphism from a smooth affine threefold to a
smooth affine curve and assumes that every closed fiber is an affine
plane. It then gives a generic affine plane and, after shrinking,
an affine-plane bundle. Generic smoothness alone establishes none
of the affine-plane hypothesis. One can restrict a complement pencil
to a base chart, but that does not establish its required fiber types.

Over the complex numbers,
[Đinh–Jelonek, Theorem 3.4](https://d-nb.info/1185855084/34)
removes stratified generalized critical values for its nonproper
isotopy statement. These include asymptotic critical values, not just
ordinary critical values. Ignoring the behavior at infinity would
therefore unjustifiably turn the pencil into a global topological
bundle. The needed boundary control is additional geometric data.

These theorems have genuine constructive or structural conclusions
under their hypotheses. Finite Cox generation, automatic affineness
and per-ideal principalization supply no pair on the fixed embedded
complement and no positive residual-degree lower bound by themselves.
