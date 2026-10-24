# Delta, transverse specialization, and normal flatness

Date: 2026-10-24. Status: **proved local algebra with independent agent reconstruction; provisional research evidence, not canonical promotion**.

This develops a distinction needed in the broader marked-embedding problem: vanishing of the ideal-filtration defect is different from compatibility of the normal cone with a transverse slice. No hypothesis that the reduced support of the intersection equals the marked curve is imposed.

## 1. Scope, retained data, and dependencies

Locally let the smooth marked curve have ideal `I=(x,y)` in a smooth threefold. Choose a lift `t` of a parameter on the curve and a local coefficient algebra `B=k[[t]]`; in formal coordinates `R=B[[x,y]]`. Put
\[
J=(f,g)\subset I,\quad M=R/J,\quad K=IM,\quad
S=\operatorname{gr}_I R=B[X,Y],\quad
H=\operatorname{in}_I J,\quad T=\operatorname{in}_I(IJ),
\]
\[
A=\operatorname{gr}_K M=S/H,\quad
\mathcal D=J/IJ,\quad G=\operatorname{gr}_F\mathcal D=H/T,
\quad Q=H/S_+H,\quad\Delta=T/S_+H.
\]
The exact comparison `0 -> Delta -> Q -> G -> 0` and the smooth-carrier vanishing statement are retained reviewed premises from the [original investigation](2026-10-23-ideal-filtrations-independent-investigation.md). Their authority remains provisional; this note does not promote them. The [continuation](2026-10-24-delta-singular-locus-continuation.md), sections 5 and 7, supplies the inherited punctual family and supported quadruple used below. Their previously reviewed computations are not rerun here.

The parameter lift is additional data for an actual transverse slice. The cone `Spec_C A` is intrinsic to `C subset Z`; the transverse slice `M/tM` need not be independent of that lift. All assertions comparing with the slice use the specified `B`-algebra structure.

The carrier ideals `(f),(g)`, the quotient `R/J`, the source lines in `J/IJ`, and all maps of the nine-embedding diagram are retained. None is reconstructed from `Delta`. The construction below applies functorially to every compatible ideal-power filtration in that diagram; one uses the actual ambient quotient and its induced ideal for each arrow.

## 2. An exact measure of failure of normal-cone specialization

The next proposition needs neither a complete-intersection assumption nor a support assumption.

**Proposition 1.** Let `B` be a DVR with uniformizer `t` and residue field `k`, let `M` be a noetherian `B`-algebra, and let `K` be an ideal. Set
\[
N_n=M/K^n,\quad A_n=K^n/K^{n+1},\quad
U_n=\operatorname{Tor}_1^B(N_n,k),\quad \bar M=M/tM.
\]
Let `bar K` be the image of `K` in `bar M`. There is a natural exact sequence
\[
U_{n+1}\longrightarrow U_n\longrightarrow
A_n\otimes_B k\xrightarrow{\gamma_n}
\operatorname{gr}_{\bar K}^n\bar M\longrightarrow0.
\tag{1}
\]
Consequently the kernel of `gamma_n` is canonically
\[
E_n=\operatorname{coker}(U_{n+1}\longrightarrow U_n).
\tag{2}
\]
The kernels together form the graded ideal of the closed immersion from the actual slice cone into the fibre of the relative cone.

**Proof.** Tensor the short exact sequence
\[
0\longrightarrow A_n\longrightarrow N_{n+1}
\longrightarrow N_n\longrightarrow0
\]
with `k`. The image of `A_n tensor k` in `N_{n+1} tensor k` is
\[
\frac{K^n+tM}{K^{n+1}+tM}
=\operatorname{gr}_{\bar K}^n\bar M.
\]
The Tor exact sequence gives (1). The maps are the ordinary multiplication-compatible maps of associated graded algebras, so their kernels form a graded ideal. All constructions are natural for compatible maps of filtered algebras. This proves (2) and the diagram compatibility.

