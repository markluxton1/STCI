# Optimal low-degree Chow polarizations from the quadric and opposite cubic rulings

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed the quadric/cubic weighted pullback, residual ruling removal, ordinary fat-point coefficient ideals and summed first-moment syzygy. Inherited inputs are classical Chow-form/norm identities and generic Artinian nilpotence.

**Status:** new project-specific elementary derivation, **covered by the scoped correctness review above**. Characteristic zero and algebraically closed \(k\) for the full ordinary fat-point coefficient ideal; the identities and generic Artin-nilpotence containments themselves work in every characteristic. This strengthens the [degree-four full-Chow pullback envelope](full_transverse_chow_pullback_envelope.md) but **does not prove** universal \(M_1=0\).

**Literature and accepted inputs checked:** the standard rational-quartic divisor class \((1,3)\) on a smooth quadric and its quadric plus three cubic generators ([*The Practice of Algebraic Curves*](https://doi.org/10.1090/gsm/218)); the two-ruling divisor calculation on \(\mathbf P^1\times\mathbf P^1\); the classical Chow polynomial of finite points and Artinian nilpotence; CM/unmixedness of homogeneous complete intersections (Stacks [00S8](https://stacks.math.columbia.edu/tag/00S8), [00N2](https://stacks.math.columbia.edu/tag/00N2)). The [existing full paired Chow/moment theorem](transverse_chow_moment_realization.md) and [spectral–Jacobian bridge](spectral_jacobian_first_jet_bridge.md) remain the project authorities for their separate conclusions.

## 1. The first two independent transverse pencils occur in degrees two and three

Let
\[
 A=x_1x_2,\quad B=x_0x_3,\qquad
 Q_\xi=A-\xi B,
\]
and put
\[
 T_u^+=x_0^2x_2-u x_1^3,\qquad
 T_{u^-}^-=x_1x_3^2-u^-x_2^3.
\]
All are eigenforms for the **intrinsic** torus of
weights \((0,1,3,4)\).
Their ordinary degrees and intrinsic weights are
\[
\begin{array}{c|ccc}
 &Q_\xi&T_u^+&T_{u^-}^-\\ \hline
\deg&2&3&3\\
\operatorname{wt}&4&3&9
\end{array}
\]
For a translated quartic
\(C_{u,v}=[s^4:s^3t:u\,st^3:v\,t^4]\),
define
\[
 \xi=u/v,\qquad u^- =v^2/u^3=1/(\xi^2u).
\]
Then **both** pairs \((\xi,u)\) and \((\xi,u^-)\)
are unimodular coordinate systems on the
two-dimensional transverse torus, related by
\[
 v=u/\xi,\qquad u^-=1/(\xi^2u).
\]
Each of \(Q_\xi,T_u^+,T_{u^-}^-\) vanishes identically on
\(C_{u,v}\).

**Classical quadric-ruling geometry.**
On the smooth quadric \(Q_\xi\), \(C_{u,v}\)
has divisor class \((1,3)\); the restriction
of a cubic surface has class \((3,3)\).
The two cubics have divisors
\[
 \tag{1}
 \boxed{
 [Q_\xi\cap V(T_u^+)]=[C_{u,v}]+2[L_{01}],\qquad
 [Q_\xi\cap V(T_{u^-}^-)]=[C_{u,v}]+2[L_{23}]
 }
\]
as effective Cartier divisors on \(Q_\xi\),
where \(L_{01}=V(x_0,x_1)\) and
\(L_{23}=V(x_2,x_3)\) are skew ruling lines.
To check the multiplicity along \(L_{01}\),
at its generic point \(x_2,x_3\) are units;
\(Q_\xi\) makes \(x_1\) a unit multiple of
\(x_0\), and then \(T_u^+\) vanishes to
order exactly \(2\) in \(x_0\).
The opposite statement follows by coordinate
reversal. The translated quartic is generically
reduced in either intersection because
\((\xi,u)\), respectively \((\xi,u^-)\),
are étale coordinates on the transverse torus.
Their degree \(4\), plus twice the ruling
line degree \(1\), exhausts Bézout \(2\cdot3=6\).
The multiplicity two is **not** an asserted
embedded structure at the shared endpoints.

## 2. A degree-\(2m,\ldots,3m\) full-paired Chow system

For
\(\sigma=\sum_i n_i[(u_i,v_i)]\)
with \(m=\sum_i n_i\), let
\[
 Q_i=A-\xi_iB,\quad
 T_i^+=x_0^2x_2-u_ix_1^3,\quad
 T_i^-=x_1x_3^2-u_i^-x_2^3.
\]
Use the **two alternative toric embeddings** of
the same paired cycle, in coordinates
\((\xi,u)\) and \((\xi,u^-)\), and define
\[
 \tag{2}
 \Theta_\sigma^\pm(\lambda,\mu;x)
  =\prod_i(\lambda Q_i(x)+\mu T_i^\pm(x))^{n_i}
  =\sum_{j=0}^m\lambda^{m-j}\mu^j
     \Theta^\pm_j(\sigma;x).
\]
Each coefficient is an ambient
**homogeneous intrinsic-torus eigenform**:
\[
 \tag{3}
 \boxed{
 \deg\Theta_j^\pm=2m+j,\qquad
 \operatorname{wt}\Theta^+_j=4m-j,\qquad
 \operatorname{wt}\Theta^-_j=4m+5j.
 }
\]
In particular,
\(\Theta_0^+=\Theta_0^-
 =H_\sigma(A,B)=\prod_i(A-\xi_iB)^{n_i}\),
the previously established canonical
**quadric-spectrum member** of a
translated-cycle CI. Its coefficient
\(-[A^{m-1}B]H_\sigma=M_1\).

**Proposition A (two new shorter all-degree
actual-ideal systems).**
If \(J=(F_a,G_b)\) is a proper
homogeneous **scheme-theoretic CI**
with entire fundamental cycle
\(\sum_i n_i[C_{u_i,v_i}]\), then
\[
 \tag{4}
 \boxed{\Theta^\pm_j(\sigma;x)\in J
   \qquad(j=0,\ldots,m).}
\]
Proof: at a generic local Artinian
CI of length \(n_i\), the
\(\mathfrak m_i^{n_i}\) power vanishes,
and the \(i\)-th factor in (2)
belongs to \(\mathfrak m_i^{n_i}\).
All other components are handled by
their own factors. Unmixedness of
the complete intersection contracts
the generic containments globally.
No torus invariance of \(F,G\) or
the scheme \(Z\) is assumed.

**Proposition B (support and the dense
ordinary-power ideal).**
Let \(\mathfrak T_\sigma^\pm\)
be the ideals generated by the
coefficients in (2). Then
\[
 \tag{5}
 \begin{aligned}
 V(\mathfrak T_\sigma^+)
   &=\bigcup_i C_{u_i,v_i}\ \cup L_{01},\\
 V(\mathfrak T_\sigma^-)
   &=\bigcup_i C_{u_i,v_i}\ \cup L_{23},\\
 \boxed{
 \sqrt{\mathfrak T_\sigma^++\mathfrak T_\sigma^-}
   &=I_{\bigcup_i C_{u_i,v_i}}.}
 \end{aligned}
\]
At a point, the product of binary linear
polynomials in \(\lambda,\mu\) is identically
zero iff one of those linear factors is
identically zero; use (1).
Since \(L_{01}\cap L_{23}=\varnothing\),
the sum has exactly the desired
global reduced support.

On the ambient dense coordinate torus,
the \(2m+1\) coefficient equations
generate the **same canonical fat-point
envelope** as the [quartic full-Chow
pullback](full_transverse_chow_pullback_envelope.md):
\[
 \tag{6}
 \boxed{
 \mathfrak T_\sigma^\pm|_{\mathbf G_m^3}
 =\bigcap_i I_{C_{u_i,v_i}}^{n_i}
   \bigm|_{\mathbf G_m^3}.
 }
\]
The map \((u,v)\mapsto(\xi,u)\), or
\((\xi,u^-)\), is a unimodular change
of Laurent variables. Near \(p_i\),
the remaining factors give an invertible
linear map between coefficient spaces,
so the coefficient ideal is the
ordinary \(n_i\)-th power of the
maximal ideal (characteristic zero).
Away from the specified points a
coefficient is a unit.

Thus (4)–(6) retain *both paired torus
characters and all multiplicities*,
but lower the ordinary equation-source
degrees from **\(4m\)** to the
**optimal quadric–cubic range**
\(2m\) through \(3m\).
They give one common quadric-spectrum
member plus two **opposite chains**
of \(m\) cubic polarizations.

## 3. First opposite polarizations: an exact syzygy containing \(M_1\)

The two residual ruling divisors have a
particularly simple **ambient
polynomial identity**. For each
paired toric point,
\[
 \tag{7}
 \boxed{
 \frac{x_2^2}{u_i}T_i^+
 +\xi_i^2 x_0^2T_i^-
 =-x_1(A+\xi_iB)\,Q_i.
 }
\]
It follows by direct expansion using
\(u_i^-=(\xi_i^2u_i)^{-1}\),
or geometrically from the rational
function comparing \(2L_{01}\) with
\(2L_{23}\) on \(Q_{\xi_i}\).
Equation (7) is homogeneous of
ordinary degree \(5\) and
intrinsic weight \(9\).

Let
\[
 H=\prod_iQ_i^{n_i},\qquad
 H_i=H/Q_i,
\]
and introduce the **normalized first
cubic polars**
\[
 \tag{8}
 E_+:=\sum_i n_i\,\frac{T_i^+}{u_i}H_i,\qquad
 E_-:=\sum_i n_i\,\xi_i^2T_i^-H_i .
\]
These are the coefficients of
\(\lambda^{m-1}\mu\) in (2) after
rescaling the \(i\)-th cubic
factor by \(1/u_i\), respectively
\(\xi_i^2\). Hence
\[
 \tag{9}
 E_\pm\in J,\quad
 \deg E_\pm=2m+1,\quad
 \operatorname{wt}E_+=4m-1,\
 \operatorname{wt}E_-=4m+5.
\]

Multiplying (7) by \(n_iH_i\)
and summing over all **paired**
toric points gives a new exact
degree-\((2m+3)\) identity:
\[
 \tag{10}
 \boxed{
 x_2^2 E_+ +x_0^2E_-
 +x_1H\bigl(mA+M_1(\sigma)B\bigr)=0,
 \quad M_1(\sigma)=\sum_i n_i\xi_i.}
\]
Every term has **intrinsic weight**
\(4m+5\).
This is the first simple **ambient
syzygy** tying together
- the low-degree quadric-spectrum equation \(H\);
- one degree-\((2m+1)\) first polar from
  each *opposite* toric quotient;
- **the elementary first moment \(M_1\)**
  as the coefficient of \(B=x_0x_3\)
  in the *canonical comparison quadric*
  \(mA+M_1B\).

The formula was verified both
symbolically for a generic toric point
and directly after summing two
independent points; the displayed
termwise proof covers all multiplicities.
For a CI realizing \(\sigma\), all
three \(H,E_+,E_-\) are **actual ideal
members**, so (10) is a concrete
Koszul/cofactor comparison source.

### What the **same two generators** now have to satisfy

The comparison quadric in (10) is
the **first polar** of the spectral
form at the reducible member
\(B=0\):
\[
 \tag{10a}
 mA+M_1B
 =A\,\partial_AH(1,0)
  -B\,\partial_BH(1,0),
\]
because \(H(A,B)=
A^m-M_1A^{m-1}B+\cdots\).
The \(\eta_i\) parameters
**cancel completely** in this
comparison: geometrically this
is the principal difference
between the two residual double
ruling lines on each smooth
quadric. That is precisely
why the *first* elementary
symmetric function of the
quadric parameters appears,
rather than an independent
moment of the cubic parameters.

More concretely, write the
**actual** cofactor identities
\[
 \tag{10b}
 \begin{array}{lll}
 H=h_FF+h_GG,&
 E_+=p_FF+p_GG,&
 E_-=q_FF+q_GG,
 \end{array}
\]
with each cofactor homogeneous
of the uniquely indicated
degree. Substitution into (10)
and the Koszul syzygy theorem
for a regular sequence give
**a homogeneous polynomial**
\[
 \tag{10c}
 T\in S_{2m+3-a-b}
 =S_{(a-2)(b-2)/2+1}
\]
satisfying the **two simultaneous**
equations
\[
 \tag{10d}
 \boxed{
 \begin{aligned}
 x_2^2p_F+x_0^2q_F+
   x_1(mA+M_1B)h_F &= T\,G,\\
 x_2^2p_G+x_0^2q_G+
   x_1(mA+M_1B)h_G &=-T\,F.
 \end{aligned}}
\]
Thus (10d) is the exact
**two-generator lifting condition**
for the first opposite-ruling
Chow syzygy. All unknown
cofactors are constrained by the
*same* \(F,G\) and the *same*
symmetric toric points; they
cannot be chosen independently
one carrier at a time.
For \((a,b)=(4,4)\) the
Koszul multiplier has degree \(3\);
for \((6,6)\) it has degree \(9\).

The Koszul theorem guarantees
such a \(T\) **whenever all the
membership conditions in (10b)
already hold**. Thus (10d) is
an equivalent **source-incidence
formulation**, not an additional
independent obstruction.
To deduce UM1 one would need
to show that this entire
cofactor system is impossible
when \(M_1\ne0\), or isolate
a tighter consequence by
combining it with the opposite
endpoint filtrations.
No cancellation or
degree-count contradiction
has yet been proved.

**Exact boundary of the implication.**
(10) is an *identity of polynomials
constructed from \(\sigma\)*.
It is true even for cycles that are
**not** realizable CIs.
Thus it does **not** by itself
imply \(M_1=0\).
One must prove that the simultaneous
membership of the two opposite
polar chains in the **same
two-generated homogeneous regular
sequence**, including endpoint
gluing, forces the \(B\)-coefficient
of the comparison quadric to vanish.
That further claim is **open**.
In particular, no cancellation
of \(H\) modulo \(J\) is valid
since \(H\in J\), and the ordinary
Koszul-cofactor syzygy of degree
\(2m+3\) can involve a multiplier
of nonnegative degree
\(2m+3-a-b\) (for the admissible
bidegrees). Neither a formal division
nor the presence of the syzygy
is a new STCI exclusion.

## 3.1 Exact lower-degree carrier-free realization incidence

The [full-Chow cofactor/norm criterion](full_transverse_chow_pullback_envelope.md#32-exact-full-cycle-realization-criterion-via-cofactor-identities-and-the-norm)
can now be sharpened **without changing its
hypotheses or its exact scope**.
Fix a prescribed paired translated multicycle
\(\sigma=\sum_i n_i[C_i]\),
\(m=\sum n_i\), and let
\(J=(F_a,G_b)\) be a proper
homogeneous CI with \(ab=4m\).
Then
\[
 \tag{11}
 \boxed{
 [V(J)]=\sigma\quad\Longleftrightarrow\quad
 \begin{cases}
 \mathfrak T_\sigma^++\mathfrak T_\sigma^-\subset J,\\[2pt]
 \operatorname{Nm}_{\mathcal A_J/k[t^{\pm1}]}
    (X+uY+vZ)=\mathcal C_\sigma(X,Y,Z).
 \end{cases}}
\]
As before, the **norm requirement is
redundant when all \(n_i=1\)**.
The inclusion makes the actual
scheme support lie in \(\cup C_i\);
the CI degree gives total generic
transverse length \(m\);
the factorization of the norm
records each local length separately.

The inclusion in (11) consists
precisely of the **same-equations
homogeneous cofactor identities**
\[
 \tag{12}
 \boxed{
 \Theta_j^\pm
 =A_j^\pm F_a+B_j^\pm G_b,\quad
 \deg A_j^\pm=2m+j-a,\quad
 \deg B_j^\pm=2m+j-b,
 \quad j=0,\ldots,m.}
\]
One copy of the \(j=0\) equation
is redundant because it is
the common \(H_\sigma\).
Thus (11)–(12) are an **exact
degree-by-degree** elimination
interface involving only the
two actual surface equations,
the full paired toric points,
and the local length/norm
condition, with **the lowest
possible quadratic spectral
source followed by opposite
cubic corrections**.
They replace \(2(m+1)\)
equations of degree \(4m\)
with \(2m+1\) equations in
degrees \(2m,\ldots,3m\).

This remains an **equivalent
formulation of realization**,
not a new criterion expressed
solely in the toric-point
coefficients, a proof of
\(M_1=0\), or a shortcut around
the unknown scheme structure
of repeated components.

## 4. Improvement, intrinsic meaning, and the remaining gap

The earlier degree-four full-Chow
pullback gave an exact support envelope
with **\(2(m+1)\)** generators
of ordinary degree \(4m\).
The opposite quadric–cubic
polarizations give the same exact
support and generic ordinary-power
envelope using **\(2m+1\)**
degree-\((2m,\ldots,3m)\)
homogeneous eigenforms, sharing \(H\).
For \((6,6)\), \(m=9\):
the new members have degrees
\(18,19,\ldots,27\), rather than \(36\).
For \((4,4)\), \(m=4\):
degrees \(8,\ldots,12\), rather than \(16\).

The geometry is not a coincidental
parameterization: each individual
quadric–cubic intersection has
the quartic and a **double ruling
line**, with the two opposite
charts selecting disjoint residual
lines. The syzygy (10) is
the algebraic comparison between
these two rulings.
It is precisely where the
elementary coefficient \(M_1\)
enters a **joint, degree-uniform
global-equation condition**,
rather than merely appearing as a
coefficient in the Chow form or a
trace on a finite algebra.

The still unresolved statement is
that the image of the **actual
proper-CI realization incidence**
under these low-degree opposite
polarization/cofactor equations
lies in \(M_1=0\).
No such vanishing or elimination
of arbitrary non-invariant
nonreduced pairs is established.
