# A first moment and a linear Chow separator for translated CI arrangements

**Review, November 20, 2026:** independent review checked the finite-free
trace, congruence and one-eigenform extensions, component multiplicities,
linear Chow separator, closure corollary and scope qualifications below.
Let \(k\) be algebraically closed of characteristic different from two, and put
\[
 H=\{[1:t:t^3:t^4]\},\qquad
 C_{u,v}=[s^4:s^3t:u st^3:v t^4],\qquad u,v\in k^\times.
\]
Here \(H\) is the intrinsic torus, acting with integer weights
\((0,1,3,4)\), and \(C_{1,1}=C_0\).
Covered actual pairs have invariant ideals, an eigenform generator, or
the polynomial congruences (2). Reduced translated CI arrangements
automatically have invariant ideals. Repeated cycle support alone does
not establish any of these hypotheses.

## The first-moment theorem

Suppose \(I=(F,G)\subset S=k[x_0,x_1,x_2,x_3]\) is a homogeneous
height-two complete-intersection ideal with whole cycle
\[
 [V(I)]=\sum_i n_i[C_{u_i,v_i}],\qquad
 n_i>0,\qquad m=\sum_i n_i,\qquad \deg F\deg G=4m.
\]
Assume that \(I\) is \(H\)-invariant, that one actual generator is an
eigenform, or that the pair satisfies (2) after exchanging and rescaling.
Then
\[
                         \sum_i n_i\frac{u_i}{v_i}=0. \tag{1}
\]
The same sum is the first moment of the scalar function
\(x_1x_2/(x_0x_3)\) on the component parameters.

**Proof.** First suppose the ideal is invariant. The
[equivariant generator lemma](../../results/torus_eigenvector_generator_lifting.md)
supplies actual eigenform generators with the same ordinary degrees
\(a,b>0\). A proper CI is pure, so the stated cycle leaves no other
projective support. In particular the middle vertices
\([0:1:0:0]\), \([0:0:1:0]\) are absent. The pure powers covering
those vertices occur in different generators. After exchanging and
rescaling them, \(F,G\) have weights \(a,3b\), respectively, and
\[
 F\equiv x_1^a\pmod{x_0^2},\qquad
 G\equiv x_2^b\pmod{x_3^2}. \tag{2}
\]
Indeed an ordinary-degree-\(a\), weight-\(a\) monomial satisfies
\(e_0=2e_2+3e_3\), and every term other than \(x_1^a\) is divisible by
\(x_0^2\). For weight \(3b\), similarly \(e_3=3e_0+2e_1\).