If multiplication by `t` on `M` is injective, the same kernel has the concrete form
\[
E_n=
\frac{(K^n\cap tM)+K^{n+1}}
 {tK^n+K^{n+1}}.
\tag{3}
\]
Under `U_n=(K^n:t)/K^n`, the connecting homomorphism sends the class of `m`, with `tm in K^n`, to the class of `tm` in `A_n tensor k`. Thus `E_n` records torsion in a neighborhood that cannot be lifted to the next neighborhood. It is not simply the torsion of `A_n`.

## 3. All degrees detect normal flatness

**Proposition 2.** In Proposition 1 assume that `t` is a nonzerodivisor on `M` and `M/K=B`. The following are equivalent:

1. `gamma_n` is an isomorphism for every `n`.
2. Every `M/K^n` is `B`-flat.
3. Every `A_n` is `B`-flat.
4. Every power `K^n` is saturated with respect to `t`: `(K^n:t)=K^n`.

Condition 3 says that the normal cone is flat over the marked curve. This is the classical normal-flatness condition, not a novelty claim. The exact torsion diagnostic (1) is the useful interface with the retained neighborhood tower.

**Proof.** Conditions 2 and 4 are equivalent because a module over a DVR is flat exactly when it is torsion free. Conditions 2 and 3 are equivalent by successive extensions, starting from `M/K=B`, and by the fact that `A_n` is a submodule of `M/K^{n+1}`. Condition 2 implies 1 directly from (1).

For the converse, (1) makes every map `U_{n+1}->U_n` surjective. Artin--Rees applied to `tM subset M` gives a constant `c` such that
\[
tM\cap K^{n+c}\subset tK^n.
\]
The map `U_{n+c}->U_n` is zero: a representative `m` satisfies `tm in K^{n+c}`, hence `tm in tK^n`, so cancellation of `t` gives `m in K^n`. This same map is surjective as a composite of adjacent transition maps. Therefore `U_n=0` for every `n`, proving 2. Completeness is not needed for this argument.

The quantifier over all degrees is essential. In the inherited punctual family of continuation section 5, `A_1=(B/t^r)^2`, yet its degree-one slice comparison is an isomorphism `k^2 -> k^2`.

