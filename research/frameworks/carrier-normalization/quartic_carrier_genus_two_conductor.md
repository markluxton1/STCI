# Genus-two bisections and conductor geometry

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

## 9. Genus-two bisection: global ribbon contradiction and distinct conductor algebra

In characteristic zero, the bisection second-pencil reduction gives the actual Cartier equivalence (2csim2H) on the normalization. The resulting pure Cartier double is a ribbon with nilideal (mathcal O_{mathbf P^1}(-8)). Its generically nonzero ambient conormal map would be
[
mathcal O_{mathbf P^1}(-7)^{oplus2}longrightarrowmathcal O_{mathbf P^1}(-8),
]
which is impossible. The [complete bisection proof](../../arguments/carriers/genus_two_bisection_proof.md) establishes the second pencil, purity, Hilbert-polynomial calculation, and nonzero map; the [quartic-carrier assembly](../../arguments/carriers/quartic_carrier_proof.md#61-bisection-the-global-nilideal-obstruction) uses this to exclude the entire bisection lane, without a mate-degree bound.

A **different, conditional** quadratic-descent calculation survives as a reusable conductor-power lemma: with (w^2=delta) and (Q|_D=m+w), descent of a positive power (after excluding (m=0)) forces (delta=r^2), (m=alpha r), and (((alpha+1)/(alpha-1))^n=1), with (alpha
otin{0,pm1}). These are necessary conditions under the hypothetical bisection setup, not surviving STCI cases. See the [complete split-conductor argument](../../arguments/carriers/genus_two_bisection_descent.md).

## 13. Entire genus-two conductor and ambient conic model

The [entire-conductor proof](../../arguments/carriers/genus_two_entire_conductor_proof.md) establishes rational singularities without assuming a Cartier or (mathbf Q)-Cartier canonical class, identifies the **actual** conductor via finite duality, and proves that its downstairs scheme is a reduced line (Gamma). The whole upstairs conductor is a rank-two finite-flat algebra
[
p_*mathcal O_D=mathcal O_Gammaoplusmathcal O_Gamma(-2),
]
including singular or nonreduced fibers; its quadratic multiplication is a quartic section. These scheme-level conclusions cannot be replaced by reduced Jacobian support.

The [ambient conic-model proof](../../arguments/carriers/genus_two_ambient_conic_model_proof.md) identifies the two line equations with the complete basepoint-free adjoint pencil, proves the exact pulled-back line ideal, and constructs the integral strict transform (Tsim4H_B-2E_B) in the blowup along (Gamma). Proper trace and crepancy make (T) normal Gorenstein ADE. **This does not assert** that the original normalization (S) is Gorenstein or that its pencil descends through horizontal contractions. The [assembly](../../arguments/carriers/quartic_carrier_proof.md#6-sectional-genus-two-conic-geometry-and-the-two-correction-strata) uses these as proved inputs.

## 14. Exact conductor coordinates and fixed-curve fiber condition

For the genus-one projection of Section 2, the fixed rational normal quartic in retained coordinates \((x_0,x_1,x_2,x_3)\) and omitted coordinate \(z\) is \([U^4:U^3V:UV^3:V^4:U^2V^2]\). Write the six defining quadrics as
\[
\begin{aligned}
E_0&=x_0z-x_1^2,&E_1&=x_0x_2-x_1z,&E_2&=x_0x_3-x_1x_2,\\
E_3&=x_1x_2-z^2,&E_4&=x_1x_3-zx_2,&E_5&=zx_3-x_2^2.
\end{aligned}
\]
For a normalized pair \(Q_1=-E_3-aE_0-bE_1-cE_2-dE_4-eE_5\), \(Q_2=fE_0+gE_1+hE_2+iE_4+jE_5\), the entire conductor algebra from Section 2 has coefficients
\[
\begin{aligned}
A&=ax_0-bx_1-dx_2+ex_3,\\
R_1&=x_1x_2-ax_1^2+bx_0x_2+c(x_0x_3-x_1x_2)+dx_1x_3-ex_2^2,\\
L&=fx_0-gx_1-ix_2+jx_3,\\
R&=-fx_1^2+gx_0x_2+h(x_0x_3-x_1x_2)+ix_1x_3-jx_2^2.
\end{aligned}
\]
With \(z_c=U^2V^2\), restriction to the curve yields \(R_C=-z_cL_C\) and \((R_1)_C=z_c^2-A_Cz_c\). Over a zero of \(L_C\), the two possible omitted coordinates are \(z_c\) and \(A_C-z_c\). The singleton full-inverse-support condition therefore forces
\[
\operatorname{Supp}\operatorname{div}(L_C)\subseteq\operatorname{Supp}\operatorname{div}(A_C-2z_c).
\]
Since \(L_C\) has zero middle coefficient while \(A_C-2z_c\) has middle coefficient \(-2\), a squarefree \(L_C\) is impossible. This is a necessary support condition, not an assertion that all repeated-root strata are excluded by the same argument. The exact symbolic companion is [verify_session_genus_one_entire_conductor_2026_10_09.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_genus_one_entire_conductor_2026_10_09.py).


## 15. Genus-two conductor-line positions on the fixed quartic

Under the accepted genus-two blowup and mate-stratum hypotheses, if \(\Gamma=V(t_0,t_1)\) is the conductor line and \(f\) is the basepoint-free adjoint pencil, then \(t_i=g s_i\) with \(\operatorname{div}(g)=D_M\sim-K_M\). Consequently the scheme-theoretic intersection length is
\[
\tau=\operatorname{length}(C\cap\Gamma)=D_M\cdot c^\#=4-f\cdot c^\#.
\]
The two strata give \(\tau=2\) for \(\lambda=0\) and \(\tau=3\) for \(\lambda=1\), including nonreduced contact.

The unique quadric \(q=x_0x_3-x_1x_2\) restricts to degree two on any line. Thus a line meeting \(C\) in length at least three lies on \(q\), and the complete trisecant family is
\[
\Gamma_\kappa: x_2-\kappa x_0=x_3-\kappa x_1=0\quad(\kappa\in k),\qquad
\Gamma_\infty: x_0=x_1=0.
\]
Their common restriction divisor has degree three: three distinct points for \(\kappa\ne0,\infty\), and a triple endpoint for \(\kappa=0,\infty\). No trisecant has contact partition \([2,1]\); no line meets \(C\) in length four.

For \(P(a)=[1:a:a^3:a^4]\), the secant through distinct finite \(a,b\) lies on \(q\) precisely when \(a^2+ab+b^2=0\), equivalently \(a^3=b^3\). Otherwise it is an ordinary bisecant. At finite \(a\), \(q(\ell P(a)+mP'(a))=-3a^2m^2\), so its tangent has length two for \(a\ne0\), but the endpoint tangent is a trisecant. Ordinary bisecants through infinity are included. Explicit line equations for finite \(a,b\) are
\[
\begin{aligned}
T_0&=x_2-(a^2+ab+b^2)x_1+ab(a+b)x_0,\\
T_1&=x_3-(a+b)(a^2+b^2)x_1+ab(a^2+ab+b^2)x_0.
\end{aligned}
\]
After removing the common factor \((t-as)(t-bs)\), their restrictions are \(s(t+(a+b)s)\) and \(t^2+(a+b)st+(a^2+ab+b^2)s^2\). For a secant through infinity, \(T_0=x_1-ax_0\), \(T_1=x_2-a^3x_0\), with residual quadrics \(s^2\) and \(t^2+ast+a^2s^2\). The exact executable identity check is [verify_session_genus_two_line_positions_2026_10_10.m2](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/verify_session_genus_two_line_positions_2026_10_10.m2).

A useful limitation: three intersections of \(C\) with \(\Gamma\) do **not** automatically produce three branch points of the residual degree-two conductor cover. Horizontal components can be connected to the strict curve by ADE chains and contracted, identifying points downstairs. The separate all-length chain arguments must be used instead of naive branch counting. Also, the adjoint pencil argument gives \(h^0(M,-K_M)=1\), not \(h^0(M,-nK_M)=1\) for every \(n\); the mate correction may have fractional coefficients.



## 16. Bisection fiber counts: integral descent and the three-center obstruction

These are separate characteristic-zero, second-pencil **conditional** obstructions, not substitutes for the global ribbon proof. On the four-blowup model, with entire fibers (F_t), center counts (k_t), and relative canonical terms (R_t),
[
Z_t=rac{k_t}{2}F_t-R_t,qquad ccdot Z_t=k_t,qquad sum_t k_t=4.
]
For positive even (k_t), the full exceptional correction is integral and supported on complete connected exceptional graphs. The descent of (mathcal O_M(c+Z_p)) makes the smooth embedded curve Cartier at a singular downstairs point, a contradiction. This excludes partitions ([4]), ([2,2]), and ([2,1,1]), including infinitely near centers and nonreduced fibers. The original [even-fiber proof](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md#6-consequences-and-surviving-scope) retains the full descent argument and its hypotheses.

The distinct [three-center analysis](../../arguments/carriers/genus_two_bisection_three_center_proof.md) classifies all permitted original fiber types and forced exceptional graphs for (k_t=3): (A_3), (D_4), or (D_n) ((nge5)). The nonreduced (D_n) case satisfies the rational intersection equations, so numerical negativity alone does not exclude it. An **integral anti-nef uniformizer cycle** with contact coefficient one fails at the trivalent fork. Thus ([3,1]) is excluded within that conditional argument, leaving ([1,1,1,1]) at this stage. The focused proof preserves the exact center histories and coefficient calculations.

## 19. Genus-two marked section case

### Free-chain proof when the marked prime is absent

Assume that the horizontal prime \(B=e_0-e_i-e_j\) of plane degree zero
is absent. In the plane marking below there is one double center \(p_0\)
and eight simple centers. For the strict exceptional curve
\(D_i=e_i-\sum_{j\succ i}e_j\), nefness gives
\(L\cdot D_i=m_i-\sum_{j\succ i}m_j\ge0\), where \(j\succ i\)
denotes a proximate center, \(m_0=2\) and \(m_i=1\) for \(i>0\).
Each simple center has at most one proximate child. The double center
must be proper and can have at most one proximate child, since two would
produce \(B\). A satellite would require two proximate children at the
older of its two exceptional curves. The clusters are therefore free
chains. A simple cluster with \(N\) centers has null prefix
\(A_{N-1}\), ending at the last center of positive \(L\)-degree.
The chain rooted at \(p_0\) cannot meet a horizontal proper line, which
avoids \(p_0\).

Smooth embedded descent permits at most one \(h\)-positive prime per
connected exceptional graph. The \(h\)-positive exceptional primes
are proper lines. A horizontal one passes through four simple centers
and a vertical one passes through \(p_0\) and two simple centers.
Once a free chain leaves a line it cannot return, since the next center
lies at a different point of the previous exceptional divisor.

At a singular point on the smooth downstairs curve, choose a local
function on \(S\) restricting to a uniformizer on that curve. The
exceptional part \(Y\) of its full pullback has positive integral
coefficients. The proper part has nonnegative intersection with every
exceptional prime, so \(Y\) is anti-nef. The unique transverse contact
has coefficient one, since the pullback has order one on the strict
curve. When a contacted \((-3)\)-curve \(H\) meets the \(s\)-th vertex
of an \(A_{s+t-1}\) chain, write its chain coefficients as \(y_j\),
with \(y_0=y_{s+t}=0\). The differences
\(d_j=y_j-y_{j-1}\) are nonincreasing and have a drop of at least one
at \(s\). Since they are integral, either \(d_s\ge1\) or
\(d_{s+1}\le-1\), so \(y_s\ge\min(s,t)\). At \(H\), the sum of
neighbor coefficients must be at most three.

For a single horizontal line \(H\), a chain of \(s\) centers on it
followed by \(t>0\) centers off it contributes \(st/(s+t)\) to the
Schur complement at \(H\); for \(t=0\) the terminal curve has
positive \(L\)-degree and the cluster contributes no arm. The unique
horizontal line has coefficient one in \(Z\). Its equation
\(Z\cdot H=-1\) and the homogeneous chain equations require the
contributions to sum to two. For the attached clusters
\(A=\sum s\le4\) and \(T=\sum t\le4\).
Cauchy gives \(\sum st/(s+t)\le AT/(A+T)\le2\), with equality only
when \(A=T=4\) and each \(s=t\). The integer chain test then requires
a sum of neighboring coefficients at least four, contradicting three.

Two disjoint horizontal proper lines on the resolution share exactly one
simple plane center and together use seven of the eight simple centers.
The shared cluster follows at most one line, say \(H_1\). It cannot leave
that line, since the resulting null chain would connect both
\(h\)-positive lines in one exceptional graph. Hence its null prefix is an
endpoint \(A_k\) arm on \(H_2\), with \(k\le3\). The one center
outside the lines can create at most one additional endpoint \(A_s\) arm,
\(s\le3\), with the sharper restriction \(s\le3-k\) if the arm is on
\(H_1\). It cannot attach in the shared cluster. The two contributions
are at most \(3/4\) each. The sum of the two horizontal coefficients
\(1/(3-d_i)\), where \(d_i\) is the sum of arms on that line, is at most
\(8/9\) when the arms are split and at most one when they are on the
same line. The required \(K_M\cdot Z=1\) forces the latter bound to
be attained, with \(k=s=3\).

The equality configuration uses two clusters. The shared root follows
\(H_1\) for three more centers. A second root on \(H_2\) follows that
line for two more centers and takes the only center off both lines.
A vertical exceptional line through \(p_0\) cannot contain both
roots, whose joining line is \(H_2\), and cannot contain later centers
at either root because its direction differs from that of the first
child. There is no vertical exceptional proper line. The two horizontal
lines therefore give \(h\cdot Z=1\), contrary to \(h\cdot Z=3\).

Two preliminary bounds fail. Four consecutive on-line centers followed
by four off-line centers give an \(A_7\) arm attached at its middle,
not a four-vertex bound. Its rational coefficient at \(H\) can be
one, but the integral anti-nef cycle requires a neighboring coefficient
of at least four. In the two-line case a shared root followed by three
centers on \(H_1\) gives an \(A_3\) arm on \(H_2\), allowing coefficient
\(4/9\) there and \(1/3\) on the isolated line, so the proposed individual
bound \(2/5\) fails. A second \(A_3\) arm can arise from the remaining
off-line center; the proposed total bound \(19/21\) misses this case.

Independent review accepted both line cases under the characteristic-zero
marked section and smooth descent hypotheses with \(B\) absent. The
integer recurrences and intersection inequalities alone remain available
when those geometric inputs are established in another characteristic.
[Original free-chain proof and negative controls](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/GENUS_TWO_LAMBDA_ONE_HORIZONTAL_LINE_BUDGET.md).

### Marked constraints and the case with the horizontal prime

For the genus-two section stratum \(\lambda=1\), the plane marking gives
\[
c^\#=h,\quad L=4h-2e_0-\sum_{i=1}^8e_i,\quad
f=h-e_0,\quad Z=L-h=3h-2e_0-\sum_{i=1}^8e_i,
\]
with \(Z\) effective, exceptional, \(K\cdot Z=1\), and \(Z^2=-3\). The vertical root lattice is \(D_8\). The marked blowup clusters and proximity relations are part of the geometry: they cannot be replaced by an arbitrary abstract ADE graph. A candidate horizontal degree-zero exceptional prime is \(B=e_0-e_i-e_j\); when it is present, a satellite can attach it to an **internal** vertex of an \(A\)-chain. A blanket three-arm-star classification is therefore false.

Under the additional assumption that \(B\) is **absent**, the free-chain and line-budget analysis excludes the section case. The proof first requires an **integral anti-nef cycle** with contact coefficient one at the unique contacted exceptional prime; rational correction coefficients alone do not suffice. The possible horizontal proper lines through the first center have tightly constrained center incidence. The one-line case fails the integral contact and coefficient budget. In the two-line equality case the two horizontal lines each contain the required marked centers, but no vertical proper exceptional line can supply the missing \(h\)-degree: the total horizontal coefficient gives \(h\cdot Z=1\), contrary to \(h\cdot Z=3\). This two-line conclusion was independently accepted. Consequently any surviving \(\lambda=1\) configuration must contain \(B\). The free-child and one-satellite graphs with \(B\) present remain a separate boundary; neither a reduced-conductor shortcut nor the invalid universal star bound excludes them. [Marked-model derivation](../../arguments/carriers/genus_two_marking_and_section_proof.md).
