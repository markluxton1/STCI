# Residual speciality and first-moment vanishing

**Review status.** The residual-linkage criterion and the single-repeated-
component filtration were independently reconstructed during the November 23,
2026 first-moment investigation. The written account was independently
checked by a distinct Sol/max correctness reviewer on the same date.
The input moment theorem and conormal splitting retain their existing reviews.
The full one-triple proof in Section 5 and the source-space identity (RS2a)
were also independently reconstructed by a distinct algebraic-geometry
reviewer; the latter identity received a separate generalizations check.

## 1. A low-degree symmetry criterion from linkage

Let \(k\) be algebraically closed, \(S=k[x_0,x_1,x_2,x_3]\), and let a
diagonal \(\mathbf G_m\)-action preserve a reduced pure curve
\(Y\subset\mathbf P^3\). Suppose \(J=(F_a,G_b)\), \(a\le b\), is a
homogeneous height-two complete intersection with reduced support \(Y\).
Write \(Z=V(J)\) and let \(R\) be the residual curve defined by
\(I_R=J:I_Y\). If \(Z=Y\), the residual is empty.

**Residual symmetry criterion.** If
\[
 H^1(R,\mathcal O_R(b-4))=0,                         \tag{RS1}
\]
then \(F_a\) is an actual eigenform when \(a<b\), and \(J\) is an
invariant ideal when \(a=b\). This assertion is valid in every
characteristic. It does not require \(Y\) or \(R\) to be arithmetically
Cohen–Macaulay or locally complete intersection.

