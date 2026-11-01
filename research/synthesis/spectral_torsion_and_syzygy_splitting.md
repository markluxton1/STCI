# Spectral torsion and the degrees of syzygy generators

For a smooth quadratic spectral root, the difference between its two
ruling line bundles determines the minimal degrees of the second-obstruction
syzygies. Four-torsion changes those generator degrees from \((3,3)\) to
\((2,4)\), while the full dual obstruction space remains sixteen-dimensional.
This gives an intrinsic interpretation of a syzygy jump, separate from any
attempt to exclude actual complete intersections.

Work over an algebraically closed field \(k\) of characteristic zero.
The splitting and rank classification below are independently reviewed
source-level results, still provisional and not canonically promoted.
The accepted [global dual compression](../supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-global-second-dual-compression)
and [R-0007](../results/quadratic_root_obstruction_model.md) supply the
identification with the actual ambient obstruction. The geometric proof
itself uses the spectral curve and its ruling line bundles.

The [general pushforward theorem](spectral_pushforward_powers.md#1-the-pushforward-of-every-power)
owns the intrinsic full proof for every integer power on a genus-one double
cover, in every characteristic. Its coefficient determinants for n>=2,
[kernel constructions](spectral_pushforward_powers.md#3-recovering-a-positive-graded-object-from-the-kernel),
[full-root boundary classification](spectral_pushforward_boundary.md), and
[determinant schemes](spectral_determinant_schemes.md) are separately reviewed
provisional extensions. This chapter owns their n=4 application to the
actual characteristic-zero second-obstruction model. No all-n ambient
obstruction model is inferred.

## The spectral curve and the actual dual bundle

In the fixed embedded normal coordinates for
\(C_0=[s^4:s^3t:st^3:t^4]\), write the first quadratic relation as
\[
f=a(z)u^2+b(z)uv+c(z)v^2,
\]
where \(a,b,c\) are homogeneous quadratics on the base
\(\mathbf P^1\), with no common base zero. Let
\[
Z=(f=0)\subset\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction},
\qquad \pi:Z\longrightarrow\mathbf P^1_{\rm base}.
\]
For the classification assume that the full divisor \(Z\) is smooth.
It is a genus-one curve of bidegree \((2,2)\). Set
\[
A=\mathcal O_Z(1,0),\qquad B=\mathcal O_Z(0,1),\qquad
\eta=B\otimes A^{-1}\in\operatorname{Pic}^0(Z).
\]
Both \(A\) and \(B\) have degree two. Their difference \(\eta\) is
nontrivial: if \(A\simeq B\), their complete degree-two linear systems
would identify the two projections up to a projective automorphism,
forcing the image to be a graph rather than a \((2,2)\) curve. This is
also the ruling-difference class in the accepted
[spectral Picard criterion](../results/spectral_root_picard_criterion.md).

Define the actual coefficient-convolution map and its kernel on the base:
\[
T_f=
\begin{pmatrix}
a&b&c&0&0\\
0&a&b&c&0\\
0&0&a&b&c
\end{pmatrix}:
\mathcal O^{\oplus5}\longrightarrow\mathcal O(2)^{\oplus3},
\qquad W=\ker T_f.
\tag{1}
\]
The transpose on each base fiber is multiplication by the nonzero binary
quadratic \(f\), from direction degree two to direction degree four.
It is injective, so \(T_f\) is surjective. Consequently \(W\) has rank
two and determinant \(\mathcal O(-6)\). The accepted dual model identifies
\(H^0(\mathbf P^1,W(10))\) with the full dual second-obstruction target.
This target is defined on the basepoint-free root family; the actual
second class is defined on the first-compatibility locus, where the first
ambient obstruction vanishes. The target retains the actual ambient
construction, rather than merely its first normal symbols.

## Four-torsion determines the splitting

**Proposition.** At every smooth geometric root above,
\[
W\simeq
\begin{cases}
\mathcal O(-3)\oplus\mathcal O(-3),&\eta^{\otimes4}\not\simeq\mathcal O_Z,\\
\mathcal O(-2)\oplus\mathcal O(-4),&\eta^{\otimes4}\simeq\mathcal O_Z.
\end{cases}
\tag{2}
\]
Thus the jump occurs at exact torsion order two or four; order one is
absent because \(\eta\) is nontrivial.

**Proof by specialization of the general theorem.** The
[all-power pushforward proof](spectral_pushforward_powers.md#1-the-pushforward-of-every-power)
with n=4 gives

    E_4=pi_*B^4 = O(3)^2 or O(2)+O(4),

according as eta^4 is nontrivial or trivial. Its divisor-sequence presentation
is dual to (1), hence E_4=W^*. This proves (2) by duality. Rank-two duality
also gives E_4=W(6), since det W=O(-6). The geometric splitting is thus the
n=4 case of one general proof; the actual H0(W(10)) obstruction identification
remains the separate ambient input stated above.

## A coefficient rank detector and a constant-dimensional space

Write
\[
T[4]=\{f:Z_f\text{ smooth and }\eta_f^{\otimes4}\simeq\mathcal O_{Z_f}\}.
\]
The splitting can be detected without constructing an elliptic group law.
Taking global sections of (1) after twisting by two gives the square map
\[
B_f:H^0(\mathcal O(2))^{\oplus5}
\longrightarrow H^0(\mathcal O(4))^{\oplus3},\qquad q\longmapsto T_fq.
\tag{5}
\]
In monomial bases this is a \(15\times15\) matrix with entries linear in
the coefficients of \(f\). Its kernel is \(H^0(W(2))\), which (2)
makes zero off \(T[4]\) and one-dimensional on \(T[4]\). Therefore
\[
\operatorname{rank}B_f=
\begin{cases}15,&f\notin T[4],\\14,&f\in T[4].\end{cases}
\tag{6}
\]
In particular \(\det B_f=0\) detects \(T[4]\) set-theoretically on the
smooth locus. This fiberwise argument alone makes no claim about determinant multiplicities
or its zero locus at singular roots. The [scheme theorem](spectral_determinant_schemes.md)
identifies its closed subscheme on the smooth open, including nonreduced
parameter directions; the [boundary classification](spectral_pushforward_boundary.md)
keeps singular and nonreduced roots separate.

The syzygies have two degree-three minimal generators off \(T[4]\),
and generators of degrees two and four on \(T[4]\). Twisting to the
actual dual space gives
\[
h^0(W(10))=
\begin{cases}
h^0(\mathcal O(7)) + h^0(\mathcal O(7))=8+8=16,\\
h^0(\mathcal O(8)) + h^0(\mathcal O(6))=9+7=16.
\end{cases}
\tag{7}
\]
Local choices of these generators on their respective splitting strata
therefore supply sixteen tests for a second class where it is defined.
The dimension of the target does not jump; the degrees of its minimal
syzygy generators do.

There is still a reason to retain the accepted twenty-five global tests.
For every basepoint-free root, duality of (1), followed by a twist by
four, gives
\[
0\longrightarrow\mathcal O(2)^{\oplus3}
\longrightarrow\mathcal O(4)^{\oplus5}
\longrightarrow W(10)\longrightarrow0.
\]
Since \(H^1(\mathcal O(2))=0\), global sections surject from a
25-dimensional space onto the 16-dimensional target, with a
nine-dimensional kernel. The existing
[global pairing presentation](../supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-global-second-dual-compression)
uses this surjection across the whole basepoint-free family, including
singular and nonreduced roots. It avoids choosing local splitting bases
or an invertible coefficient minor. The smooth splitting theorem neither
replaces that global coverage nor proves that a local sixteen-test atlas
would be computationally cheaper.

## Intrinsic meaning and the boundary of the equation bridge

The splitting jump records the four-torsion of the degree-zero difference
between the two ruling polarizations. It can be read either from the
spectral line bundle or from the rank of the coefficient matrix (5).
This geometric information has value without deciding an obstruction
zero locus: torsion governs the presentation of a constant-dimensional
space, rather than certifying that its actual second class vanishes.

To use the actual second class as a necessary test for an actual proper
homogeneous complete intersection \(Y=(F,G)\subset\mathbf P^3\) with
\(Y_{\mathrm{red}}=C_0\), the
[R-0006 bridge](../results/actual_ci_smooth_root_bridge.md) requires all of
its hypotheses: a saturated first relation; both actual
equations of generic normal order two, with their quadratic symbols
jointly generating that line everywhere; a full generic initial ideal
that is a coprime binary complete intersection \((f_2,g_s)\); and a
smooth full root. The second test applies in this setting only for
\(s>4\). At \(s=4\) the next relation changes its target. Neither the
spectral splitting nor abstract graded compatibility supplies global
surfaces, properness or sole support.

**Review and scope.** The splitting, the \(15\times15\) rank detector and
the local sixteen-test counts were reconstructed in the source's
independent `report_math_review`, and remain reviewed provisional results.
This chapter retains the actual obstruction's characteristic-zero scope. The
linked intrinsic all-power theorem has its own characteristic-free proof;
it does not extend that ambient operator or the actual-CI bridge. No diagonal,
pure-direction or subsequent boundary exclusion is part of this result,
and no mathematical computation was run for this extraction.
