# A hypothetical STCI fixes the first-jet symplectic pairing, but that condition is realizable with residual curves

**Scope (2026-11-22):** characteristic zero, \(C=C_{1,1}\), homogeneous actual CI \(Y=V(F_a,G_b)\) with hypothetical \(Y_{\rm red}=C\). The main Poisson/Jacobian identity and relative Gorenstein residue are accepted/established sources; the explicit all-degree control and the normal-order gap are elementary deductions, **pending independent mathematical review**. No new STCI exclusion.

## Exact first-jet consequence

Set \(S=k[x_0,x_1,x_2,x_3]\),
\(L=V(x_0,x_3)\), \(T=k[x_0,x_3]\),
\(R=k[x_1,x_2]\), and
\(Q=x_0x_3-x_1x_2\).
Suppose \(F,G\in I_C\) are homogeneous of degrees \(a,b\),
form a proper CI, and **have sole reduced support** \(C\).
Then \(a,b>0\), \(ab=4m\) and the CI misses \(L\).

Expand the **actual equations** in the first normal
neighborhood of \(L\):
\[
 F=f_0+x_0p+x_3q\pmod{(x_0,x_3)^2},\qquad
 G=g_0+x_0r+x_3s\pmod{(x_0,x_3)^2}.
\]
The restrictions \(f_0,g_0\in R\) have degrees \(a,b\)
and form a binary regular sequence; \(\deg p=\deg q=a-1\),
\(\deg r=\deg s=b-1\).
Put \(M_{ij}=F_iG_j-F_jG_i\).