**Proof.** A reduced pure curve is locally Cohen–Macaulay. Complete-
intersection linkage gives a locally Cohen–Macaulay residual \(R\) and
the ideal-sheaf isomorphism
\[
 \mathcal I_Y/\mathcal J\simeq\omega_R(4-a-b).       \tag{RS2}
\]
For the precise classical hypotheses, see Franco–Kleiman–Lascu,
[*Gherardelli linkage and complete intersections*](https://arxiv.org/pdf/math/0003075),
Propositions 2.1 and 2.3, especially (2.3.1–2.3.2).
Shared components are allowed. If the residual is empty the quotient is zero.

Serre duality identifies the dual of the group in (RS1) with
\(H^0(\omega_R(4-b))\). Twist (RS2) by \(a\) and take sections.
In fact \(H^1(\mathcal J(a))=0\): the twisted CI Koszul sequence has
line-bundle terms \(\mathcal O(-b)\), \(\mathcal O\) and
\(\mathcal O(a-b)\), whose relevant intermediate cohomology on
\(\mathbf P^3\) vanishes. Therefore
\[
 (I_Y)_a/J_a\simeq H^0(\omega_R(4-b)),\qquad
 h^1(\mathcal O_R(b-4))=\dim(I_Y)_a-\dim J_a.       \tag{RS2a}
\]
The assumed vanishing gives
\[
                 (I_Y)_a=J_a.                      \tag{RS3}
\]
Here the CI ideal is saturated, since \(S/J\) has depth two, so global
sections of \(\mathcal J(a)\) are exactly \(J_a\).

Since \(Y\) is invariant, (RS3) is an invariant subrepresentation of
\(S_a\). If \(a<b\), it is the line \(kF_a\), so \(F_a\) is an
eigenform. If \(a=b\), it is \(\langle F_a,G_a\rangle\), and its
generated ideal is invariant. Split-torus representations decompose into
weight spaces in every characteristic; an infinitesimal-action argument
and a characteristic-zero integrability step are unnecessary. \(\square\)

**First-moment consequence.** Suppose now \(\operatorname{char}k\ne2\)
and the entire cycle is
\[
 [Z]=\sum_i n_i[C_{u_i,v_i}],\qquad
 C_{u,v}=[s^4:s^3t:u st^3:v t^4],\qquad
 ab=4\sum_i n_i.
\]
Here \((u_i,v_i)\in(k^\times)^2\) are pairwise distinct; repeated
components are recorded in the positive integers \(n_i\).
Each reduced component is invariant for weights \((0,1,3,4)\).
Thus (RS1) implies
\[
                         M_1=\sum_i n_i u_i/v_i=0   \tag{RS4}
\]
by the [invariant/eigenform moment theorem](chow_arrangement_moments.md#the-first-moment-theorem).
In particular, a counterexample to UM1 in characteristic zero must have
nonzero residual speciality \(H^1(\mathcal O_R(b-4))\).
Nonzero cohomology is only a necessary escape from this criterion; it
neither supplies a counterexample nor proves that the actual source breaks
symmetry.

## 2. One repeated component, with arbitrary multiplicity

Assume the translated-cycle hypotheses above, with exactly one component
\(C\) having multiplicity \(n\ge2\), and every other component simple.
The parameters and number of simple components are unrestricted. Then
\[
                    4b\ge7n+1\quad\Longrightarrow\quad M_1=0.
                                                               \tag{RS5}
\]

**Proof.** At a generic component of \(Z\), its Artinian CI algebra
has length \(n_i\); the ideal of \(Y\) is the maximal ideal there.
The residual quotient is the quotient by its one-dimensional socle, and
has length \(n_i-1\). Thus \(R\) is supported only on \(C\), with
generic length \(r=n-1\). Liaison makes \(R\) pure. The maximal ideal
of an Artinian local ring of length \(r\) has \(r\)-th power zero;
purity extends this generic vanishing to
\[
                    \mathcal I_C^r\mathcal O_R=0.
\]
Filter \(\mathcal O_R\) by these ideal powers. Each quotient
\(\mathcal G_j=\mathcal I_C^j\mathcal O_R/
\mathcal I_C^{j+1}\mathcal O_R\), \(0\le j<r\), is a quotient of
\(\operatorname{Sym}^j N^*_{C/\mathbf P^3}\). The
[conormal splitting](../../results/quartic_conormal_characteristic_jump.md)
in characteristic different from two, transported by diagonal scaling, is
\(N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-7)^{\oplus2}\).
Therefore \(\mathcal G_j(t)\) is a quotient of
\[
                 \mathcal O_{\mathbf P^1}(4t-7j)^{\oplus(j+1)}.
\]
If \(4t-7j\ge-1\), this quotient has zero \(H^1\): in its kernel
sequence the source has zero \(H^1\) and the kernel has zero \(H^2\).
This remains valid if \(\mathcal G_j\) has torsion; no normal-flatness
or line-bundle hypothesis on the layers is imposed.

It follows by the finite filtration that
\[
 4t\ge7(r-1)-1\quad\Longrightarrow\quad H^1(\mathcal O_R(t))=0.
\]
Taking \(t=b-4\), \(r=n-1\), gives precisely \(4b\ge7n+1\).
Apply (RS1–RS4). \(\square\)

For \(n=2\), the bound is \(b\ge4\), which is automatic: if
\(a\le b\le3\) and \(4\mid ab\), the only possibility is
\((2,2)\), whose total multiplicity is one. Hence **exactly one doubled
component and any number of simple components satisfy UM1 in every
bidegree**. Here the residual is the reduced smooth quartic itself.

For \(n=3\), the bound is \(b\ge6\). In characteristic zero the
remaining small-degree cases also satisfy UM1, by Section 5 below.

## 3. Several double components: an explicit conductor bound

Suppose every \(n_i\) is one or two. Let \(D\) be the reduced union of
the \(r\) doubled components. The actual residual \(R\) is exactly
\(D\): its generic lengths are \(n_i-1\), so it is generically reduced,
and liaison gives purity. A generically reduced pure curve is reduced.
For \(r=0\) the original ideal is already reduced and invariant.

For \(r\ge1\), write the doubled parameters as \((u_i,v_i)\) and put
\[
 h_i=v_i^2/u_i^3,\qquad
 \alpha_i=3(r-1)+\#\{j\ne i:u_j=u_i\},\qquad
 \beta_i=3(r-1)+\#\{j\ne i:h_j=h_i\}.
\]
Then the sufficient, configuration-sensitive bound is
\[
 4(b-4)\ge\max_i(\alpha_i+\beta_i)-1
       \quad\Longrightarrow\quad M_1=0.             \tag{RS6}
\]

**Proof.** On branch \(i\) near \(p_0\), with coordinate \(z=x_1/x_0\),
the other coordinates are \((u_i z^3,v_i z^4)\). For each \(j\ne i\),
choose the local equation \(x_2/x_0-u_jz^3\) of branch \(j\) when
\(u_i\ne u_j\), and \(x_3/x_0-v_jz^4\) otherwise. Their product
vanishes on every other branch and restricts to a nonzero scalar times
\(z^{\alpha_i}\) on branch \(i\). Surjectivity onto the smooth branch
local ring supplies every multiple of this branch-supported function.
At infinity use \(z=x_2/x_3\); the cubic and quartic parameters are
\(h_i=v_i^2/u_i^3\) and \(v_i^3/u_i^4\), giving order \(\beta_i\).

For the normalization \(\nu:\coprod_i\mathbf P^1_i\to D\), this proves
the conductor inclusion
\[
 \nu_*\!\bigoplus_i
 \mathcal O_{\mathbf P^1_i}(-\alpha_i p_0-\beta_i p_\infty)
       \ \subset\ \mathcal O_D
\]
with zero-dimensional cokernel. After twisting by \(t\), its source
has zero \(H^1\) if \(4t\ge\max_i(\alpha_i+\beta_i)-1\).
The same follows for \(\mathcal O_D(t)\), proving (RS6) by (RS1–RS4).
The conductor calculation itself is valid in every characteristic.
\(\square\)

For \(r\ge2\) in characteristic different from two, at most one other
point can share both \(u_i\) and \(h_i\): it must have \(v_j=-v_i\).
Thus \(\alpha_i+\beta_i\le7r-6\), and a uniform sufficient condition is
\[
 b-4\ge\left\lceil\frac{7(r-1)}4\right\rceil.      \tag{RS7}
\]
If neither cubic parameter repeats, the stronger bound is
\(4(b-4)\ge6r-7\). For smaller generator degree \(a=4\),
\(r\le\lfloor b/2\rfloor\); hence (RS7) covers every \(b\ge17\),
as well as the odd values \(11,13,15\). This is a multiplicity-at-most-two
statement, not an all-mate theorem on arbitrary quartic carriers.

## 4. The exact two-double residual in degree one

For two distinct doubled components, let
\(\eta_i=u_i^2/v_i\). There is an exact formula
\[
 h^1(\mathcal O_D(1))
   =[u_1=u_2]+[h_1=h_2]+[\eta_1=\eta_2],           \tag{RS8}
\]
where brackets are ordinary integer indicators, not field-valued sums.
The formula is valid in every characteristic.

**Proof.** Put \(e=[u_1=u_2]\), \(f=[h_1=h_2]\), and
\(g=[\eta_1=\eta_2]\). The branch intersections have lengths
\(3+e\) and \(3+f\) at the endpoints, giving
\(p_a(D)=5+e+f\) and \(\chi(\mathcal O_D(1))=4-e-f\).
Write a section on normalization branch \(i\) as
\(\sum_{j=0}^4 a_{ij}s^{4-j}t^j\).
At \(p_0\), gluing requires equality of the coefficients indexed
\(0,1,2\), and of index \(3\) if \(e=1\).
At infinity the coefficients through cubic order in \(x_2/x_3\),
using the \(x_3\) trivialization, are
\[
 (a_{i4}/v_i,\ a_{i3}/u_i,\ a_{i2}v_i/u_i^2,\ a_{i1}h_i).
\]
The first three must agree, and the fourth must agree if \(f=1\).
The extra cubic conditions are redundant with the opposite endpoint's
linear conditions. The common quadratic coefficient is free exactly when
\(\eta_1=\eta_2\), and otherwise is zero. Thus
\(h^0(\mathcal O_D(1))=4+g\), and Riemann–Roch gives (RS8).
\(\square\)

Consequently a \((4,5)\) counterexample with all multiplicities at most
two would require two doubled components sharing at least one of
\(u,h,\eta\). These special loci are not excluded by this argument.

## 5. One tripled component in every degree, in characteristic zero

Assume characteristic zero, exactly one component of multiplicity three,
and every other component simple. Then \(M_1=0\) in every bidegree.
Section 2 covers \(b\ge6\); for \(b\le5\), divisibility \(4\mid ab\)
and total multiplicity at least three leave \((3,4),(4,4),(4,5)\).
The first two have existing
[low-degree coverage](universal_first_moment_proof_boundary.md#target-and-proved-coverage).
We prove the remaining case by recovering an irreducible extreme component
of the actual quartic generator, not by asserting that the original pair
is invariant.

In degree \((4,5)\), the cycle is \(3C_1+C_2+C_3\), with three distinct
translates. Set \(Y=C_1\cup C_2\cup C_3\). Its actual residual is a
pure double structure \(R\) on \(C_1\); purity gives
\(\mathcal I_{C_1}^2\mathcal O_R=0\). The nilideal is a torsion-free
rank-one sheaf on the smooth \(C_1\), hence a line bundle
\(\mathcal O_{\mathbf P^1}(\ell)\), with
\[
 0\to\mathcal O_{\mathbf P^1}(\ell)\to\mathcal O_R
       \to\mathcal O_{C_1}\to0,\qquad \ell\ge-7.
\]
The inequality follows from its conormal quotient. If \(\ell\ge-5\),
twisting by one gives zero \(H^1\), so (RS1) applies. Otherwise
\(\ell=-7\) or \(-6\). The standard liaison genus formula gives
\[
 p_a(R)-p_a(Y)=\tfrac12(4+5-4)(8-12)=-10,
 \quad p_a(R)=-\ell-1,
 \quad p_a(Y)=9-\ell\in\{16,15\}.                 \tag{RS9}
\]

The [exact endpoint ranks](arrangement_endpoint_delta.md#the-exact-two-endpoint-rank-formula)
leave only three possibilities for a reduced union of three translates:
\[
\begin{array}{c|c|c}
\text{parameter condition at }p_0&\text{weighted basis}&\delta_0\\\hline
\operatorname{rank}(1,u,v)=3&1,u,v&7\\
v=\alpha u+\beta,\ u\text{ nonconstant}&1,u,u^2&9\\
u\text{ constant}&1,v,v^2&12.
\end{array}
\]
Their weights are respectively \((0,3,4),(0,3,6),(0,4,8)\).
In the middle case distinctness forces three distinct \(u\)-values.
At infinity the same table holds for
\(u'=v^2/u^3,\ v'=v^3/u^4\). Since
\(p_a(Y)=\delta_0+\delta_\infty-2\), genus fifteen is impossible;
genus sixteen forces \(\delta_0=\delta_\infty=9\). Therefore
\[
 v_i=\alpha u_i+\beta,\qquad
 v_i'=\alpha'u_i'+\beta',
\]
with three distinct values in each cubic parameter.

Both intercepts are nonzero. If \(\beta=0\), all three curves have
the same \(q=u/v\) and lie on the same smooth quadric. Each has ruling
class \((1,3)\), so a quartic containing them must contain the quadric:
its \((4,4)\) restriction cannot contain \((3,9)\). The proper subpair
consisting of that quadric and \(G_5\) would have degree ten and only
quartic translated components, an impossibility. Reversal preserves
\(u'/v'=u/v\), so the same argument excludes \(\beta'=0\).

Now put
\[
 E_4=x_0^3x_3-\alpha x_0^2x_1x_2-\beta x_1^4,
 \qquad
 E_{12}=x_3^3x_0-\alpha'x_3^2x_1x_2-\beta'x_2^4.
\]
We claim \((I_Y)_4=\langle E_4,E_{12}\rangle\). Indeed the
degree-four monomial evaluation lists at weights zero through eight are
\[
 \{1\},\{1\},\{1\},\{1,u\},\{1,u,v\},\{u,v\},
 \{u,v,u^2\},\{v,u^2,uv\},\{u^2,uv,v^2\}.
\]
With \(v=\alpha u+\beta\), \(\beta\ne0\), and three distinct
\(u\)'s, every list is independent except the one-dimensional kernel
at weight four. For the three-element lists this follows by expansion
in the basis \(1,u,u^2\); the determinants are nonzero powers of
\(\beta\), up to sign. Reversal proves the remaining weights, with
its only kernel at weight twelve.

The polynomial \(E_4\) is primitive and linear in \(x_3\) over
\(k[x_0,x_1,x_2]\): its coefficient \(x_0^3\) is coprime to its
constant term because \(\beta\ne0\). Gauss's lemma makes it
irreducible. Reversal gives the same for \(E_{12}\).
Thus every actual quartic generator in this pencil has an irreducible
extreme weight component. The established
[cycle-preserving regular-initial-sequence lemma](chow_realization_moment_separation.md#3-cycle-preserving-regular-initial-sequences)
provides an invariant proper CI with the same entire cycle. The accepted
moment theorem proves \(M_1=0\). \(\square\)

## 6. Meaning and remaining gap

Here \(R=Z:Y\) removes one layer along every supported component. It
is distinct from an off-support residual curve in a decomposition into a
curve-primary part and unwanted components.

The obstruction converts a cohomology vanishing into an actual equation-
symmetry statement and then uses the established trace theorem. By (RS2a),
at this particular twist its dimension is already determined by the
reduced support's degree-\(a\) equation space and the CI degrees. Thus the
criterion is also a source-space rigidity condition; the additional
filtration and conductor bounds are what establish new covered classes.
They use the actual residual or its justified identification with a reduced
union, and do not assume symmetry lifts from a cycle to an arbitrary ideal.

The multiplicity bound is sufficient, not claimed optimal. For a hypothetical
sole-supported pair, \(n=ab/4\); (RS5) would require
\(b(16-7a)\ge4\). Thus it supplies no new sole-support exclusion for
\(a\ge3\). Its gain is a new covered class of repeated arrangements and
a source-sensitive residual-cohomology condition for UM1. Higher residual
speciality and the particular source classes in (RS2) remain genuine
unresolved information. No unrestricted characteristic-zero STCI theorem
or classification of repeated arrangements follows.

In characteristic zero a nonzero-moment counterexample must therefore
have at least two repeated components, or have a unique repeated component
of multiplicity \(n\ge4\) with \(4b\le7n\). This necessary restriction
does not assert that either remaining class is nonempty.
