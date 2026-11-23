# Residual degree, attachment, and carrier capacity

Fix the embedded quartic \(C=C_0\). For an actual proper homogeneous pair
\(Y=V(F_a,G_b)\), write \([Y]=m[C]+R\) and
\(\delta=\deg R=ab-4m\). Let \(T\) be its **full** \(C\)-primary
component and \(Z\) the residual with no \(C\)-component. Linkage to
reduced \(C\) instead gives \(D_{\rm red}=Y:C\) with cycle \((m-1)[C]+R\).
These three curves must be distinguished before using a degree or attachment
formula.

This chapter consolidates reviewed proofs and counterexamples;
The saturated-flag statement
is [R-0019](../../results/quasiprimitive_residual_cycles.md). The fixed-source jet
statement is [R-0025](../../results/ci_fixed_sextic_jet_rigidity.md).
The [global-model chapter](residual_global_models.md) owns equation spaces,
prescribed attachments, reverse linkage and the two blowups. The full-primary
attachment-module identity is proved first below. It is not a substitute for
full primary extraction; the deformation account applies it to construction.



## Full-primary equation module and exact attachment divisor

For this section put \(I=I_C\), \(L=I_Y\), and \(J=I_T\), and denote by \(D\) the residual linked to the **full** primary component, \(I_D=L:J\). Thus \([D]=R\) and D has no C-component. This D is distinct from the once-link D_red=Y:C. The primary T and its linked D are pure locally Cohen–Macaulay curves; the empty D case is allowed.

## 2. The attachment module and its exact support

Define coherent \(\mathcal O_C\)-modules

\[
\mathcal E_T=J/IJ,\qquad
\mathcal Q_{Y,C}=J/(L+IJ).
\]

Actual equations give

\[
\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)\longrightarrow\mathcal E_T,
\qquad\mathcal Q_{Y,C}=\operatorname{coker}\rho.       \tag{1}
\]

At the generic point of \(C\), \(J=L\); hence \(\rho\) is an isomorphism on the two-dimensional minimal-generator space there. In particular \(\mathcal E_T\) has generic rank two and \(\mathcal Q_{Y,C}\) is torsion.

**Support criterion.**

\[
\operatorname{Supp}\mathcal Q_{Y,C}
=C\cap\operatorname{Supp}D.                          \tag{2}
\]

Indeed, for a closed point \(p\in C\), \(\mathcal Q_p=0\) means \(J_p=L_p+I_pJ_p\). Apply Nakayama to the finite module \(J_p/L_p\), with \(I_p\) inside the local maximal ideal, to obtain \(J_p=L_p\). This says that \(Y\) has only its full marked primary component near \(p\). Conversely that equality gives \(\mathcal Q_p=0\). Since primary decomposition of \(Y\) has no embedded components, equality is equivalent to no residual component passing through \(p\).

For a projective CI, connectedness now gives

\[
\mathcal Q_{Y,C}=0
\quad\Longleftrightarrow\quad
\operatorname{Supp}Y=C.                             \tag{3}
\]

Only this last global equivalence uses connectedness. Formula (2) is local and does not assert every residual component individually meets \(C\).

## 3. Torsion correction to the determinant

Let \(\mathcal T_T=\operatorname{tors}_{\mathcal O_C}\mathcal E_T\), and put

\[
\overline{\mathcal E}_T=\mathcal E_T/\mathcal T_T.
\]

This is a rank-two vector bundle on the smooth \(C\). The induced map

\[
\bar\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)
\longrightarrow\overline{\mathcal E}_T
\]

is generically an isomorphism and injective, with determinant

\[
\theta=\det\bar\rho\in
H^0(C,\det\overline{\mathcal E}_T\otimes\mathcal O_C(a+b))
\]

nonzero. The image of \(\rho\) meets \(\mathcal T_T\) trivially, because its composite to the torsion-free quotient is injective. Thus

\[
0\longrightarrow\mathcal T_T\longrightarrow\mathcal Q_{Y,C}
\longrightarrow\operatorname{coker}\bar\rho
\longrightarrow0.                                  \tag{4}
\]

Over each DVR \(\mathcal O_{C,p}\), Smith normal form gives

\[
\boxed{\ \operatorname{length}\mathcal Q_p
=\operatorname{length}(\mathcal T_T)_p+
\operatorname{ord}_p(\theta).\ }                    \tag{5}
\]

Furthermore \(\mathcal T_T\) is supported precisely where \(T\) fails to be locally a complete intersection. If the torsion vanishes at \(p\), \(\mathcal E_T\) is free of rank two there, and its residue fiber shows \(\mu(J_p)=2\). A height-two ideal with these two generators in a regular local ring is a regular sequence. Conversely a local regular-sequence presentation of \(J_p\) makes \(J_p/I_pJ_p\) free of rank two on \(C\), since all Koszul coefficients vanish on \(C\).

Consequently the determinant alone need not detect every attachment: it omits the non-lci contribution from the full primary component.

## 4. Identification with the actual attachment divisor

Classical linkage duality gives

\[
J/L\simeq\omega_D\otimes\omega_Y^{-1}
=\omega_D(4-a-b).
\]

Taking the quotient by \(I\) identifies

\[
\mathcal Q_{Y,C}\simeq
\omega_D(4-a-b)\otimes_{\mathcal O_{\mathbf P^3}}\mathcal O_C.   \tag{6}
\]

One must not replace a canonical module by a structure sheaf without justification. In this particular codimension-two intersection, their **lengths after restriction** agree even when \(D\) is not Gorenstein.

Here is the local proof. Put \(B=\mathcal O_{D,p}\), a one-dimensional CM local ring, and let \(I_CB=(f,g)\). Since \(D\) has no component equal to \(C\), this is primary to the maximal ideal. Over the infinite residue field choose a linear combination of the two generators which is a nonzerodivisor \(f\) on \(B\). Complete it to an invertible change of the two generators. The quotient \(A=B/fB\) is Artinian, and its canonical module is \(\omega_A=\omega_B/f\omega_B\), up to an irrelevant invertible factor. Matlis duality gives

\[
\operatorname{length}(\omega_A/g\omega_A)
=\operatorname{length}\operatorname{Ann}_A(g)
=\operatorname{length}(A/gA).
\]

The second equality is rank-nullity for multiplication by \(g\) on the finite-length module \(A\). Thus (6) implies

\[
\operatorname{length}\mathcal Q_p
=\operatorname{length}\mathcal O_{C\cap D,p}.          \tag{7}
\]

Since every finite subscheme of smooth \(C\) is an effective Cartier divisor, equal pointwise lengths identify their ideal divisors. Write \(\operatorname{div}\mathcal T_T=\sum_p\operatorname{length}(\mathcal T_T)_p[p]\). Combining (5) and (7) gives

\[
\boxed{\ C\cap D=\operatorname{div}\mathcal T_T+\operatorname{div}\theta\ }
                                                               \tag{8}
\]

as **effective divisors on \(C\)**, or equivalently

\[
I_{C\cap D,C}
=\operatorname{Fitt}_0(\mathcal Q_{Y,C})
=\operatorname{Fitt}_0(\mathcal T_T)\,(\theta).
\]

No equality with sums of contacts of individual branches, a conductor boundary of the total curve, or an exceptional cycle is asserted. Those are different invariants. In particular (8) is not a formula for the complete residual scheme.

### Full thick attachment and the marked normal nilpotent contribution

Let \(H=T\cap D\), a finite scheme, and set \(s=a+b-4\). Classical linkage and Euler characteristic give the full attachment budget