The standard conormal-algebra construction and functorial maps are recorded in [Stacks, normal cones](https://stacks.math.columbia.edu/tag/062Z). Normal flatness and the relation between normal cones and tangent cones of fibres are classical themes of [Lejeune-Jalabert--Teissier, *Normal cones and sheaves of relative jets*, 1974](https://www.numdam.org/item/CM_1974__28_3_305_0.pdf). The proof above is direct and does not use their more general theorems as a dependency.

## 4. A sufficient criterion for Delta to commute with the slice

Return to the smooth marked curve and the two-generator regular-sequence ideal of section 1. The two normal algebras involved are
\[
A=S/H=\operatorname{gr}_I(R/J),\qquad
A'=S/T=\operatorname{gr}_I(R/IJ).
\tag{4}
\]
The second is essential: the defect compares `J` with `IJ`, so considering only the normal cone of `Z` omits half the comparison.

**Proposition 3.** Assume `R/J` is `B`-flat. If both `A` and `G=gr_F(J/IJ)` are `B`-flat in every degree, then the full initial ideals `H,T`, and the modules `Q,G,Delta`, commute with the specified slice. In particular
\[
\Delta\otimes_Bk\simeq\Delta_{\mathrm{actual\ slice}}.
\tag{5}
\]
Equivalently, the sufficient hypothesis is normal flatness of both algebras in (4).

**Proof.** The module `D=J/IJ` is free of rank two over `B` because `J` is a regular-sequence ideal contained in `I`. The sequence
\[
0\longrightarrow D\longrightarrow R/IJ
\longrightarrow R/J\longrightarrow0
\]
therefore makes `R/IJ` flat over `B`. Degreewise there is another exact sequence
\[
0\longrightarrow G_n\longrightarrow A'_n\longrightarrow A_n\longrightarrow0.
\tag{6}
\]
Thus flatness of `A,G` implies flatness of `A'`; conversely flatness of `A,A'` implies flatness of `G`, which is a submodule of the flat module `A'` over a DVR.

The induced filtration on `D subset R/IJ` is exactly `F^nD=D cap I^n(R/IJ)`, and the quotient map to `R/J` is strict. This verifies (6), including its left exactness. Also `t`-regularity on `R/J` gives `J cap tR=tJ`, hence `D tensor k=bar J/(bar I bar J)`. Since `(f,g,t)` is a regular sequence in the regular local ring, permutation shows that the sliced pair `(bar f,bar g)` is still a regular sequence. Thus the object on the right of (5) is the same complete-intersection comparison for the actual slice.

Proposition 2 applied to `R/J` and `R/IJ` now shows that their normal algebras commute with the slice. Since the ambient `S_n` and the quotient algebras `A_n,A'_n` are flat, the kernels `H_n,T_n` commute with the slice as well. The initial ideal for the sliced `IJ` is the full initial ideal of `bar I bar J`, because ordinary products commute with passage to the quotient. Finally tensoring the cokernel descriptions
\[
Q=H/S_+H,\quad G=H/T,\quad\Delta=T/S_+H
\]
is right exact, and the images of the multiplication maps become exactly `bar S_+ bar H`. This gives all asserted identifications, including (5).

These are sufficient conditions for `Delta`, not necessary ones. The supported example below has `Delta=0` in both relative and sliced settings, although its first normal algebra is not flat.

## 5. Two sharp distinctions

### 5.1 Zero Delta does not imply compatibility of normal cones

Use the inherited supported quadruple
\[
J=(x^2,y^2+tx),\quad I=(x,y),\quad
H=(tX,X^2,XY^2,Y^4).
\]
The continuation proves `Delta=0`. Nevertheless
\[
A\otimes_B k=k[X,Y]/(X^2,XY^2,Y^4),
\qquad
\operatorname{gr}_{\bar K}(M/tM)=k[X,Y]/(X^2,Y^2).
\]
The specialization kills `Y^2` in degree two and `Y^3` in degree three. Hence `E_2=E_3=k`, with all other `E_n=0`. The actual intersection is finite flat over the curve and supported on it; even here, absence of ideal-filtration cancellation does not establish normal flatness. The two measurements answer different questions.

### 5.2 Flatness of the actual algebra is a genuine hypothesis

In `R=k[[t,x,y]]`, take
\[
I=(x,y),\qquad f=x,\qquad g=ty+x^2,
\qquad J=(x,ty).
\]
The carrier polynomials `x` and `ty+x^2` are distinct and integral in `k[t,x,y]`: the latter is primitive and linear in `t`, with coprime coefficients `y,x^2`. They form a regular sequence. The central first conormal matrix, in the source frames `(e_f,e_g)` and target frames `(X,Y)`, is
\[
\phi=\begin{pmatrix}1&0\\0&t\end{pmatrix}.
\]
The actual quotient and its normal algebra are
\[
M=B[[y]]/(ty),\qquad A=B[X,Y]/(X,tY).
\]
The ideal `J` is homogeneous for the normal grading, so its full initial ideal is exactly `(X,tY)`. Also
\[
\operatorname{in}_I(IJ)=(X^2,XY,tY^2)=S_+H,
\]
and `Delta=0`. Yet `A_n=B/(t)` for every `n>=1`, so the cone is not flat over `B`. Every slice comparison is an isomorphism: both graded algebras are `k[Y]`. Multiplication by `t` on `M` is not injective. This explicitly rules out dropping that hypothesis in Proposition 2, even with integral carriers and a smooth marked curve.

This example is used only to identify the necessary flatness hypothesis. Its additional support is permitted by the investigation's scope and is not a separate classification objective.

## 6. In this codimension-two setting, normal flatness of A already suffices

The additional condition on `G` in Proposition 3 can be removed for the actual two-generator complete intersection along the smooth marked curve. The following lemma identifies why the rank-two equation module is unusually rigid.

**Lemma 4 (the two lowest initial-equation degrees).** Let `(V,m,L)` be an equicharacteristic regular local ring of dimension two, and let `J_0 subset m` be a two-generator regular-sequence ideal. Let `H_0=in_m J_0` in `L[X,Y]`. The two weights `a<=b` of the filtered vector space `D_0=J_0/mJ_0` are exactly the two lowest degrees, counted with multiplicity, of a minimal homogeneous generating set of `H_0`. Both weights are determined by the Hilbert function of `L[X,Y]/H_0`.

**Proof.** The finite filtration on `D_0` admits an adapted basis. Choose lifts `f,g` of its two basis classes, of orders `a<=b`; Nakayama makes them generators of `J_0`. Every element of `J_0` has order at least `a`, and the initials in degree `a` have dimension one or two. If `a=b`, they are independent: a constant leading relation would produce a nonzero class in `F^{a+1}D_0`, contrary to adaptation.

Suppose `a<b`. For any `n<b`, an expression `c f+d g` with order `n` has initial a multiple of `in f`, since `d g` has order at least `b`. At degree `b`, the initial of `g` is not a multiple of `in f`. If it were `u in f` for a homogeneous polynomial `u` of degree `b-a>0`, lifting `u` and replacing `g` by `g-u f` would raise the order of the same nonzero class of `D_0` beyond `b`, again contradicting adaptation. Thus the first two minimal-generator degrees of `H_0` are `a,b`, with no intervening minimal equation. All other minimal equations have larger degree.

For the Hilbert-function assertion, `a` is the first degree with `H_{0,a}!=0`. If `dim_L H_{0,a}=2`, then `b=a`. Otherwise, multiplication by the single nonzero degree-`a` initial equation is injective in the polynomial ring, and gives `dim_L H_{0,n}=n-a+1` for `a<=n<b`. Hence `b` is the first degree with
\[
\dim_L H_{0,b}>b-a+1.
\]
These dimensions are obtained by subtracting the quotient Hilbert function from `dim L[X,Y]_n=n+1`. This proves the lemma.

**Proposition 5.** In the formal smooth-curve setting of section 1, if `A=gr_I(R/J)` is flat over `B` in every degree, then `G=gr_F(J/IJ)` is flat over `B` in every degree. Consequently normal flatness of `C_{C/Z}` alone suffices for all the base-change conclusions of Proposition 3.

**Proof.** First `t` is a nonzerodivisor on `M=R/J`. Indeed the `K`-adic filtration is separated by Krull intersection. A nonzero element killed by `t` would have a nonzero initial class in some `A_n`, also killed by `t`, contradicting flatness. Thus `M` is `B`-flat. The exact sequences `0 -> A_n -> M/K^{n+1} -> M/K^n -> 0`, starting with `M/K=B`, show that every `M/K^n` is `B`-flat.

It follows that reduction modulo `t` is strict on the filtered ideal `J`:
\[
J\cap I^n\longrightarrow \bar J\cap\bar I^n
\quad\text{is surjective for every }n.
\tag{7}
\]
To see this directly, lift an element on the right to `h in J`. Since it lies in `bar I^n`, write `h=i+t r` with `i in I^n`. In `M`, `t[r]` lies in `K^n`. Flatness of `M/K^n` makes `K^n` saturated, so `[r] in K^n`; write `r=i'+j'` with `i' in I^n,j' in J`. Then `h-tj'` belongs to `J cap I^n` and has the required reduction. Since `D tensor k=bar J/(bar I bar J)`, (7) gives
\[
\operatorname{image}(F^nD\longrightarrow D\otimes_Bk)
=F^n\bar D.
\tag{8}
\]

Each `A_n` is a finite free `B`-module, so the generic and special transverse initial algebras have the same Hilbert function. Flat specialization identifies the latter with the actual sliced initial algebra. Both actual transverse ideals are two-generator complete intersections: the generic one follows by flat localization/completion at the generic point of `C`; the special one follows from `t`-regularity on `R/J`. Lemma 4 therefore gives the same two filtered equation-module weights in the generic and special fibres. In particular
\[
\operatorname{rank}_B F^nD
=\dim_k F^n\bar D\qquad\text{for every }n.
\tag{9}
\]

Now `F^nD` is a finite free submodule of `D=B^2`. Its image modulo `t` has, by (8)--(9), the same dimension as its rank. Smith normal form therefore has only unit invariant factors for the inclusion `F^nD subset D`; the submodule is saturated and a direct summand. Every quotient `F^nD/F^{n+1}D` is consequently torsion free over `B`, hence flat. This is precisely the assertion about `G`. Proposition 3 supplies the remaining base-change identifications.

**Geometric limitation.** Normal flatness is a strong conditional locus in the broader investigation. Since `Z` is a pure one-dimensional complete intersection and `C` is a component, the generic transverse algebra is artinian. Thus `A_n` has generic rank zero for large `n`. Flatness makes those finite modules zero; hence `K^N=K^{N+1}` for some `N`, and Nakayama gives `K^N=0`. Therefore normal flatness itself forces the local reduced support to be `C`. This is a conclusion under the additional flatness hypothesis, not an imposed support assumption. Points where further components meet `C` remain covered by Proposition 1, rather than by this normal-flat specialization corollary.

## 7. Consequences and next questions

The useful invariants now separate three geometric issues while retaining their maps:

- `Delta` measures minimal normal equations lost on passage to the filtered equation module.
- `E_n` measures failure of the relative normal cone to agree with the cone of the specified actual transverse slice.
- The tower `M/K^n`, and the corresponding tower for `R/IJ`, records the saturation/flatness information required to compare them.

Proposition 5 settles the focused question whether normal flatness of `C_{C/Z}` alone forces the required flatness of `G` for the two-generator complete intersection: it does. It does not prove that `Q` or `Delta` are flat, or that they vanish. A remaining useful question is whether they can have punctual torsion even on this normal-flat locus; the flat quotient `G` would then force all torsion of `Q` into `Delta`. For points outside that locus, a promising invariant is the joint profile of the two specialization kernels for `R/J` and `R/IJ`; it should explain precisely how the defect changes when one normal algebra specializes strictly and the other does not.

No statement here identifies the filtered scheme from the cone or `Delta`, and no unrestricted STCI consequence is claimed.

## 8. Independent review and evidence boundary

The subagent `audit_base_change` independently reconstructed (1), the Artin--Rees converse in Proposition 2, the all-degrees qualification, and the supported-quadruple distinction. In a second focused review it independently checked Proposition 3, the strict filtration giving (6), sliced complete-intersection and equation-module compatibility, the absence of any flatness requirement on `Q` or `Delta`, and the explicit nonflat-algebra example. The proposing agent separately derived (1)--(3), Proposition 3, and that example, and incorporated the review's explicit slice-compatibility argument above. No discrepancy remains within the stated scope. These are independent agent reconstructions, not human referee acceptance or canonical promotion. No finite sampling or fresh replay of inherited scripts is used as a substitute for these local proofs. No canonical result or question record is modified.

In a third focused review, `audit_base_change` independently reconstructed Lemma 4 and Proposition 5. It checked the `a=b` case, exclusion of another minimal equation in degree `b`, the Hilbert-function formula for the second weight, separatedness and `t`-regularity, strict lifting in (7), generic localization followed by completion (rather than confusing `R[1/t]` with a transverse power-series ring), the rank comparison, Smith normal form, and the deduced nilpotence of `K`. It found no hidden sole-support premise or additional characteristic restriction within the equicharacteristic setting. These claims therefore have explicit proofs and independent agent reconstruction, while remaining provisional research evidence.
