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
