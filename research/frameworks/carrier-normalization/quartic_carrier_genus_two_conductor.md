# Genus-two bisections and conductor geometry

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

## 9. Genus-two bisection: global ribbon contradiction and distinct conductor algebra

For the bisection lane the second pencil gives an actual Cartier equivalence `2c ~ 2H` on the normal surface, with infinitely-near centers and the entire correction divisor retained. A section Q with divisor 2c defines a pure Cohen–Macaulay double curve R. Its nilradical J is generically square-zero; purity eliminates finite-length subsheaves and makes J square-zero globally and torsion-free rank one on smooth c. The Hilbert polynomial `chi(O_S(mH))=2m²+m+1` yields `chi(O_R)=-6`, hence `chi(J)=-7` and `J=O_P1(-8)`. The actual morphism R to P3 induces a nonzero conormal map `N^*_(C/P3)=O(-7)^2 -> O(-8)`: it is generically nonzero away from the conductor, where normalization is an isomorphism. But `Hom(O(-7),O(-8))=0`, a contradiction. This is the universal bisection exclusion, not a bound on possible mate degrees. [Full independent proof](../../arguments/carriers/genus_two_bisection_proof.md).

The earlier quadratic-descent analysis remains a distinct **conditional conductor-power lemma**: on the entire conductor line, the quadratic algebra has trace-zero generator w with `w²=delta`, and the section Q restricts as `m+w`. A descended power forces, after excluding m=0, `delta=r²`, `m=alpha*r` and `((alpha+1)/(alpha-1))^n=1`, with alpha not 0 or ±1. These equations are necessary under the hypothetical bisection setup, not evidence of surviving mates. The global conormal contradiction supersedes their use as an open-case list; the conductor algebra may still be useful elsewhere.


## 13. Entire genus-two conductor and ambient conic model

For genus-two normalization, rationality of M and `K_M.L=-2` give rational singularities of S by duality and Leray, without assuming K_S is Cartier or Q-Cartier. Finite duality identifies the **actual** conductor ideal `I=Hom_X(nu_*O_S,O_X)=nu_*omega_S`. Its Hilbert polynomial forces `O_Gamma` to have polynomial `m+1`; maximal Cohen–Macaulay purity eliminates embedded points and nilpotent zero-dimensional additions, so Gamma is a reduced line. Dualizing the conductor sequence gives `nu_*O_S/O_X=omega_Gamma=O_Gamma(-2)` and an entire rank-two finite flat conductor algebra `p_*O_D=O_Gamma+O_Gamma(-2)`, including nonreduced and singular fibers. Its quadratic multiplication is a quartic section on Gamma. These are scheme-level assertions, not a calculation of the reduced Jacobian support. [Entire-conductor audit](../../arguments/carriers/genus_two_entire_conductor_proof.md).

The two ambient line equations t0,t1 identify naturally with the complete adjoint pencil `|K_M+L|`; their ratios agree as rational functions. Since that pencil is basepoint free, the pulled-back line ideal is **exactly** `O_M(-D_M)` for an effective `D_M~-K_M`, with no residual zero-dimensional base scheme. The universal blowup property therefore lifts M to the blowup of P3 along Gamma. The image is the integral strict transform T, of class `4H_B-2E_B` because the quartic has generic order exactly two along Gamma. Adjunction gives `omega_T=O_T(-E_B)` and its pullback is `omega_M`. The proper-trace argument proves T normal; its Gorenstein crepant singularities are ADE. This is a theorem about T, **not** an assertion that the original normalization S is Gorenstein or that its pencil descends through horizontal contractions. [Ambient-model audit](../../arguments/carriers/genus_two_ambient_conic_model_proof.md).


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

**Scope:** characteristic-zero genus-two bisection under the second-pencil reduction, not an unrestricted STCI statement. On the four-blowup model \(M\to V\), let \(F_t\) be the **entire** fiber, \(k_t\) the number of centers over it, and \(R_t\) the relative canonical contribution. The exact correction is
\[
Z_t=\tfrac{k_t}{2}F_t-R_t,\qquad c\cdot Z_t=k_t,\qquad \sum_t k_t=4.
\]
Every positive component of \(Z\) is a vertical exceptional \((-2)\)-curve. Positivity of intersections and \((c+Z)\cdot E=0\) show that its positive support contains **whole connected exceptional graphs**, not arbitrary subgraphs.

### Bisection with an even fiber count

