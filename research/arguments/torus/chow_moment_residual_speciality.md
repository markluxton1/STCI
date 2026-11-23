# Residual speciality and first-moment vanishing

**Review status.** The residual-linkage criterion and the single-repeated-
component filtration were independently reconstructed during the November 23,
2026 first-moment investigation. The written account was independently
checked by a distinct Sol/max correctness reviewer on the same date.
The input moment theorem and conormal splitting retain their existing reviews.

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
Its vanishing gives
\[
                 (I_Y)_a=J_a.                      \tag{RS3}
\]
Here the CI ideal is saturated, since \(S/J\) has depth two, so global
sections of \(\mathcal J(a)\) are exactly \(J_a\). Exactness at
\(H^0(\mathcal I_Y(a))\) suffices; no vanishing of
\(H^1(\mathcal J(a))\) is asserted or needed.

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

For \(n=3\), the bound is \(b\ge6\). Below that bound, the possible
degree pairs are \((3,4),(4,4),(4,5)\). In characteristic zero the first two have existing
[low-degree coverage](universal_first_moment_proof_boundary.md#target-and-proved-coverage).
The criterion alone leaves \((4,5)\), not an established survivor.

## 3. Meaning and remaining gap

The obstruction uses the actual residual scheme of the complete
intersection, not merely its reduced support or cycle. It converts a
cohomology vanishing into an actual equation-symmetry statement and then
uses the established trace theorem. It does not assume that symmetry
lifts from the cycle to an arbitrary ideal.

The multiplicity bound is sufficient, not claimed optimal. For a hypothetical
sole-supported pair, \(n=ab/4\); (RS5) would require
\(b(16-7a)\ge4\). Thus it supplies no new sole-support exclusion for
\(a\ge3\). Its gain is a new covered class of repeated arrangements and
a source-sensitive residual-cohomology condition for UM1. Higher residual
speciality and the particular source classes in (RS2) remain genuine
unresolved information. No unrestricted characteristic-zero STCI theorem
or classification of repeated arrangements follows.
