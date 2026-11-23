# Layerwise attachment duality, triples, and actual auxiliary cuts

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed LA1–LA6 and TR1–TR7, including canonical-ideal duality, triple conormal torsion, the quadruple boundary and auxiliary cuts. Inherited inputs are classical linkage/canonical-module duality and the stated Bănică–Forster local forms.

This account owns LA1--LA6 and TR1--TR7: the saturated attachment layers,
the triple conormal-torsion specialization and its fourth-order boundary,
and the comparison with an actual auxiliary cut. Its review qualifications
are retained at the individual statements below.

The [full-primary attachment account](residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor)
fixes the shared setup: an actual proper complete intersection \(Y\), its
full \(C\)-primary component \(T\), and the linked residual \(D\) with no
\(C\)-component. Here that residual is denoted \(R\). The same account owns
the equation module \(I_T/(I_CI_T)\), its actual two-equation map \(\rho\),
the [torsion-corrected length identity (5)](residual_capacity_and_constructions.md#3-torsion-correction-to-the-determinant),
the [marked attachment divisor identity (8)](residual_capacity_and_constructions.md#4-identification-with-the-actual-attachment-divisor),
and the [full attachment genus identity (9)](residual_capacity_and_constructions.md#full-thick-attachment-and-the-marked-normal-nilpotent-contribution).
The labels (5), (8), and (9) below refer to those identities.

### Layerwise attachment duality on a non-Gorenstein primary component

**New general synthesis; covered by the scoped correctness review above.** Retain the actual
proper CI \(Y\) in a smooth threefold, its full primary component \(T\)
on a smooth integral curve \(C\), and its linked residual \(R\) (called
\(D\) in the linked attachment account), with no common reduced component. Put \(H=T\cap R\).
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
in the linked full attachment account gives the aggregate length/genus relation, not
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
torsion module used in the linked identity (5).

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
The global attachment extension is included in the scoped correctness review above.

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