If \(k_t>0\) is even, \(Z_t\) is an effective integral divisor. The equality
\(c\cdot Z_t=k_t>0\) puts a point of the strict curve on its positive support.
Let \(p\) be the image of a contacted graph. Support closure means that
the whole exceptional fiber over \(p\) has its integral correction
\(Z_p\) in one full \(f\)-fiber. Thus the line bundle
\(N=\mathcal O_M(c+Z_p)\) has degree zero on every exceptional component
over \(p\).

Apply [Kollár, Chapter 2, Proposition 76(1), PDF pp. 35–36](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
The conductor argument establishes rationality of the singularities of
\(S\). The resolution is log minimal with zero boundary since adjunction
gives \(K_M\cdot E=-2-E^2\ge0\) on every exceptional \((-2)\)- or
\((-3)\)-curve. A log resolution refinement preserves degree zero on
every exceptional component, including the newly created ones. The descent
theorem gives \(N=\sigma^*P\) for an invertible \(P\) near \(p\); it does
not require \(K_S\) to be Cartier or \(\mathbf Q\)-Cartier. Away from
\(p\), \(P\) agrees with \(\mathcal O_S(c_S)\), so reflexivity on the
normal surface identifies the sheaves at \(p\) too.

The actual smooth embedded \(c_S\) is therefore Cartier at \(p\).
If \(g\) is its local equation and \(u\) lifts a generator of the maximal
ideal on \(c_S\), then \((g,u)\) generates the surface maximal ideal by
Nakayama. This forces regularity, contradicting the singular point on the
minimal resolution. The counts allow reducible and nonreduced fibers and
infinitely near centers. The excluded partitions are \([4]\), \([2,2]\)
and \([2,1,1]\), leaving \([3,1]\) and \([1,1,1,1]\) in this argument.

The separate parity auditor checked Proposition 76, support closure, the
entire local correction, reflexive extension to the actual curve and
the regular-local-ring contradiction. Acceptance covers every positive even
count under the characteristic-zero second-pencil and smooth-lift
hypotheses. [Proof and independent decision in the historical source](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md#6-consequences-and-surviving-scope).

**Three-center exclusion (conditional on the same geometric inputs; source originally awaited a separate parent audit).** The nef-anticanonical rational pencil on \(V\) has three possible entire-fiber types: an irreducible smooth component of square zero; a reduced chain with two \((-1)\) ends; or a nonreduced tree with one multiplicity-two \((-1)\) component, two multiplicity-one leaves, and a possibly empty multiplicity-two tail. A blowup of an old \((-2)\) component is forbidden by nefness. For \(k_t=3\), every old \((-1)\) must be hit exactly once, an old square-zero component exactly twice, and a positive-coefficient new exceptional component must finish with square \(-2\). At each new center,
\[
\operatorname{coeff}_{E}(Z_t)=\tfrac32\operatorname{mult}_{E}(F_t)-\operatorname{coeff}_{E}(R_t).
\]
These rules leave exactly the following configurations:

| Original \(V\)-fiber | Forced positive exceptional graph | Obstruction |
| --- | --- | --- |
| Irreducible | \(A_3\) chain, coefficients \(3/2,1,1/2\) | The strict curve has intersection two with the same connected exceptional graph, not one transverse contact |
| Reduced | \(D_4\) star, central coefficient \(2\), leaves \(3/2,3/2,1\) | The strict curve meets both original \((-1)\) ends in one connected graph |
| Nonreduced | \(D_n\), \(n\ge5\), with contact component coefficient \(3\); shortest \(D_5\) correction \(3A+\frac32(B_1+B_2)+2E_1+E_2\) | No positive **integral anti-nef uniformizer cycle** can have coefficient one at the contact component |

The nonreduced case is a substantive near-counterexample to a purely numerical argument: the rational correction is effective and satisfies intersection equations. The obstruction uses a genuine local uniformizer of the smooth downstairs curve. An integral anti-nef cycle with contact coefficient one propagates coefficient one along the \((-2)\) long arm; at the trivalent fork, anti-nefness would demand \(2\ge1+1+1\), impossible. Thus the three-center partition \([3,1]\) is excluded **within the conditional argument**, leaving only \([1,1,1,1]\). Preserve the source's exhaustive center-history proof and status distinction: [three-center fiber analysis](../../arguments/carriers/genus_two_bisection_three_center_proof.md).


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