Set \(A_0=k[x_0,x_3]\) and \(E=S/I\). The
[finite-free trace proof](../torus_sextic_residuals.md#trace-obstruction-for-supported-pairs)
applies here without its sole-support assumption: (2) implies that
\[
 {\cal B}=\{x_1^i x_2^j:0\le i<a,\ 0\le j<b\}
\]
generates \(E\) over \(A_0\), by induction on ordinary degree after
reduction modulo \((x_0,x_3)\). The free graded module on this set has
Hilbert series \((1-z^a)(1-z^b)/(1-z)^4\), equal to that of the regular
sequence quotient \(E\). Thus the surjection is an isomorphism, and
\({\cal B}\) is a basis of the finite free \(A_0\)-algebra \(E\).

Multiplication by \(x_1x_2\) has ordinary degree two and weight four.
Every diagonal matrix entry in this homogeneous eigenbasis is therefore
a scalar multiple of \(x_0x_3\). Consequently
\[
               \operatorname{Tr}_{E/A_0}(x_1x_2)=\alpha x_0x_3.
\]
Modulo \((x_0^2,x_3^2)\), the algebra is exactly
\[
 \bigl(A_0/(x_0^2,x_3^2)\bigr)[x_1,x_2]/(x_1^a,x_2^b).
\]
In the displayed basis, multiplication by \(x_1x_2\) has zero diagonal.
Trace commutes with base change, and \(x_0x_3\) remains nonzero in this
base ring; hence \(\alpha=0\). This uses the explicit matrix diagonal,
not an assertion that a nilpotent matrix over a nonreduced ring has
zero trace.

Now pass to \(K=k(x_0,x_3)\). Each reduced component cone contributes a
degree-four field extension of \(K\): the equation
\(x_1^4=x_0^3x_3/v_i\) is Eisenstein at \(x_3\), and \(x_2\) is recovered
from \(x_1x_2=(u_i/v_i)x_0x_3\). Its contribution to the trace is therefore
\(4(u_i/v_i)x_0x_3\). A generic multiplicity \(n_i\) multiplies this
contribution by \(n_i\): use a composition series of the corresponding
Artinian local \(K\)-algebra, whose successive simple quotients are
its residue field. Trace additivity thus gives
\[
 0=\operatorname{Tr}_{E/A_0}(x_1x_2)
   =4x_0x_3\sum_i n_i\frac{u_i}{v_i}.
\]
Since \(4\ne0\), this proves (1) for invariant ideals.

If the actual pair already satisfies (2), no invariance is needed.
The same finite-free basis exists, and the component calculation gives
\(\operatorname{Tr}(x_1x_2)=4x_0x_3\sum_i n_i u_i/v_i\).
The explicit zero diagonal after base change again forces its scalar
coefficient to vanish, proving (1).

Finally suppose one generator is an eigenform, say
\(F=c\prod_j H_j^{r_j}\). Each irreducible factor \(H_j\) is an eigenform:
greatest minus least occurring weight, called width, is additive for
nonzero products in a graded domain. Each proper pair \((H_j,G)\) has
a translated subcycle of the whole cycle. In the graded domain
\(D=S/(H_j)\), the nonzero image \(g\) of \(G\) has homogeneous radical,
the intersection of the homogeneous primes of that subcycle.
For a nonzero weight component \(g_w\), some \(g_w^N=gh\ne0\);
width additivity forces \(g\) to have width zero. Thus replacing \(G\)
by its corresponding actual weight component gives the same ideal
\((H_j,G)\), which is invariant. This is the
[existing graded-domain reduction](../torus_sextic_residuals.md#trace-obstruction-for-supported-pairs);
primality of \(\sqrt{(g)}\) is unnecessary. Apply (1) to each such pair.
Cartier divisor additivity on \(V(G)\) gives
\([V(F,G)]=\sum_j r_j[V(H_j,G)]\), so the weighted sum proves (1).
Here all \(H_j\) are nonzerodivisors modulo \(G\), by properness.
\(\square\)

A single eigenform factor only constrains its own intersection subcycle;
it does not give (1) for the whole cycle of an arbitrary remaining factor.

If the whole fundamental cycle is reduced, a proper CI is pure and
generically reduced, hence reduced. Its scheme is precisely the union
of the translated curves, each preserved by \(H\). Its ideal is
therefore invariant, so (1) applies without an additional symmetry
hypothesis in that case. This is the
[existing reduced-ideal bridge](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle).

## A regular function on the Chow space

Fix \(m>0\), and let \(R_Z(L,M)\) be the Chow form of an effective
degree-\(4m\) curve cycle \(Z\), in two hyperplane coefficient rows.
Put \(L_0=x_3-x_0\), and consider the Chow open subset
\[
                         U=\{R_Z(L_0,x_0)\ne0\}.
\]
Every translated cycle \(\sum_i n_i[C_{u_i,v_i}]\) belongs to \(U\):
each curve meets \(L_0=0\) in the dense torus, where \(x_0\ne0\).
On \(U\), normalize
\[
 f_Z(y,z)=\frac{R_Z(L_0,x_0+yx_1+zx_2)}{R_Z(L_0,x_0)},\qquad
 \tau(Z)=[y]f_Z\,[z]f_Z-[yz]f_Z. \tag{3}
\]
These coefficient ratios and \(\tau\) are regular functions on \(U\).

To calculate (3), intersect \(Z\) with \(L_0\). For a translated cycle,
list the resulting \(4m\) points with multiplicity and write
\(X_\ell=x_1/x_0\), \(Y_\ell=x_2/x_0\). The defining product property
of the Chow form gives
\[
 f_Z(y,z)=\prod_{\ell=1}^{4m}(1+yX_\ell+zY_\ell).
\]
The product of the linear coefficients includes every \(X_\ell Y_j\),
whereas the mixed coefficient omits precisely the terms with
\(\ell=j\). Thus
\[
 \tau(Z)=\sum_{\ell=1}^{4m}X_\ell Y_\ell
        =4\sum_i n_i\frac{u_i}{v_i}. \tag{4}
\]
The final equality uses \(x_3=x_0\) on the section and
\(x_1x_2=(u_i/v_i)x_0x_3\) on \(C_{u_i,v_i}\).
For \(\operatorname{char}k\ne2\), each reduced translated curve has four
distinct section points; repeated cycle components are simply repeated
factors. Formula (3) involves no division by two.

In fact a linear Chow coefficient suffices. Let \(A_0,A_y,A_z,A_{yz}\)
be the constant, \(y\), \(z\), and \(yz\) coefficients of
\(R_Z(L_0,x_0+yx_1+zx_2)\), each a linear function of the Chow coefficients.
On the section of \(C_{u,v}\), \(t^4=v^{-1}\), \(X=t\), \(Y=ut^3\).
The sums of \(t\) and of \(ut^3\) over the four roots both vanish.
Consequently every translated cycle satisfies
\[
 A_y=A_z=0,\qquad
 A_{yz}=-4A_0\sum_i n_i u_i/v_i,\qquad
 \tau=-A_{yz}/A_0. \tag{5}
\]
Thus \(A_{yz}=0\) is a global linear Chow equation for all the covered
CI cycles in the first-moment theorem.

## What this excludes, and what remains open

Let \({\cal A}_m\) be the cycle image of all proper homogeneous pairs
covered by the theorem, with whole degree-\(4m\) cycle consisting of
translated quartics. Equations (1) and (5) give \(A_{yz}=0\) on \({\cal A}_m\), hence
on its closure in the full projective Chow space. At every full collision,
\[
                   \tau(m[C_{u,v}])=4m\,u/v.
\]
If \(\operatorname{char}k\nmid4m\), this is nonzero. Since \(A_0\ne0\)
and \(A_{yz}=-A_0\tau\), this full collision lies outside that Chow
hyperplane. Therefore
\[
        m[C_{u,v}]\notin\overline{{\cal A}_m}
        \quad\hbox{for every }u,v\in k^\times. \tag{6}
\]
In particular (6) always holds in characteristic zero. It excludes a
full collision even after leaving the CI locus in the Hilbert scheme:
the resulting Chow limit itself cannot be \(m[C_{u,v}]\).
No scheme-level identification of the full Chow-polytope fiber with
\(\operatorname{Sym}^m(\mathbf G_m^2)\) is used.

This also applies to the closure of reduced Chow-matched CI cycles.
The generic distinct configuration in the full symmetric power has no
CI realization of any type with degree product \(4m\): (1) puts every
reduced realization on the proper closed first-moment locus. This is a
necessary condition only. For example the
[reduced quartic realization locus](../equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts)
has dimension four inside the eight-dimensional symmetric power,
whereas this first-moment hypersurface has dimension seven.
Partial collisions and cycle limits on the coordinate boundary remain possible.

The moment also relates the two fixed-carrier examples. On the smooth
quadric family \(u=v\), every summand \(u/v\) equals one, excluding
characteristic-zero realizations in the theorem's covered equation classes.
On the fixed quartic family
\(C_a=[s^4:a s^3t:st^3:t^4]\), one has \(u/v=a\), so (1) is the first
of the [fixed-carrier moments](fixed_carrier_chow_arrangements.md#parameter-space-and-characteristic-dependence).
The second and fifth moments there come from additional descent gaps.

In characteristic zero, a hypothetical sole-support CI must fall outside
all three covered classes and its cycle outside their Chow-image closure.
The [one-carrier trace tests](chow_trace_cone_jets.md) give additional
presentation conditions for the same moment in arbitrary degrees.
The [quartic classification](quartic_chow_pencils.md#classification)
gives a separate proof for every \((4,4)\) pencil. It realizes non-invariant
pencils outside the invariant quartic Chow closure, even though the
moment vanishes on both loci. Higher-degree non-invariant lifts
without the trace hypotheses remain open.

A connected torus cannot nontrivially permute a finite set of components.
Restricting component parameters to a one-dimensional subtorus or coset
of \(T/H\) is a different condition, not assumed here.


## The homogeneous transverse Chow form as a section norm

**New synthesis, pending independent review.** The first moment above is
only the first coefficient of a more canonical object. The algebraic inputs
are classical: a zero-dimensional Chow form is a norm/determinant of
multiplication, and border-basis theory characterizes genuine multiplication
tables. The project-specific point is to write that norm in the homogeneous
transverse coordinates of the translated-quartic family and compare it with
the resultant of the actual homogeneous sources.

Use homogeneous transverse coordinates
\[
 p=[W:U:V],\qquad C_p=[Ws^4:Ws^3t:Ust^3:Vt^4]
\]
on \(WUV\ne0\), so \(C_{[1:u:v]}=C_{u,v}\). For
\(Z=\sum_i n_i[p_i]\), \(\sum_i n_i=m\), retain
\[
 {\cal C}_Z(X,Y,Z_0)=\prod_i(W_iX+U_iY+V_iZ_0)^{n_i}. \tag{CHN1}
\]
Its binary specialization is
\[
 H_Z(A,B)\doteq{\cal C}_Z(0,-B,A)
 =\prod_i(V_iA-U_iB)^{n_i}. \tag{CHN2}
\]
Thus \(H_Z\) remembers \(U_i/V_i\), while \({\cal C}_Z\) retains the paired
homogeneous transverse coordinates.

Take the symmetric transverse plane \(\Pi:x_3-x_0=0\), with moving line
\(M_{\alpha,\beta,\gamma}:\alpha x_0+\beta x_1+\gamma x_2=0\). For one
translate put
\[
\begin{aligned}
 \Psi_{W,U,V}(\alpha,\beta,\gamma)
 ={}&WV^3\alpha^4-4WUV^2\alpha^2\beta\gamma-W^2V^2\beta^4\\
   &+2WU^2V\beta^2\gamma^2-U^4\gamma^4 . \tag{CHN3}
\end{aligned}
\]
This is bihomogeneous of degree four in both triples. On the torus it is,
up to scalar, the Chow form of \(C_p\cap\Pi\). Indeed
\[
 \Psi_{1,u,v}
 =\operatorname{Res}_t(vt^4-1,\alpha+\beta t+\gamma u t^3),
\]
and hence
\[
 \prod_{t^4=v^{-1}}(\alpha+\beta t+\gamma u t^3)
 =\alpha^4-4{u\over v}\alpha^2\beta\gamma-{1\over v}\beta^4
 +2{u^2\over v^2}\beta^2\gamma^2-{u^4\over v^3}\gamma^4. \tag{CHN4}
\]

Define the multiplicative transform
\[
 {\cal N}_Z(\alpha,\beta,\gamma)
 :=\prod_i\Psi_{W_i,U_i,V_i}(\alpha,\beta,\gamma)^{n_i}. \tag{CHN5}
\]
It is determined by the factorization of \({\cal C}_Z\) and has degree
\(4m\) in the moving-line coordinates. This is the precise
Galois-polynomial interface: \({\cal C}_Z\) records the unordered transverse
roots, while \({\cal N}_Z\) is their norm through the universal quartic
kernel (CHN3).

For an actual proper degree-\((a,b)\) pair \(Y=V(F,G)\) with translated
fundamental cycle \(Z\), \(ab=4m\), the projective resultant on \(\Pi\)
gives
\[
 \boxed{\operatorname{Res}_{\Pi}
 (F|_\Pi,G|_\Pi,\alpha x_0+\beta x_1+\gamma x_2)
 \doteq{\cal N}_Z(\alpha,\beta,\gamma).} \tag{CHN6}
\]
This is a specialization of the global Chow-resultant certificate, not a new
resultant theorem.

Within the translated-quartic Chow fiber, this one plane loses no
set-theoretic arrangement information. Every linear factor of the section
Chow form has normalized shape
\[
 \alpha+t\beta+ut^3\gamma,
\]
so it recovers \(t\), then \(u\), and then \(v=t^{-4}\). Hence
\(Z\cap\Pi\), and therefore \({\cal N}_Z\), determines the multiset of
transverse parameters with multiplicities. This injectivity is asserted only
on the torus arrangement locus; equality of one plane section for arbitrary
curves does not imply equality of global Chow cycles.

After Chow-polytope rigidity has already placed a candidate in this family,
sole support is therefore equivalent to
\[
 {\cal N}_Z\doteq\Psi_{1,1,1}^{\,m},\qquad
 \Psi_{1,1,1}
 =\alpha^4-4\alpha^2\beta\gamma-\beta^4
  +2\beta^2\gamma^2-\gamma^4. \tag{CHN7}
\]
Without the translated-family hypothesis, (CHN7) is only a section condition.

### Multiplication matrices and all transverse moments

Let \(B_\Pi\) be the finite section algebra of an actual pair in this family.
All support lies in \(x_0\ne0\). Put
\(\xi=x_1/x_0,\eta=x_2/x_0\), with multiplication matrices
\(M_\xi,M_\eta\). Classical norm theory gives
\[
 {{\cal N}_Z(1,y,z)\over{\cal N}_Z(1,0,0)}
 =\det(I+yM_\xi+zM_\eta). \tag{CHN8}
\]
Thus the transverse Chow polynomial is literally a joint
characteristic/norm polynomial.

In characteristic zero,
\[
 \log\det(I+yM_\xi+zM_\eta)
 =\sum_{\ell\ge1}{(-1)^{\ell+1}\over\ell}
   \operatorname{Tr}(yM_\xi+zM_\eta)^\ell, \tag{CHN9}
\]
and for a translated arrangement
\[
 \operatorname{Tr}(M_\xi^rM_\eta^s)=
 \begin{cases}
  4\displaystyle\sum_i n_i u_i^s v_i^{-(r+3s)/4},
       &r+3s\equiv0\pmod4,\\
  0,&r+3s\not\equiv0\pmod4,
 \end{cases} \tag{CHN10}
\]
for \(r,s\ge0\), not both zero. This follows by summing
\(u_i^s t^{r+3s}\) over \(t^4=v_i^{-1}\).

The existing first moment is exactly
\[
 [y]{\cal N}\,[z]{\cal N}-[yz]{\cal N}
 =\operatorname{Tr}(M_\xi M_\eta)
 =4\sum_i n_i{u_i\over v_i}. \tag{CHN11}
\]
Thus the binary \(H_Z\) is the natural polynomial for the first trace, while
the full \({\cal C}_Z\) and \({\cal N}_Z\) retain the paired higher moments.

The congruences (2) do **not** make all higher moments vanish. Modulo
\((x_0^2,x_3^2)\), \((r,s)=(1,1)\) is the only positive mixed trace whose
possible diagonal coefficient
\(x_0^{(3r+s)/4}x_3^{(r+3s)/4}\) survives. Higher vanishings require stronger
source information.

### Literature boundary and the remaining problem

D'Andrea--Jeronimo, *Rational Formulas for Traces in Zero-Dimensional
Algebras* (AAECC 19 (2008), 495--508, arXiv:math/0503721), supply the
classical Chow/trace input. Kehrein--Kreuzer, *Characterizations of Border
Bases* (J. Pure Appl. Algebra 196 (2005), 251--270), supply the classical
border-basis/commuting-multiplication-matrix criterion.

The project-specific application is (CHN3), fixed-plane injectivity on the
translated-quartic fiber, and the identification of the old first Chow
separator with the first coefficient of the full norm transform. Independent
review is pending.

The realization question is now finite and source-facing: determine which
\({\cal C}_Z\) have \({\cal N}_Z\) in the resultant image of the prescribed
homogeneous section spaces. The perfect-power target (CHN7) is still an exact
form of the original existence problem, not an obstruction by itself.
Progress must extract lower-complexity coefficient, rank, tangent, or
border-algebra conditions on that image.