The **existing sole-support theorem**
[Jacobian duality and Hamiltonian actions](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
gives
\[
 M_{12}-2M_{03}\in(F,G).
\]
Restriction to \(L\) therefore gives the **exact first-jet
Poisson congruence**
\[
 \tag{1}
 J(f_0,g_0)-2(ps-qr)\in(f_0,g_0),\qquad
 J(f_0,g_0):=f_{0,x_1}g_{0,x_2}
            -f_{0,x_2}g_{0,x_1}.
\]
In the graded Artin CI
\(\mathscr A=R/(f_0,g_0)\), socle degree
\(d=a+b-2\), the component \(\mathscr A_d\)
is one-dimensional, and the Grothendieck residue
\(\operatorname{Res}_{f_0,g_0}\) identifies it with \(k\).
Since
\(\operatorname{Res}_{f_0,g_0}J(f_0,g_0)=ab\),
equation (1) is **equivalent** to
\[
 \tag{2}
 \boxed{\operatorname{Res}_{f_0,g_0}(ps-qr)
       =\frac{ab}{2}=2m.}
\]
Thus the first-jet **consequence of the existing Poisson
identity** is one prescribed nonzero scalar, not isotropy.
This statement does **not** say (2) is the only first-jet
restriction that might follow after using the full
scheme-theoretic sole-support condition and higher jets.

Equation (2) agrees with the new
[spectral–Jacobian identity](spectral_jacobian_first_jet_bridge.md):
the canonical spectral divisor of a hypothetical STCI
is \(m[1]\), and hence its moment is \(M_1=m\).
The skew Serre/Macaulay pairing is \(\Omega(v_0,v_3)=2M_1=ab/2\).
On the full translated-cycle CI locus, conjectural
universal vanishing would instead require \(\Omega=0\);
the distinction is exactly what would exclude a
characteristic-zero STCI *if that conjecture is proved*.

## All-degree first-jet flexibility: a strict negative control

For **any integers \(a,b\ge4\)** and scalars
\(\lambda,\mu\in k\), define
\[
 \tag{3}
 \begin{aligned}
 F_{\lambda}
  &=x_1^{a-4}(x_1^4-x_0^3x_3)
       +\lambda x_0Q\,x_1^{a-3},\\
 G_{\mu}
  &=x_2^{b-4}(x_2^4-x_0x_3^3)
       +\mu x_3Q\,x_2^{b-3}.
 \end{aligned}
\]
Both homogeneous equations vanish on \(C\).
On \(L\), their restrictions are
\((f_0,g_0)=(x_1^a,x_2^b)\), whose projective
common zero locus is empty; therefore the pair is
proper. The only nonzero first normal coefficients are
\[
 p=-\lambda x_1^{a-2}x_2,\qquad
 s=-\mu x_1x_2^{b-2},\qquad q=r=0.
\]
Consequently
\[
 ps-qr=\lambda\mu x_1^{a-1}x_2^{b-1},
\quad
 \tag{4}
 \operatorname{Res}_{x_1^a,x_2^b}(ps-qr)=\lambda\mu.
\]
Taking \(\lambda\mu=ab/2\) satisfies **the exact
hypothetical-STCI first-jet congruence (1)**, even
as a polynomial identity after restriction to \(L\).
Taking any other \(\lambda\mu\) gives arbitrary values of
the same scalar for other proper containing pairs.

Yet *all* these pairs have residual curves.
Indeed, on the ambient torus put
\([x_0:x_1:x_2:x_3]=[1:t:ut^3:vt^4]\).
The equations, after dividing by nonvanishing powers of
\(t\) and \(u\), have transverse derivatives at
\(u=v=1\) with determinant
\[
 \tag{5} 4-\lambda t-\mu/t.
\]
This rational function is not identically zero
in characteristic zero, so the intersection has
generic length **one** along \(C\).
Its total degree is \(ab\), and hence the residual
cycle has degree \(ab-4>0\).
For a sextic pair \(a=b=6\), take \(\lambda=1,\mu=18\):
the pair satisfies the full first-jet STCI requirement
\(\Omega=18\), but has residual degree \(32\).
Therefore **first-jet compatibility with the
sole-support Poisson identity does not certify
sole support, at any degrees \(a,b\ge4\)**.

## Why the spectral power cannot detect lower orders in higher degree

A hypothetical sole-support CI has
\[
 \tag{6}Q^m=(x_0x_3-x_1x_2)^m\in(F,G),
 \qquad m=ab/4.
\]
This membership follows already from nilpotence at
the single minimal associated prime, with no
embedded primes. However the *normal-order
truncations along \(L\)* of this relation are
automatically satisfied to substantial depth
for **every** proper degree-\((a,b)\) CI
avoiding \(L\), whether or not it even contains \(C\).

Let \(E=S/(F,G)\). Graded Nakayama and the binary
CI \(R/(f_0,g_0)\) give a graded **free**
\(T\)-module decomposition
\[
 E\simeq\bigoplus_{j=1}^{ab}T(-d_j),
 \qquad 0\le d_j\le d=a+b-2 .
\]
Any homogeneous class \(h\in E_N\) with \(N\ge d\)
therefore lies in
\[
 \tag{7} h\in (x_0,x_3)^{N-d}E .
\]
For \(h=Q^m\), \(N=2m=ab/2\), so
\[
 \tag{8}
 Q^m\in(F,G)+(x_0,x_3)^{r_*},
 \qquad
 \boxed{r_*=\frac{ab}{2}-(a+b-2)
              =\frac{(a-2)(b-2)}2.}
\]
The congruence (8) is **tautological** from the
graded module and imposes no new condition on
the first \(r_*-1\) normal orders. For \((4,4)\),
\(r_*=2\); for \((6,6)\), \(r_*=8\);
for \((5,8)\), \(r_*=9\).
This is why directly examining the low-order
spectral power cannot replace the full global
realization test in the currently surviving
high-degree ranges. The first potentially
nontrivial normal coefficient of \(Q^m\) is
at order \(r_*\), **not** order one or two
in the sextic example.

The global vanishing \(Q^m=0\) in \(E\) might
still indirectly constrain first jets through
higher-degree compatibility and source cofactor
relations. (8) only rules out a **low-order
truncation-only** contradiction; it does not
assert first-jet independence from all higher
STCI conditions.

## The first power obstruction is another Serre-duality class

The normal-order bound (8) has a **coordinate-independent leading
term** in the associated graded module of the disjoint line.
Put \(I_L=(x_0,x_3)\), \(R=k[x_1,x_2]\), \(T=k[x_0,x_3]\),
\(d=a+b-2\), \(N=2m=ab/2\), and \(r_*=N-d\).
The graded freeness of \(E=S/(F,G)\) over \(T\), with fiber
\(A=R/(f_0,g_0)\), gives
\[
 \operatorname{gr}_{I_L} E\simeq A\otimes_k T
 \quad\text{as a bigraded *module* (not as an algebra).}
\]
The \(I_L\)-adic leading class of \(Q^m\) therefore lies in
\[
 \tag{9}
 \boxed{
 \mathfrak o_{r_*}(F,G)
 =[Q^m]\in
 \big(I_L^{r_*}E/I_L^{r_*+1}E\big)_N
 \simeq A_d\otimes_k T_{r_*}
 \simeq H^1(L,\omega_L)\otimes_k
       \operatorname{Sym}^{r_*}\langle x_0,x_3\rangle .
 }
\]
The first identification of the *particular graded piece* is
canonical: modulo the first powers of \(I_L\), the fiber quotient
is precisely \(A\), and only fiber degree \(d\) can contribute
at base degree \(r_*\). The identification \(A_d\simeq
H^1(L,\omega_L)\) uses the ordered binary Koszul complex.
Its vanishing is independent of the choice of CI generators
and of the identification of the Serre line.

Thus \(\mathfrak o_{r_*}\) is a **binary form of degree \(r_*\)**
with coefficients in the *same* Serre-duality line that
contains the first-jet pairing
\(\Omega(v_0,v_3)=ab/2\).

There is a useful cohomological proof that no lower-order
power obstruction exists. At order \(j\), lifting a presentation
\(Q^m=UF+VG\) reduces to the surjectivity of
\[
 R_{N-a-j}\oplus R_{N-b-j}
 \xrightarrow{(f_0,g_0)}R_{N-j}.
\]
Its cokernel is \(A_{N-j}\). In the relevant range
\(0\le j\le r_*\), the twisted Koszul sequence on
\(L\simeq\mathbf P^1\) gives
\[
 A_{N-j}\simeq
 H^1\bigl(L,\mathcal O_L(N-a-b-j)\bigr).
\]
For \(j<r_*\) this is zero because
\(N-a-b-j\ge-1\). At \(j=r_*\) it is
\(H^1(L,\mathcal O_L(-2))\simeq k\).
This is exactly the graded Macaulay/Serre duality
behind (9), via standard line-bundle cohomology
([Stacks, Tag 01XS](https://stacks.math.columbia.edu/tag/01XS)).

A **necessary** condition for sole support is therefore
\(\mathfrak o_{r_*}(F,G)=0\). It is not sufficient:
later filtration orders and the full power membership
\(Q^m\in(F,G)\) still matter. In degree \((4,4)\), the
first obstruction is a **quadratic** form on the base
\(x_0,x_3\); in degree \((6,6)\), it is an **octavic**,
with nine coefficients. This gives an exact geometric
interface between the first-jet Serre scalar and the
later spectral-power obstruction. There is **no proved
universal relation** carrying the prescribed nonzero
first-jet class to a nonzero \(\mathfrak o_{r_*}\).

### The first obstruction is a degree-uniform *linear map on the spectral form*

The preceding leading-class construction applies to **any**
homogeneous polynomial of degree \(N=2m\), not only \(Q^m\).
For \(a,b>0\) with \(ab=4m\), let
\(\mathbf H_m=\operatorname{Sym}^m\langle A,B\rangle\)
denote the \((m+1)\)-dimensional space of binary
homogeneous spectral forms, where
\(A=x_1x_2\) and \(B=x_0x_3\).
There is a canonical linear map associated with the actual CI:
\[
 \tag{9a}
 \boxed{
 \Phi_{F,G}:\mathbf H_m
  \longrightarrow
  H^1(L,\omega_L)\otimes_k
        \operatorname{Sym}^{r_*}\langle x_0,x_3\rangle,
 \quad
 H\longmapsto[H(A,B)]_{I_L^{r_*}} .
 }
\]
The class is well-defined because **every**
degree-\(2m\) element of \(E=S/(F,G)\) has
\(I_L\)-order at least \(r_*\).
No choice of a Groebner basis, projection splitting
or cofactor presentation is required.

For an entire translated-cycle CI, the [canonical
spectral equation](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation)
satisfies \(H_\sigma(A,B)\in(F,G)\), so
\[
 \tag{9b}\boxed{H_\sigma\in\ker\Phi_{F,G}.}
\]
For a hypothetical sole-support STCI the prescribed
element of this kernel is exactly
\((A-B)^m\). Thus the **first** global
compatibility condition on the known cycle
is a set of at most \(r_*+1\) linear equations
in the **coefficients of its spectral form**,
whose matrix depends algebraically on the
actual pair \(F,G\). Later \(I_L\)-orders
still impose additional conditions.

This is a direct coefficient-level interface between
the full Chow/spectral approach and the equation-source
approach, rather than a carrier-by-carrier test.
It does not prove that \(M_1\) must vanish:
kernel membership can allow nonzero first coefficient
for special pairs, and the map depends on the
same equations being tested. Determining the
rank and kernel of \(\Phi_{F,G}\) on the full
translated-cycle equation incidence is a
precise bounded algebraic problem.

### The leading obstruction equals a *single relative Grothendieck residue*

The map \(\Phi_{F,G}\) has a more concrete expression
in the **same relative residue functional** as the
first-jet area. Let
\[
 \mathcal R_{F,G}:E\longrightarrow T(-d),\qquad
 d=a+b-2
\]
be the relative Grothendieck residue for fiber
variables \(x=x_1,y=x_2\) and ordered equations
\((F,G)\), with orientation \(dx\wedge dy\).
The standard residue normalization is homogeneous
of degree \(-d\), \(T\)-linear and commutes with
specialization at \(u=v=0\).
On the binary Artin CI \(A=R/(f_0,g_0)\), it
annihilates all degrees below \(d\) and
induces a nonzero functional \(A_d\to k\).

Take any homogeneous \(h\in E_N\) with \(N\ge d\),
and write it in an arbitrary graded \(T\)-free
basis lifting a homogeneous basis of \(A\).
Every basis vector of fiber degree \(d_i<d\)
has zero relative residue **by degree**, while
the unique vector of degree \(d\) has
nonzero *constant* residue. Its coefficient
is necessarily a binary form of degree
\(N-d\) in \(u,v\).
Consequently,
\[
 \tag{9c}
 \boxed{
 [h]_{I_L^{N-d}}=0
 \quad\Longleftrightarrow\quad
 \mathcal R_{F,G}(h)=0;
 \qquad
 \Phi_{F,G}(H)
 =\mathcal R_{F,G}(H(A,B)).
 }
\]
Both sides take values in the Serre top-degree
line, with the canonical residue trace fixing
its scalar normalization. Thus the **first
spectral-power obstruction is exactly**
\[
 \tag{9d}
 \boxed{P_{F,G}(u,v)
 :=\mathcal R_{F,G}\bigl((uv-xy)^m\bigr)
 \in k[u,v]_{r_*}.}
\]
The STCI hypothesis forces \(P_{F,G}=0\);
this condition is necessary, not sufficient
for \(Q^m\in(F,G)\). It is not the same
as ordinary algebra trace (which inserts
the relative Jacobian into the residue).

For general homogeneous spectral forms
\(H(A,B)=\sum_{j=0}^m h_jA^{m-j}B^j\),
the T-linearity of the residue gives
\[
 \tag{9e}
 \boxed{
 \Phi_{F,G}(H)
 =\sum_{j=0}^{\lfloor r_*/2\rfloor}
 h_j(uv)^j\,
 \mathcal R_{F,G}\bigl((xy)^{m-j}\bigr).
 }
\]
Terms with \(j>r_*/2\) vanish because
their residue would have negative base degree.
In particular the **entire** degree-\(m\)
Chow spectral form is tested through
finitely many higher relative residue
moments, not through an ad hoc choice of
cofactors.

The STCI comparison now has a particularly
uniform form:
\[
 \tag{9f}
 \underbrace{\mathcal R_{F,G}(M_{03})=ab/2}
       _{\text{accepted sole-support Poisson/first-jet theorem}},
 \qquad
 \underbrace{\mathcal R_{F,G}(Q^m)=0}
       _{\text{necessary spectral nilpotence}}.
\]
These are evaluations of the **same** duality
functional on **different homogeneous
numerators**. In the quartic control family,
\(\mathcal R_{F,G}(Q^4)=(\lambda\mu-4)uv\).
No universal identity expressing the second
residue in terms of the first has been proved.
The missing implication concerns the full
global support/equation compatibility, not
the existence of either residue.

### Explicit quartic compatibility failure in the control family

For \(a=b=4,m=4,r_*=2\), specialize (3) to
\[
 F=x^4-\lambda u x^2y+O((u,v)^3),\qquad
 G=y^4-\mu v xy^2+O((u,v)^3),
\]
with \(x=x_1,y=x_2,u=x_0,v=x_3\).
The actual family (3) has exactly these normal layers:
its remaining terms have orders three or four.
Modulo the two equations and normal order three,
\[
 x^4\equiv\lambda ux^2y,\qquad
 y^4\equiv\mu vxy^2.
\]
Consequently
\[
 \begin{aligned}
 Q^4=(uv-xy)^4
 &\equiv x^4y^4-4uv\,x^3y^3\\
 &\equiv(\lambda\mu-4)uv\,x^3y^3
        \pmod{(F,G)+(u,v)^3}.
 \end{aligned}
\]
Since \([x^3y^3]\) generates the
socle \(A_6=k[x,y]/(x^4,y^4)\), the first power
obstruction is
\[
 \tag{10}
 \boxed{\mathfrak o_2(F,G)
   =(\lambda\mu-4)\,uv\otimes[x^3y^3].}
\]
Thus \(Q^4\in(F,G)\) **requires**
\(\lambda\mu=4\) for this family, while the
sole-support Jacobian identity (1) **requires**
\(\lambda\mu=8\). They cannot hold simultaneously.

This is an **exact failure of compatibility between
the two necessary conditions**, and it remains true
for any modification of the family that preserves
its normal layers through order two.
It is **not** a new proof of all \((4,4)\) exclusions:
generic first normal layers and second normal
terms have not been classified or eliminated.
The full \((4,4)\) exclusion is already an established
independent result. In higher degrees the first
power obstruction arises much later and can involve
many higher normal equation layers, so (10)
cannot simply be copied to \((6,6)\).

## A stronger negative control: both *leading* STCI conditions can hold

The incompatible \((4,4)\) family above
has the specialized jets \(q=r=0\).
Allowing the two other first normal jets
shows that its incompatibility does **not**
extend to arbitrary first-jet presentations.

Take **any** proper quartic pair with
\(f_0=x^4,\ g_0=y^4\), and write
\[
 F=x^4+u p+v q+O((u,v)^2),\qquad
 G=y^4+u r+v s+O((u,v)^2),
\]
where \(p,q,r,s\in k[x,y]_3\). Put
\(\rho=\operatorname{Res}_{x^4,y^4}\),
which extracts the coefficient of \(x^3y^3\).
The simultaneous **first normal Poisson requirement**
and **first spectral power requirement** become
\[
 \tag{11}
 \rho(ps-qr)=8,
\]
\[
 \tag{12}
 \boxed{
 P_{F,G}(u,v)
 =u^2\rho(pr)
 +uv\bigl(\rho(ps+qr)-4\bigr)
 +v^2\rho(qs)=0.
 }
\]
To prove (12), reduce
\(Q^4=(uv-xy)^4\) modulo
\((F,G)+(u,v)^3\). Its terms of normal
order at most two are \(x^4y^4-4uvx^3y^3\).
Replacing \(x^4,y^4\) by their *first*
normal equations yields exactly (12).
Higher normal layers of either defining
equation cannot affect this order-two class
because each of \(x^4,y^4\) already
vanishes in the binary CI.

Equations (11) and (12) are **compatible**:
they require
\[
 \rho(pr)=\rho(qs)=0,\qquad
 \rho(ps)=6,\quad\rho(qr)=-2.
\]
The simple choice
\[
 \tag{13}
 p=x^3,\quad q=y^3,\quad
 r=-2x^3,\quad s=6y^3
\]
satisfies all four scalar conditions.

Crucially, these jets arise from **actual homogeneous
global equations containing \(C\)**. Set
\[
 U=x_0^2x_2-x_1^3,\qquad
 V=x_2^3-x_1x_3^2,\qquad Q=x_0x_3-x_1x_2,
\]
and define
\[
 \tag{14}
 \boxed{
 F=(x_1^4-x_0^3x_3)-x_0U+x_3V,\qquad
 G=(x_2^4-x_0x_3^3)+2x_0U+6x_3V.
 }
\]
All three of \(Q,U,V\) vanish on \(C\),
and both binomial quartics do as well.
Thus \(F,G\in I_C(4)\).
Their restrictions to \(L\) are
\(x_1^4,x_2^4\), so the pair is
proper and misses the projection center.
The first normal coefficients are exactly
(13), and hence
\[
 \boxed{\Omega(v_0,v_3)=8,\qquad
        \mathcal R_{F,G}(Q^4)=0.}
\]
These are **both** of the necessary low-order
STCI conditions, with no formal or source-lifting
assumption: the equations themselves are global.

Nevertheless \(Y_{\rm red}\ne C\).
Indeed, on the dense torus
\([1:t:w t^3:z t^4]\), the transverse
Jacobian determinant of \((F,G)\) at
\(w=z=1\) is
\[
 \tag{15}
 -t^7\bigl(t^{18}-18t^{10}-20t^9-3t^8-2\bigr),
\]
which is not identically zero in characteristic
zero. The generic intersection multiplicity
along \(C\) is therefore one, and Bézout
gives a residual cycle of degree \(16-4=12\).

The two first **failing higher-jet tests** of this
global pair can also be written down without
computing its residual curve:
\[
 \tag{16}
 M_{12}-2M_{03}
 \equiv 12u\,x^2y^3+72v\,x^3y^2
 \pmod{(F,G)+(u,v)^2},
\]
\[
 \tag{17}
 Q^4
 \equiv 2u^2v\,x^2y^3
       +12uv^2\,x^3y^2
 \pmod{(F,G)+(u,v)^4}.
\]
Both are nonzero. For (16), expand the actual
gradients and note that the two displayed
monomials represent independent classes in
\((R/(x^4,y^4))_5\).
For (17), reduce
\(x^4=-ux^3-vy^3+O((u,v)^3)\) and
\(y^4=2ux^3-6vy^3+O((u,v)^3)\)
iteratively; the order-two terms cancel
by (12), but at order three the displayed
coefficients remain.
The higher corrections of (14) only begin
at normal order three, so they do not
alter this calculation.
Hence the **full** Poisson identity fails
already at order one, while the
**full** spectral power identity fails at
order three. Passing the leading scalar
residue tests is not passing either
full ideal-membership requirement.

**Conclusion of the paired controls.**
The special family with \(q=r=0\) is
incompatible at second normal order
(\(\lambda\mu=4\) versus \(8\)); but
the general first normal data can
satisfy the Poisson/spectral leading
conditions simultaneously, even for
actual global containing pairs.
Consequently there is **no contradiction
from these two leading tests alone**.
One must impose the **full**
membership \(Q^m\in(F,G)\) and the complete
actual Poisson/source incidence, not merely
their lowest nontrivial residue classes.
The \((4,4)\) unrestricted exclusion is
independently known and is **not** being
reproved here. The example is a diagnostic
against overpromoting the restricted
compatibility failure into a theorem.

## Implication and stopping rule

The direct first-jet check gives **no obstruction**:
a hypothetical STCI must have nonzero symplectic
jet area \(ab/2\), and there are proper global
containing pairs with precisely that area and
nonzero residual degree. The new useful question
is whether the *full* joint Poisson and spectral
power equations prohibit this prescribed area
when combined with the entire reduced-support
condition. A proof that **all** translated-cycle
CIs have area zero would contradict (2) and
settle the characteristic-zero rational quartic
STCI problem. No such theorem is claimed here.