\[
\operatorname{length}H=s\deg T-2p_a(T)+2.             \tag{9}
\]

Indeed \(I_D/L\simeq\omega_T(-s)\), so
\(\chi(\mathcal O_Y)=\chi(\omega_T(-s))+\chi(\mathcal O_D)
=-\chi(\mathcal O_T)-s\deg T+\chi(\mathcal O_D)\).
The scheme union exact sequence gives
\(\chi(\mathcal O_Y)=\chi(\mathcal O_T)+\chi(\mathcal O_D)-\operatorname{length}H\);
equating these proves (9) in every characteristic.

Since \(J\subset I\), there is also an exact sequence

\[
0\longrightarrow I\mathcal O_H\longrightarrow\mathcal O_H
\longrightarrow\mathcal O_{C\cap D}\longrightarrow0.
\]

Define \(\epsilon_{\mathrm{normal}}=\operatorname{length}(I\mathcal O_H)\).
This is the marked normal nilpotent contribution, **not the entire nilradical** of \(H\): the scheme \(C\cap D\) can itself be nonreduced along \(C\). Combining (8)–(9) yields

\[
\boxed{\ \operatorname{length}\mathcal T_T+\deg\operatorname{div}\theta
+\epsilon_{\mathrm{normal}}
=(a+b-4)\deg T-2p_a(T)+2.\ }                          \tag{10}
\]

This is an identity for an actual pair and its full primary/residual schemes, not a universal positive lower bound. If the residual vanishes, all three terms vanish. The filtration by powers of \(I\) on \(\mathcal O_H\) retains further normal attachment layers; it terminates since a pure length-\(m\) thickening \(T\) satisfies \(I^m\mathcal O_T=0\).

[Benguş-Lasnier–Rangachev, Theorem B(1)](https://arxiv.org/html/2504.09362v3)
is precisely the full-scheme genus/discrepancy formula (9). Its Cohen–Macaulay,
generically-CI hypotheses permit nonreduced T; no characteristic restriction
is imposed. Its reduced Jacobian/Milnor formulas are separate and are not
applied to T after removing nilpotents. The proof of (9) above independently
fixes the distinction between full T cap D and marked C cap D.

### Layerwise attachment duality on a non-Gorenstein primary component

**New general synthesis; pending independent review.** Retain the actual
proper CI \(Y\) in a smooth threefold, its full primary component \(T\)
on a smooth integral curve \(C\), and its linked residual \(R\) (called
\(D\) above), with no common reduced component. Put \(H=T\cap R\).
No normality or primitive hypothesis on \(T\) is made. In this
subsection assume the generic algebra of \(T\) is curvilinear of
length \(m\ge2\). The scalar genus/discrepancy identity (9) is
already classical; the following comparison retains all individual
layers and is not a new proof of that invariant alone.

Use Bănică--Forster's saturated normal-power flag \(P_i\) on
\(\mathcal O_T\), with \(P_0=\mathcal O_T,\ P_1=I_C\mathcal O_T,\ P_m=0\).
Let
\[
 W_i=P_i/P_{i+1}=\mathcal L^i(D_i),\quad
 D_0=D_1=0,\quad D_i\ge0 .
\]
These are the actual multiplication divisors of the free first
conormal line \(\mathcal L\); see the
[saturated filtration account](../normal-geometry/curvilinear_genus_and_defects.md#4-saturate-first-the-same-boundary-information-appears-as-divisors).
Let \(K=I_{H/T}\subset\mathcal O_T\). Define an effective divisor
\(H_i\) on \(C\) by the inclusion
\[
 (K\cap P_i)/(K\cap P_{i+1})= W_i(-H_i)\ \subset W_i .
\]
This is a line subsheaf with finite cokernel (the same generic
line). Equivalently its length divisor is the \(i\)-th layer
of the *induced saturated flag* on \(\mathcal O_H\).
In particular
\[
 H_0=C\cap R,\qquad
 \sum_i H_i=\operatorname{div}_{C}(\mathcal O_H).
\]
The latter denotes the cycle of lengths at points of \(C\),
not an assertion \(\mathcal O_H\) is an \(\mathcal O_C\)-module.

**Layerwise formula.** For every \(0\le i<m\),
\[
 \boxed{\quad H_i=H_{m-1-i}
       =H_0+D_i+D_{m-1-i}-D_{m-1}.\quad}                 \tag{LA1}
\]
In particular
\[
 0\le H_i\le H_0,\qquad
 \operatorname{div}_C(\mathcal O_H)\le m(C\cap R).
                                                               \tag{LA2}
\]
The full attachment length is therefore not an independently
free parameter if the reduced attachment and normal multiplication
defects are known. More precisely,
\[
 2\sum_i D_i=m(D_{m-1}-H_0)+\sum_i H_i.                 \tag{LA3}
\]
The left side is twice the divisor of the sum of ordinary normal
layer torsion lengths, by ordinary-to-saturated filtration
comparison (which does not require \(T\) Gorenstein).
When \(R\) is empty this reduces to the earlier Gorenstein
duality and Frobenius formula. When \(T\) itself is Gorenstein,
ordinary saturated duality gives \(H_i=H_0\) for all \(i\);
in particular the full attachment has exactly \(m\) times
the reduced attachment length at every point. This is because
the attachment ideal is invertible on a Gorenstein primary
component linked inside a Gorenstein CI, not a statement
about arbitrary intersections with another curve.

**Proof.** Scheme-theoretic linkage of disjoint full unions of
primary components identifies the image of \(\operatorname{Ann}_{\mathcal O_Y} I_{T/Y}\)
in \(\mathcal O_T\) with \(K\). It is injective since \(Y\)
has no embedded components and the complementary full primary
components have zero intersection of their defining ideals in
\(\mathcal O_Y\). Finite duality in the Gorenstein \(Y\) therefore
gives
\[
 K\simeq\omega_T\otimes\omega_Y^{-1}|_T .
\]
More generally the validity of this identification is the sole
linkage hypothesis; the following local argument only needs
that ideal to be a canonical module. Fix a point, complete,
and lift a uniformizer \(t\) of \(C\). The resulting primary
algebra \(A\) is finite free over the DVR \(V=k[[t]]\) by
purity; \(K\) is likewise finite free, and the preceding
canonical-module identification gives an \(A\)-linear
isomorphism \(K\simeq\operatorname{Hom}_V(A,V)\) after
trivializing the invertible twists. Thus there is a functional
\(\lambda:K\to V\) with perfect pairing
\((a,k)\mapsto\lambda(ak)\).

Over the fraction field of \(V\) the algebra is
\(F[z]/(z^m)\), so the orthogonal of \(P_i\) in \(K\)
is \(K\cap P_{m-i}\). Indeed the pairing is perfect
generically and \(\lambda(ak)=0\) for all \(a\in P_i\)
is equivalent to \(kP_i=0\), since \(P_i\) is an ideal
and the original pairing is perfect. The flags in \(A\)
and in \(K\) are saturated as \(V\)-modules, by their
construction from the generic flag. Consequently restriction
of the \(V\)-dual sequence proves that the induced pairing
of \(W_i\) and \(W_{m-1-i}(-H_{m-1-i})\) is perfect over the
DVR. Write \(d_i,h_i\) for the coefficients at the point.
A lift \(z\) generating the first free layer gives generators
of the \(i\)-th saturated layer with leading term
\(t^{-d_i}z^i\); the corresponding generator for \(K\) has
leading term \(t^{h_i-d_i}z^i\), up to units. In the top
layer, \(\lambda(t^{h_{m-1}-d_{m-1}}z^{m-1})\) is a unit.
Perfectness of each complementary pairing gives
\[
 d_i+d_{m-1-i}=d_{m-1}-h_{m-1}+h_{m-1-i}.
\]
For \(i=m-1\) this gives \(h_{m-1}=h_0\);
interchanging \(i\) gives the symmetry in LA1.
The inequality follows from \(d_i+d_{m-1-i}\le d_{m-1}\)
by actual multiplication of saturated layers. Summing gives LA3.
These local computations are invariant under all choices,
hence are equalities of divisors on \(C\). \(\square\)

The top term gives a global identity independent of any local
choice: the annihilator of the marked ideal in \(K\)
is \(\omega_C\otimes\omega_Y^{-1}|_C\) by transitivity
of finite duality. It is precisely the highest saturated layer
of \(K\), so
\[
 \boxed{\ \mathcal L^{m-1}(D_{m-1}-H_0)
             \simeq\omega_C\otimes\omega_Y^{-1}|_C.\ }   \tag{LA4}
\]
Thus it is the *signed* divisor \(D_{m-1}-H_0\) that
has the sole-support socle class when residual components
are present. Treating the original top defect as effective
in that same class without checking attachment discards
this correction.

For example, in length three LA1 gives \(H_2=H_0\),
\(H_1=H_0-D_2\). Thus \(D_2\le H_0\) as divisors,
and full attachment is exactly \(3H_0-D_2\).
In particular the first nonprimitive defect of a full primary
triple necessitates an actual residual attachment there,
rather than an arbitrary vertical exceptional component.
This does not exclude a primitive triple: it gives no positive
lower bound on \(H_0\) when the defect is zero. For higher
lengths the same bound is on
\(D_{m-1}-D_i-D_{m-1-i}\), not necessarily on
\(D_{m-1}\) itself. LA4 uses the actual two defining
twists and reduces to CI adjunction when \(H_0=0\);
it does not furnish a degree bound on mates.

**Literature boundary.** The saturated filtration and
multiplication inequalities are Bănică--Forster, §3.5,
[*Multiplicity Structures on Space Curves*](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf).
Manolache's [Gorenstein filtration duality
(2023)](https://doi.org/10.59277/RRMPA.2023.141.148)
identifies complementary layers for Gorenstein structures.
The above uses the *canonical ideal* \(K\) in a possibly
non-Gorenstein primary structure, supplied by the ordinary
linkage theorem (also see Manolache, [*Linkage Extensions*](https://arxiv.org/abs/math/0501036)).
Benguş-Lasnier--Rangachev's discrepancy theorem cited
above gives the aggregate length/genus relation, not
the new pointwise comparison in LA1. These standard
duality statements are inputs; the displayed identities
are a direct application to the actual full-primary
attachment, not a claim of priority for a new
duality theorem.

### Triples: the full attachment has only two independent divisors

**Existing geometry first.** The local form of a
quasiprimitive triple, including its non-lci
points, is already in Bănică--Forster,
[*Multiplicity Structures on Space Curves*,
§3](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf).
In coordinates \((t,u,v)\) with \(C=(u,v)\),
a generically curvilinear Cohen--Macaulay
triple has at a point the local ideal
\[
 J_T=(u^2-t^d v,\ uv,\ v^2),\qquad d\ge0,
                                                        \tag{TR1}
\]
after interchanging their two normal variables.
For \(d=0\), eliminate \(v=u^2\); it is
the primitive lci triple \((v-u^2,u^3)\).
For \(d>0\), \(u^2=t^d v\) in the
local ring, whose saturated second layer
has a free generator \(v\). Hence
\(d=\operatorname{ord}_P D_2\).
All this is the *classical local normal form*,
not a new triple classification.

**Conormal-torsion identity (TR2).** The actual
conormal equation module \(J_T/I_CJ_T\)
has a free rank-two part and a torsion
summand of length \(d\). For \(d>0\)
write \(f_1=u^2-t^dv,\ f_2=uv,\ f_3=v^2\).
Its Hilbert--Burch syzygies can be taken
\[
 vf_1-uf_2+t^df_3=0,\qquad vf_2-uf_3=0.
\]
Modulo \((u,v)\), the only relation
is \(t^df_3=0\). Thus
\[
 J_T/I_CJ_T\simeq
 k[[t]]^2\oplus k[[t]]/(t^d).
\]
For \(d=0\), \(J_T\) is lci and
its conormal equation module is free.
Consequently the *effective divisors on \(C\)*
agree:
\[
 \boxed{\ \operatorname{div}
 \operatorname{tors}(I_T/I_CI_T)=D_2.\ }                  \tag{TR2}
\]
Here the displayed equality is valid for
every actual generically curvilinear
CM triple in a smooth threefold, whether
or not it occurs as the full primary of
a Gorenstein CI. The proof is formal
local algebra and works over an arbitrary
algebraically closed coefficient field;
no division by two or three occurs.
The BF normal form and Hilbert--Burch
theorem are inputs, while TR2 records
their application to the specific
torsion module used in (5) above.

**Two-divisor attachment theorem (TR3).**
Now *add* the hypotheses of the full-primary
attachment theorem: \(T\) is the full
marked primary of an actual proper CI
\(Y=V(F,G)=T\cup R\), and the residual
\(R\) has no component \(C\).
Write
\[
 \tau=\operatorname{div}
       \operatorname{tors}(I_T/I_C I_T)=D_2,\qquad
 \eta=\operatorname{div}\det\bar\rho .
\]
Both are effective divisors and are
intrinsic to the actual pair and its
full primary. The attachment equation
module identity (8) gives
\(H_0=C\cap R=\tau+\eta\). The
complementary-layer relation LA1
at \(m=3\) gives
\(H_1=H_0-D_2,\ H_2=H_0\).
Hence without any further choices
\[
 \boxed{\quad
 (H_0,H_1,H_2)
 =(\tau+\eta,\ \eta,\ \tau+\eta),\qquad
 [\operatorname{length}(T\cap R)]
 =2\tau+3\eta .\quad}                                   \tag{TR3}
\]
The bracket denotes the zero-cycle
of local lengths along \(C\), not an
assertion that the full intersection
is itself a Cartier divisor on \(C\).
Its marked normal-nilpotent excess is
\(\epsilon_{\rm normal}=\tau+2\eta\).
The top signed class LA4 reduces to
\[
 \mathcal L^2(-\eta)
  \simeq\omega_C\otimes\omega_Y^{-1}|_C,                \tag{TR4}
\]
since \(D_2-H_0=-\eta\).
This is an especially transparent
description: all three attachment
layers and their canonical class are
controlled by **two effective divisors**,
the non-lci defect of the primary and
the determinant failure of the two
actual equations. Every independently
computed layer or genus formula must
agree with TR3.

The [actual fixed toric \((4,6)\) triple
TS5--TS7](../torus/fixed_carrier_chow_arrangements.md#an-actual-non-lci-curvilinear-triple-the-conormal-torsion-is-visible)
has \(\tau=2[p_0]\) and
\(\eta=5[p_0]+9[p_\infty]\). TR3 predicts
\((7,5,7)\) at \(p_0\) and
\((9,9,9)\) at \(p_\infty\), full
attachment length \(46\), matching
the two independent computations there.
The new point is the **cross-framework
identification** of the BF divisor
\(D_2\) with the torsion of the actual
full-primary equation module and its
consequences for genuine residuals,
not a rediscovery of BF's normal form
or a new classification of triples.

**Boundary of scope.** For generic
multiplicity greater than three
different multiplication divisors
and independent relation syzygies
appear, so neither TR2 nor TR3
is claimed in that form. For generic
embedding dimension two, the BF
rank-one saturated flag is not
available. In a sole-support CI,
\(\eta=\tau=0\) and the triple is
primitive; this does not alone
exclude its existence. No
unconditional positive residual
bound in all degrees follows from
TR3. The relation to actual local
cohomology is LC-A1 at the first
annihilator layer and still requires
first-element coregularity when
interpreted as the *second* defect.
Independent review of the global
attachment extension is pending.

### A classical fourth-order counterexample to extrapolating TR2

The triple identity \(\tau=D_2\)
cannot be extended by replacing the
triple with a quasiprimitive multiple
structure of arbitrary length.
Bănică--Forster, [*Multiplicity
Structures on Space Curves*, original
1986 publication, §3.9, p. 61](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/coxeter86.pdf),
already prove that when \(D_2=D_3=d[P]\),
a quasiprimitive **quadruple** has
a locally complete-intersection ideal
\[
 \boxed{\ I_T=(t^d x-y^2,\ x^2)\ }\qquad(d>0).           \tag{TR5}
\]
The quotient is free of rank four
over \(k[[t]]\), with basis
\(1,y,x,xy\). Its saturated flag is
\[
 P_1=(y,x,xy),\qquad
 P_2=(x,xy),\qquad P_3=(xy),
\]
and its normal multiplication has
\(y^2=t^dx,\ y^3=t^dxy\).
Hence \(D_2=D_3=d[P]\) are both
nonzero. Nevertheless \(I_T\) is
lci, so \(I_T/(I_CI_T)\) is free
of rank two and
\[
 \boxed{\quad \tau=0\ne D_2=D_3.\quad}                 \tag{TR6}
\]
For \(d=1\) this is the smallest
transparent instance. It is a
*local quasiprimitive quadruple*,
not an asserted global pair
supported on the fixed quartic.
The result uses exactly the
already-established BF local
classification and its hypotheses;
the elementary basis computation
is an independent check.

Thus the sharp general finding
from TR2 is that multiplicity three
has a special collapse of independent
defects. At multiplicity four,
the values \(D_2,D_3\) and local
conormal syzygies must be retained
separately; nonzero \(D_2\)
does **not** force a non-lci
primary or torsion of its conormal
equation module. The full
attachment identities LA1--LA6
remain applicable under their
actual-CI hypotheses. No universal
fourth-order conormal-torsion
formula is asserted without checking
both BF cases and the actual
saturated syzygy module.

**Source fidelity.** The original
1986 scan has the factor
\(y(t^dx-y^2)\) in BF's other,
non-lci quadruple case. One
modern re-typeset copy of §3.9
instead prints \(y(t^d-y^2)\),
which cannot define the stated
generic length-four structure.
Any subsequent use of that
other local model must consult
the original rather than copy
the missing-\(x\) transcription.
This typographical observation
is not used in TR5--TR6.

### Triple determinant recovery from an actual auxiliary cut

Combine TR3 with the signed order-one
cutting-surface formula LA6. On
a generically curvilinear full-primary
**triple** in an actual proper CI,
for any proper auxiliary smooth
Cartier surface \(J_0\supset C\)
whose defining equation has generic
normal order one, the identity
simplifies **pointwise**:
\[
 \begin{aligned}
 B_Y-[R\cap J_0]
   &=2\Theta+D_2-H_0\\
   &=2\Theta-\eta.
 \end{aligned}
\]
Thus the *actual equation determinant
divisor* is recovered as
\[
 \boxed{\quad
 \eta=2\Theta+[R\cap J_0]-B_Y.
 \quad}                                                 \tag{TR7}
\]
The left side comes from the
two defining equations on the full
primary; the right side uses the
actual proper auxiliary cut and
its tangency divisor. The equality
holds as effective divisor classes
supported on \(C\) after
subtracting the residual cut on
the auxiliary surface. This is a
direct consequence of the established
canonical duality formulas and
BF's triple normal form; it is
not a new genus or intersection
theorem.

For TS5--TS7 with \(m=3,N=6\),
\(\Theta=p_0+p_\infty\),
\([R\cap Q]=12p_0+12p_\infty\),
and \(B_Y=9p_0+5p_\infty\).
TR7 gives
\[
 \eta=(2+12-9)p_0+(2+12-5)p_\infty
       =5p_0+9p_\infty,
\]
exactly the independent conormal
determinant calculation.
The non-lci torsion is then
\(\tau=D_2=2p_0\), recovering
\(H_0=7p_0+9p_\infty\).

For a locally complete-intersection
quadruple with \(D_2=D_3=d>0\)
the formula is **not** TR7:
LA6 reads
\(B_Y-[R\cap J_0]=3\Theta+D_3-H_0\),
and since its conormal torsion is
zero, \(H_0=\eta\); an additional
\(D_3\) remains. This supplies a
geometric explanation for the
multiplicity-three cancellation
and prevents presenting it as a
general all-order conservation law.
The residual cut \([R\cap J_0]\)
cannot be discarded unless the
residual is absent, so TR7 is not
an automatic detector of residual
degree from \(B_Y\) alone.

### Cutting the residual pair rather than just its primary part

Let \(J_0\) be a smooth auxiliary Cartier divisor
containing \(C\), with no reduced component of \(R\)
contained in \(J_0\). Assume \(T\) is generically
curvilinear and the equation of \(J_0\) has generic
order \(k\), \(1\le k<m\), in its algebra. Write
\(B_Y,B_T\) for the zero-dimensional torsion
length cycles of the actual cuts \(Y\cap J_0,T\cap J_0\).
The unrestricted (CM, not necessarily Gorenstein)
[Cartier-cut determinant CF1](../normal-geometry/curvilinear_genus_and_defects.md#determinant-of-a-cartier-cut)
computes \(B_T\) by multiplication in the saturated flag.
Then the residual pair has the exact local comparison
\[
 \boxed{\ B_Y=B_T+[R\cap J_0]-\sum_{i=m-k}^{m-1}H_i
             =B_T+[R\cap J_0]-\sum_{i=0}^{k-1}H_i.\ }   \tag{LA5}
\]
All cycles are on the auxiliary cut, and those on \(C\)
are embedded into it. The second equality is LA1.
No Gorensteinness of \(R\) or \(T\) is required.

For the proof use the scheme union sequence
\(0\to\mathcal O_Y\to\mathcal O_T\oplus\mathcal O_R
\to\mathcal O_H\to0\), and multiply by the equation
\(j\) of \(J_0\) locally (trivialize its line bundle).
On \(R\) it is regular. The snake lemma gives
\[
 0\to \operatorname{Ann}_Yj\to\operatorname{Ann}_Tj
 \to\operatorname{Ann}_Hj\to\mathcal O_{Y\cap J_0}
 \to\mathcal O_{T\cap J_0}\oplus\mathcal O_{R\cap J_0}
 \to\mathcal O_H/j\mathcal O_H\to0.
\]
The annihilator on \(T\) is \(P_{m-k}\) by purity and
the generic algebra. Its image in \(\mathcal O_H\)
has length cycle \(\sum_{i=m-k}^{m-1}H_i\).
Moreover the two finite modules \(\operatorname{Ann}_Hj\)
and \(\mathcal O_H/j\mathcal O_H\) have equal pointwise
length by rank-nullity. The kernel and cokernel of the
middle comparison are finite, and the induced map
of pure one-dimensional quotients is an isomorphism:
the map \(\mathcal O_{Y\cap J_0}\to\mathcal O_{T\cap J_0}\)
is surjective, with finite kernel, so every element
mapping to punctual torsion is itself punctual torsion.
Taking lengths gives LA5.

For \(k=1\) in particular CF2 and LA1 give
\[
 \boxed{\ B_Y-[R\cap J_0]
  =(m-1)\Theta+D_{m-1}-H_0.\ }                          \tag{LA6}
\]
Here \(\Theta\) is the actual first-normal-line tangency
to the cutting surface. If neither defining equation contains
\(J_0\), their divisorial gcd on \(J_0\) is precisely \(kC\);
after division the finite residual cut accounts for \(B_Y\),
as in CF1. Thus the divided resultant on a suitable ruled
cutting surface has both a genuine residual-curve contribution
and a **subtracted** attachment correction.
It cannot be read as simply the primary socle defect plus
every intersection of the residual with the cutting surface.
The global degree version of LA6 follows already from
adjunction; this pointwise comparison identifies what is
lost at each attachment, and can be used with actual
equation restrictions. The proof works in arbitrary
characteristic. It does not apply to a cut containing
a residual component or to a generic algebra of higher
embedding dimension without replacing the rank-one
filtration argument.

For comparison, the [toric repeated-root primary theorem TS1--TS3](../torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier)
computes every \(D_i,H_i\) in the above rank-one setting
for actual arrangements in the classified fixed-quartic
carrier. Its nonprimitive primary of length three has
\(D_2=2[p_0]\), compatible with \(H_0(p_0)=N+1\).
For the quartic collision the total full attachment grows
from 18 to 24 even though the reduced attachment shrinks
from 18 to 12 and the residual degree from 12 to 8.
These are pointwise normal and attachment calculations
for actual pairs, and a control against replacing the
marked attachment by the full one in capacity bounds.

The [actual-quadric cut calculation TS4](../torus/fixed_carrier_chow_arrangements.md#a-fixed-auxiliary-quadric-detects-the-same-punctual-defect-at-every-collision)
now independently verifies LA6 for the entire
classified fixed-quartic arrangement family.
Its punctual cut divisor is
\(3(N-3)p_0+(N-1)p_\infty\), independent
of the marked multiplicity \(m\); a
direct local computation of \(Q|A\) and
\(G_N|Q\) agrees with the signed-layer
formula. This is a concrete test that
the subtraction of \(H_0\), rather than
addition or replacement by the full
thick attachment, has the right sign.
It is not a universal conservation
law for arbitrary CI degenerations.

The [explicit (4,6) toric triple TS5--TS7](../torus/fixed_carrier_chow_arrangements.md#an-actual-non-lci-curvilinear-triple-the-conormal-torsion-is-visible)
gives a generically curvilinear but
non-lci primary of multiplicity three,
with completed ideal
\((X^2-\tfrac12x^2Z,XZ,Z^2)\).
Its exact Hilbert--Burch relations
yield conormal torsion \(k[[x]]/(x^2)\),
of length two. The actual attachment
lengths are \(7+9=16\), with determinant
part \(5+9=14\), full thick attachment
length 46, and auxiliary quadric cut
torsion lengths 9 and 5.
This verifies on an **actual globally
homogeneous CI** why non-lci torsion
must be retained separately from
the determinant, and why a constant
punctual cut does not encode residual
absorption. Do not infer the equality
\(\tau=D_2\) for arbitrary thick curves.

## 5. A sharp control: the determinant can be a unit at a real attachment

This is a local explanatory example, not a global homogeneous realization on the fixed quartic. It is used to test exactly the proposed omission of \(\mathcal T_T\), not to launch a case classification.

In \(k[[t,x,y]]\), mark \(C=(x,y)\) and take

\[
L=(x^2,xy+ty^2),\qquad
J=(x^2,xy+ty^2,y^3).
\]

The quotient by \(J\) is free over \(k[[t]]\), with basis \(1,x,y,y^2\), so \(J\) is \(C\)-primary and CM. At \(t\ne0\), \(y^3\) belongs to \(L\), since

\[
t^2y^3=yx^2+(-x+ty)(xy+ty^2).
\]

Thus it is the full marked primary component. The residual ideal is

\[
K=(x+ty,t^2)=L:J,\qquad L=J\cap K.
\]

A Hilbert--Burch matrix for \(J\) is

\[
\begin{pmatrix}
y&0\\
-x+ty&-y^2\\
-t^2&x+ty
\end{pmatrix}.
\]

Reducing its relations modulo \(I=(x,y)\) gives

\[
\mathcal E_T\simeq k[[t]]^2\oplus k[[t]]/(t^2).
\]

The actual equations \(x^2,xy+ty^2\) map to the two free basis vectors. Hence \(\bar\rho\) is the identity and \(\theta\) is a unit, but

\[
\mathcal Q_{Y,C}\simeq k[[t]]/(t^2),\qquad C\cap D=2[0].
\]

All attachment length sits in the non-lci torsion term. This disproves a determinant-only residual detector for general full primary components.

The full thick attachment is larger: substituting \(x=-ty\) in \(J+K\) gives
\(\mathcal O_H\simeq k[[t,y]]/(t^2,y^3)\), of length six.
The marked normal ideal \(I\mathcal O_H=(y)\) has length four, while
\(\mathcal O_{C\cap D}=k[[t]]/(t^2)\) has length two.
Thus \(\epsilon_{\mathrm{normal}}=4\), illustrating the two distinct attachment quantities in (10).



## Marked attachment controls genuine residual degree

## 1. Exact statement

Let \(Y=V(F_a,G_b)\) be an actual proper homogeneous intersection
containing \(C\). Let \(T\) be its full \(C\)-primary component and
\(Z\) its linked residual, sharing no component with \(C\). Write

\[
[Y]=m[C]+R,\quad [Z]=R,\quad \delta=\deg R=ab-4m,
\qquad A=\operatorname{length}(C\cap Z).
\]

The residual \(Z\) may be nonreduced, disconnected or non-Gorenstein.
It is a pure locally Cohen–Macaulay curve when nonempty. Then

\[
\boxed{\delta\ge\left\lceil\frac A3\right\rceil.}\tag{1}
\]

If no component of \(R\) lies on the unique containing quadric \(Q\),
then

\[
\boxed{\delta\ge\left\lceil\frac A2\right\rceil.}\tag{2}
\]

Neither bound assumes an integral or normal carrier, nor a reduced
residual. The attachment in these formulas is to **reduced marked**
\(C\), not the generally larger full \(T\cap Z\).

## 2. Direct proof and a module-to-degree bridge

The inherited global generation of \(I_C(3)\) lets us choose a cubic
\(h\) through \(C\) containing none of the finitely many components
of \(Z\). Indeed, at the generic point of any component distinct from
\(C\), global generation gives some section nonzero there; avoid the
finite union of proper linear subspaces. Purity makes \(h\) a
nonzerodivisor on \(O_Z\). Thus \(Z\cap V(h)\) is finite of length
\(3\delta\), by the exact Cartier sequence and the Hilbert polynomial.
Since \(h\in I_C\), there is a surjection

\[
O_Z/(h)\twoheadrightarrow O_Z/I_C O_Z=O_{C\cap Z}.
\]

Therefore \(A\le3\delta\). If \(Z\) has no component on \(Q\),
use its quadratic equation instead of \(h\) and get \(A\le2\delta\).
This proof does not reduce \(Z\) or replace it by its normalization.

The [attachment-module identity](#full-primary-equation-module-and-exact-attachment-divisor)
makes the numerator accessible from the full primary equation module.
Put \(I=I_C\), \(J=I_T\), and \(E_T=J/IJ\). The actual two equation
classes map into \(E_T\). Let

\[
\tau=\operatorname{length}(\operatorname{tors}E_T),\qquad
\eta=\deg\operatorname{div}\theta,
\]

where \(\theta\) is the determinant of their induced map into the
torsion-free rank-two quotient. Because \(T\) is the **full** primary
component, this determinant is generically nonzero. The inherited identity
is \(A=\tau+\eta\). Consequently

\[
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{3}\right\rceil,}
\quad\text{or}\quad
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{2}\right\rceil}
\quad(R\text{ has no component on }Q). \tag{3}
\]

This combines an already reviewed module identity with an elementary
scheme-theoretic Bézout estimate. It is not a new assertion of positivity
of \(\tau+\eta\) for every characteristic-zero pair. At a sole-support
endpoint \(Z\) is empty and both vanish. It also does not let one replace
\(A\) by the full attachment: the extra normal-nilpotent length in
\(T\cap Z\) is absent from (3).

## 3. A sharp actual family and the failure of the full-attachment substitution

On \(Q\cong\mathbf P^1\times\mathbf P^1\), use
\(C\sim(1,3)\). For any integer \(s\ge1\), choose a divisor
\(B\in |O_Q(2s,0)|\) consisting of \(2s\) distinct trisecant ruling
lines. The product of its section and the \(s\)-th power of the
Cartier equation of \(C\) is a section of
\(O_Q(3s,3s)=O_Q(3s)\). It lifts to an actual homogeneous form \(G_{3s}\)
because \(H^1(\mathbf P^3,O(3s-2))=0\). The proper pair \((q,G_{3s})\)
has, as a divisor on the smooth quadric,

\[
Y=sC+B,
\quad T=sC,
\quad R=B,
\quad \delta=2s,
\quad A=C\cdot B=6s.
\]

It attains \(A=3\delta\), proving that coefficient three cannot be
improved for arbitrary proper pairs in (1). This reuses the known smooth-
quadric construction principle; it does not reopen a closed STCI case.

The full attachment has length
\(\operatorname{length}(T\cap Z)=sC\cdot B=6s^2\).
For \(s>1\), substituting that length into \(A\le3\delta\) would be
false. This family therefore gives an actual fixed-quartic control for
both sharpness and the necessary marked/full distinction.

### A direct capacity bound from saturated duality defects

For a generically curvilinear full primary \(T\), LA1 also
gives the following estimate from its individual saturated
multiplication divisors, without computing the entire residual:
\[
 A=\deg H_0\ \ge
 \sum_{P\in C}\ \max_{0\le i<m}
 (D_{m-1,P}-D_{i,P}-D_{m-1-i,P}).
\]
Every term inside the maximum is nonnegative by
multiplicativity. The capacity estimate (1) (or (2)
when the quadric is available) therefore gives an
actual lower bound on residual degree from any
certified failure of complementary-layer duality.
For a primary triple the right side is exactly
\(\deg D_2\). This needs the **full actual primary**
filtration, not the displayed initial equations or an
arbitrary formal thickening. For an actual Gorenstein
primary it is zero and gives no exclusion; the
adjunction class LA4 and the separate equation-module
constraint may then still supply attachment.
The total residue-degree bound retains the original
congruence \(\deg R\equiv ab\bmod4\).
This is a sufficient route from a particular intrinsic
duality defect to positive residual degree, not a proof
that every characteristic-zero primary has such a defect.
Independent review of LA1 is pending.

## 4. How to use the bound without making it circular

The inequalities are useful when geometry supplies an independent lower
bound \(A\ge A_0\), or a bound on \(\tau+\eta\), for a class of possible
primary structures. If one has already explicitly computed the entire
primary ideal and its degree, then \(m\), hence \(\delta\), is already
known; (3) is then a consistency check. It is not a shortcut around a
completed primary decomposition.

Every bound must also respect \(\delta\equiv ab\pmod4\). For example,
an independent estimate \(A\ge13\) gives \(\delta\ge5\); if
\(ab\equiv0\pmod4\), this strengthens to \(\delta\ge8\).

For any curve whose ideal is generated in twist \(d_0\), the same proof
gives \(\deg R\ge\lceil\operatorname{length}(C\cap Z)/d_0\rceil\).
Any independently known hypersurface through \(C\), avoiding all residual
components, gives its own degree in the denominator. The quartic's quadric
and cubics give the two especially simple alternatives above.



## Full attachment: genus, nilpotents, and low residual degree

In this section assume the genuine linked residual Z is nonempty. Set r=deg Z>0, B=length(T cap Z), and N=a+b-4>0. Here T is the full C-primary component, and Z has no C-component. The two pure locally Cohen–Macaulay schemes share no curve component and are linked by Y. The lower bounds containing max{1,...} use precisely this nonempty hypothesis; a sole-support endpoint has r=0 instead.

## 2. The attachment identity on the genuine residual side

The same standard linkage calculation gives

\[
\boxed{B=Nr-2p_a(Z)+2.}\tag{1}
\]

Indeed adjunction gives \(p_a(Y)=1+Nab/2\), and linkage gives

\[
p_a(T)-p_a(Z)=\frac N2(4m-r).
\]

The scheme-union exact sequence gives
\(p_a(Y)=p_a(T)+p_a(Z)+B-1\), proving (1). These formulas hold for
nonreduced locally Cohen–Macaulay schemes, using their dualizing modules;
they are not formulas for the reduced support or normalization.

Since \(p_a(Z)=1-h^0(\mathcal O_Z)+h^1(\mathcal O_Z)\), equation (1)
also reads

\[
B=Nr+2h^0(\mathcal O_Z)-2h^1(\mathcal O_Z).
\tag{2}
\]

Consequently, if a separate argument supplies \(h^0(\mathcal O_Z)\le h\),
then

\[
\boxed{r\ge\max\{1,\lceil(B-2h)/N\rceil\}.}\tag{3}
\]

This is useful when the full-primary attachment module can be computed
before a residual decomposition. It is conditional on that extra
cohomology information; connected nonreduced support does not imply
\(h^0=1\).

The practical input may instead be an independently proved lower bound
\(B\ge B_0\), or attachment data controlled throughout a proposed family
of primary thickenings. One can replace \(B\) by \(B_0\) in the lower
bounds below. A completed explicit extraction of the full primary ideal
already determines its generic multiplicity and hence \(r=ab-4m\);
these inequalities are not claimed to shortcut that completed computation.
They are constraints on proposed primary families, module budgets, or
partially known decompositions.

Two clean cases need no detailed cohomology calculation:

- If \(Z\) is reduced, it has at most \(r\) connected components, and
  \(h^0(\mathcal O_Z)\) is their number. Thus
  \[
  \boxed{r\ge\max\{1,\lceil B/(a+b-2)\rceil\}.}\tag{4}
  \]
- If \(Z\) is reduced and connected, or more generally
  \(H^0(\mathcal O_Z)=k\), then
  \[
  \boxed{r\ge\max\{1,\lceil(B-2)/(a+b-4)\rceil\}.}\tag{5}
  \]

For (4), the equality \(B=(N+2)r\) forces \(r\) disjoint lines: equality
requires \(h^0=r\) and \(h^1=0\), so each connected component has degree
one. This is an equality characterization for any actual pair attaining
it, not a construction of such a pair for arbitrary degrees.

The variable \(B\) cannot silently be replaced by
\(\operatorname{length}(C\cap Z)\). The full attachment can have an
additional normal-nilpotent contribution even when the marked intersection
has been fixed. Likewise (4) cannot be used after merely reducing \(Z\):
that changes its degree and its Euler characteristic.
If a marked lower bound \(\operatorname{length}(C\cap Z)\ge A_0\) is
known, the containment \(C\cap Z\subset T\cap Z\) does give
\(B\ge A_0\). Thus the **weaker inequalities obtained by substituting the
lower bound \(A_0\)** are legitimate under the same reducedness or
cohomology hypotheses. That use of a lower bound does not identify the
two attachment lengths or turn (1) into a marked-intersection identity.

## 3. Why genus alone does not give an unrestricted degree bound

There are locally Cohen–Macaulay double lines of degree two and arbitrarily
negative arithmetic genus. In coordinates \([x:y:z:w]\), take
\(L=V(x,y)\), choose \(e\ge-1\), and a surjection

\[
\mathcal O_L(-1)^2\xrightarrow{(f,g)}\mathcal O_L(e),
\]

where \(f,g\) have degree \(e+1\) and no common zero on \(L\). The
kernel construction gives the ribbon with ideal

\[
I_Z=(x^2,xy,y^2,gx-fy),
\qquad
0\to\mathcal O_L(e)\to\mathcal O_Z\to\mathcal O_L\to0.
\tag{6}
\]

It has

\[
\deg Z=2,\qquad p_a(Z)=-e-1,\qquad
h^0(\mathcal O_Z)=e+2,\qquad h^1(\mathcal O_Z)=0.
\]

Thus the right side of (1), for fixed \(r=2\), can be arbitrarily large
among unrestricted curve candidates. A reduced integral Castelnuovo bound
cannot be applied to these schemes. Even topological connectedness does
not repair the issue: the extra global functions in (6) are nilpotent.

This is standard ribbon geometry, not a new example. The primary text
[Nollet–Schlesinger, *Hilbert Schemes of Degree Four Curves* (2003)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B62E5E7FF38C897359DE99E647E71DFF/S0010437X03100711a.pdf/hilbert-schemes-of-degree-four-curves.pdf)
uses the displayed homogeneous double-line ideals and genus calculation.
[Bayer–Eisenbud, *Ribbons and their canonical embeddings*](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf)
provides the square-zero extension framework. These sources were inspected
on 2026-10-28; no literature novelty is asserted.

This is a limitation of genus-only reasoning for arbitrary candidates.
It does **not** assert that all these ribbons occur as the full residual
of pairs of two fixed degrees containing \(C\). Actual equations impose
additional bounds, which the next section makes explicit in degree two.

## 4. Actual equations sharply constrain a degree-two residual

Assume \(a\le b\). If the genuine residual degree is one, purity makes
\(Z\) a reduced line. Therefore

\[
\boxed{r=1\ \Longrightarrow\ B=N+2.}\tag{7}
\]

If the genuine residual degree is two, its possible structures are a
plane conic (including intersecting lines and a planar double line), two
skew lines, or a nonplanar double line. In the first two cases,

\[
B=2N+2\quad\text{or}\quad B=2N+4.
\tag{8}
\]

For a double line, (6) gives

\[
B=2N+2e+4.
\tag{9}
\]

For clarity, purity excludes hidden exceptional degree-two schemes in
this list. A component of degree two and multiplicity one is an integral
conic; two components of degree one are lines. With sole support a line,
generic length two makes \(I_L^2\) vanish generically in \(\mathcal O_Z\),
and absence of embedded associated points makes it vanish everywhere.
The resulting square-zero ideal is a torsion-free rank-one module on the
smooth line, hence a line bundle. This gives (6), with \(e\ge-1\) forced
by the globally surjective conormal quotient.

There is now an equation-degree restriction absent from the genus-only
control:

\[
\boxed{e+2\le b.}\tag{10}
\]

To prove it, the conormal sequence of (6) gives

\[
I_Z/I_L^2\simeq\mathcal O_L(-e-2)
\ \subset\ I_L/I_L^2=\mathcal O_L(-1)^2.
\]

The first normal symbol of a degree-\(d\) equation containing \(Z\)
therefore lies in \(H^0(\mathcal O_L(d-e-2))\). If \(a,b<e+2\), both
first symbols vanish. At \(\eta_L\), both equations then lie in the square
of the maximal ideal of the regular two-dimensional normal local ring.
Their quotient has length at least three, since it surjects onto the
length-three quotient by that square. This already contradicts length two
for a full double-line component of \(Y\). Hence at least one first
symbol is nonzero, and its degree is at most \(b\), proving (10).

Combining the cases yields the exact small-degree test

\[
\boxed{
r=2\ \Longrightarrow\
B\text{ is even and }2N+2\le B\le2N+2b.
}\tag{11}
\]

Thus a full-primary calculation giving \(B>2N+2\max(a,b)\) rules out
genuine residual degrees one and two even without a reducedness assumption.
If \(B>0\), it also rules out the empty residual, so it forces \(r\ge3\).
The congruence \(r\equiv ab\pmod4\) may then strengthen this degree
conclusion, separately from the attachment argument.

The lower endpoint in (11) is the planar conic case. Intermediate even
values correspond to a double-line parameter \(e\), but (11) is a necessary
test, not an existence theorem for the corresponding complete intersection
or the fixed quartic partner.

There is also a global algebraic filter. A line or planar conic is ACM, so
linkage forces the full primary \(T\) to be ACM. For \(a,b\ge4\), its
minimal ideal resolution is respectively

\[
\begin{aligned}
0&\to S(-(a+b-1))^2
\to S(-a)\oplus S(-b)\oplus S(-(a+b-2))\to I_T\to0,\\
0&\to S(-(a+b-1))\oplus S(-(a+b-2))
\to S(-a)\oplus S(-b)\oplus S(-(a+b-3))\to I_T\to0.
\end{aligned}\tag{12}
\]

These are the standard dual mapping cones for linking a line or a
\((1,2)\) conic. Thus the small residual alternatives can be tested on
actual primary ideals and syzygies, not only on cycle degrees. Two skew
lines instead have Rao module \(k\) in degree zero, so \(T\) has Rao
module \(k\) in degree \(N\). No classification of all such primary
thickenings of the fixed \(C\) is asserted here.

## 5. Extension to a ribbon on any smooth residual support

The proof of (10) is not peculiar to lines. Suppose the genuine residual
\(Z\) is a ribbon of multiplicity two on a smooth integral support
\(A\subset\mathbf P^3\) of degree \(d\) and genus \(g\), with nilpotent
line bundle \(L\) of degree \(\ell\). Then

\[
0\to M\to N^*_{A/\mathbf P^3}\to L\to0,
\qquad \deg M=-4d-2g+2-\ell.
\]

At least one actual equation has a nonzero first symbol, a section of
\(M(a)\) or \(M(b)\), because \(Z\) is the full generic
multiplicity-two component. Its divisor of zeros is effective, so

\[
\ell\le (b-4)d-2g+2,
\qquad p_a(Z)=2g-1-\ell\ge4g-3-(b-4)d.
\]

Since \(r=2d\), equation (1) gives the conditional quantitative bound

\[
\boxed{B\le(a+2b-8)r-8g+8.}\tag{13}
\]

Whenever the coefficient is positive, this bounds \(r\) from below using
the full attachment and the support genus. For a line it recovers (11)'s
upper bound. The hypotheses require an actual ribbon on smooth support;
one cannot apply (13) to an arbitrary nonreduced residual with several
layers, singular support, or punctual conormal defects.



## A common capacity lemma and its exact limits

The marked-attachment proof has the following useful scope independent of
this quartic. If \(C\subset\mathbf P^3\) has \(I_C(d_0)\) globally
generated, and \(Z\) is a pure residual curve with no component on \(C\),
then \(\ell(C\cap Z)\le d_0\deg Z\). The proof selects a section avoiding
all associated curve components, uses its Cartier sequence on \(Z\), and
surjects its finite zero scheme onto \(C\cap Z\). It therefore works with
nonreduced residuals. An individual hypersurface through \(C\) avoiding all
residual components improves \(d_0\) to its degree. Normalization is neither
needed nor harmless for this finite-scheme assertion.

For a smooth degree-\(c\) curve on an integral carrier of degree \(a\),
a singleton divisorial inverse \(\Gamma\) with residue degree \(f\), ideal
valuation \(e\), and numerical square \(\sigma\), [the normalization proof](../carriers/normalization_residual_capacity.md)
gives
\[
\deg R\ge\frac{be(c^2f^2-a\sigma)}{d_0cf-e\sigma}
\]
when \(d_0a>cef\). Indeed \(d_0H-Z\) is nef,
\(H\cdot\Gamma^{\rm num}=cf\), and Hodge index makes the displayed
denominator positive. This separates the reusable lemma from the numbers
\((c,d_0)=(4,3)\). If the denominator vanishes retain the undivided nef
inequality. A zero Hodge gap alone leaves the endpoint open. In the
generically regular singleton case, however, the [exact almost-Cartier
criterion](../carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) closes fixed-carrier existence in some
degree if the actual downstairs index is finite, with minimum degree
\(cR_X/a\). The more general upstairs-only or thick setting still needs
actual section descent.

There are three different mechanisms here: a finite-scheme quotient bounds
marked attachment by degree; surface positivity bounds the valuation vector
of an actual mate; liaison expresses full attachment through Euler
characteristics. No implication identifies their defect divisors. The ribbon
control shows why connectedness alone does not bound full attachment.
The prescribed A-type family shows why a large local Cartier index alone
neither constructs sole support nor supplies the needed global divisor
relation. In particular its residual cancels the local class and survives
with explicitly different marked and full attachment lengths.

### Local index forces residual attachment

Let \(X=V(F_a)\) be integral and regular at the generic point of the
smooth marked curve \(C\), and let \(G_b\) define an actual proper
intersection of cycle \(m[C]+R\), \(m>0\), with genuine residual
scheme \(Z\) (the pure residual after removing the full C-primary
component). Write \(r_P\) for the order of \([C]_P\) in the local
almost-Cartier group of \(X\), allowing infinite order. Define
\[
 S_m=\{P\in C:r_P\nmid m\},
\]
where infinite order never divides a positive integer. Off the finite
on-curve singular set the index is one. If \(P\notin\operatorname{Supp}R\),
the actual effective Cartier divisor cut by \(G\) has local cycle
\(mC\); since the generic point is regular and the surface is S2, it
represents precisely the almost-Cartier class \(m[C]\). Hence \(r_P\mid m\).
In particular
\[
 S_m\subset C\cap\operatorname{Supp}Z,\qquad
 \#S_m\le\ell(C\cap Z)\le d_0\deg R
\]
whenever \(I_C(d_0)\) is globally generated, by the marked-attachment
capacity above. This connects local divisor-class failure to positive
residual degree even at Hodge equality. For the fixed quartic use
\(d_0=3\) and also the congruence \(\deg R=ab-4m\). The assertion does
not bound residual *multiplicity* at a point or give a converse. If the
residual divisor itself has regular marked generic points, its local
almost-Cartier class cancels \(m[C]\); in general only the support
necessity is asserted. Combine independent lower bounds by their maximum,
not by addition.

The local argument is a direct application of the almost-Cartier
divisor criterion of Hartshorne–Polini (Proposition 7.1) and the
existing marked-attachment inequality, not a new general theorem of
intersection theory. It uses actual local classes downstairs, not
normalization indices. Independent review of this bridge is pending.

## Literature and verification boundary

The marked-attachment and full-discrepancy proofs above are independent of finite sampling. Standard local canonical-module duality is used with its precise length argument, rather than replacing the residual dualizing module by a structure sheaf. The normal-pullback literature and Hodge argument belong to [normalization capacity](../carriers/normalization_residual_capacity.md); fixed-twist formal extension belongs to [formal visibility](formal_residual_visibility.md). No inherited computation was rerun here.

## Characteristic reach and limitation

The full-primary module, Matlis length comparison, marked-attachment bounds,
and ribbon equation-symbol tests are characteristic-free over an algebraically
closed field. They neither require nor prove positivity of attachment. In
particular at the [quartic-carrier supported pairs in every positive
characteristic](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier),
the genuine residual and all attachment terms vanish. Reducedness assumptions
in the genus bounds remain necessary in every characteristic.


## Compatible families and the exact specialization hypothesis

[Benguş-Lasnier–Gaffney–Rangachev, Theorem 3.1](https://arxiv.org/html/2310.16558v4) applies to a flat embedded complex-analytic curve family X over a smooth base, contained in a flat Gorenstein curve family Y, with no embedded point at the origin and with X a union of full induced components in every fiber. It proves fiberwise residual specialization and flat finite attachment, hence locally constant attachment length. Its ambient reduced-equisingularity discussion does not restrict that full-component flatness theorem to reduced X. The primary theorem and its full-primary-decomposition proof were freshly checked here.

This does not authorize arbitrary full-primary extraction in a changing CI family: if multiplicity along C increases, the degree of the full primary component increases and it cannot be a projective flat family with fixed Hilbert polynomial. A flat lower witness can instead cease to be a full component at the special fiber, failing the theorem's component hypothesis. The once-link family in [reverse liaison](residual_liaison.md) is a different flat object. Neither a reduced-support Milnor invariant nor the constant full-attachment conclusion may be substituted after these hypotheses fail.

## Exact finite arithmetic filter for small movement divisors

For each integer `epsilon` from 1 through 8, the historical arithmetic enumeration considers integer tuples `(r,s,a,b)` satisfying
\[
r\ge2,\quad s>r,\quad 3r\le a\le b,\quad ab=4rs,\quad
r\mid\epsilon s,\quad
4r(a+b)=7r(r+s)-\epsilon(s-r).
\]
It uses the proved cutoff `5r <= 3 epsilon (2 epsilon+1)` for the small-order regime, and the forced tail `s=3r` beyond that cutoff. For small `r`, write `c=7r-epsilon`, `N=4r^2(15r^2+epsilon^2)` and enumerate **signed** divisor pairs `uv=N`; candidate degrees are `a=(u+16r^2)/c`, `b=(v+16r^2)/c`, retained only when integral and satisfying all original equations. For the large-order tail, odd epsilon gives no integral solutions; for even `epsilon=2h`, signed divisor pairs of `48h^2` yield the remaining finite candidates after integrality and original-equation checks. This is a complete **necessary integer enumeration only for epsilon=1,...,8**. It does not test Picard descent, ambient equation lifting, or geometric existence.
