# Intrinsic local algebra and characteristic-zero quartic geometry

Full mathematical investigations retained by subject. Proposals, independent reviews, limitations and rejected mathematical approaches retain their original epistemic status. This compilation is not a new proof audit.


---

## 2026-10-23-intrinsic-coefficient-valuations.md

# Coefficient valuations, intrinsic blowup flags, and the mu4 test

Date: 2026-10-23. Status: **provisional research contribution; local constructions independently reviewed; not promoted**. This note supplies a secondary local framework for the intrinsic `(4,4)` investigation. It proves no characteristic-zero nonexistence theorem and replaces no global quartic-realizability argument.

## Scope and premises

The curve is the fixed smooth quartic

\[
 C=[s^4:s^3t:st^3:t^4]\subset X=\mathbf P^3_k,
 \qquad K=k(C)=k(z),
\]

with `k` algebraically closed, initially of characteristic zero. The characteristic-two comparisons are identified individually. All valuations considered here are trivial on `k`. A chosen generic formal-coordinate identification is

\[
\widehat{\mathcal O}_{X,\eta_C}\simeq K[[U,V]].
\]

The identification, including its coefficient-field embedding, is a choice. The normal ideal and the blowup of `X` along `C` are intrinsic.

The navigation protocol is [INDEX](../INDEX.md); the contribution requirements are [CONTRIBUTING_AGENT](../CONTRIBUTING_AGENT.md). The accepted premise [STCI-R-0021](../results/quartic_mu4_degeneration.md) concerns only the prescribed pair

\[
 F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]

Its global support statements are used as premises. The explicit weighted calculations below are new checks of local expressions, not re-execution of an inherited proof. The earlier [higher-initial note](2026-10-21-higher-initial-ideals-valuations.md) correctly called for a suitable completion; this note makes the domain restriction precise and supplies an intrinsic normal-first alternative.

## 1. Which coefficient valuations occur?

Every nontrivial valuation of `k(z)` trivial on algebraically closed `k` is equivalent to the order at a unique point of `P1`. Here is a direct proof, valid in any characteristic. If `w(z)>0`, every `z-a`, `a != 0`, has value zero, so factoring polynomials into linear factors shows that `w` is `ord_0` times `w(z)`. If `w(z)<0`, every `z-a` has value `w(z)`, giving the point at infinity. If `w(z)=0`, nontriviality implies that some `z-a` has nonzero value, because otherwise every polynomial and rational function would have value zero. Such a value must be positive and can occur for only one `a`: differences between distinct `z-a` are nonzero constants. This gives `ord_a`. The value group on `K` itself is cyclic; normalize it to `Z`.

Fix `p` and `w=ord_p`. Prolongations to an algebraic extension are choices of places over `p`. At finite separable level they are the localizations at primes over `p` in the normalization of the coefficient curve. In a finite normal extension the field automorphisms permute these places transitively. Passing through finite extensions organizes prolongations to a fixed algebraic closure as compatible systems of places. A purely inseparable extension has a unique prolongation. These extension facts, the finite-index bound for value groups, and the finite residue-extension bound are standard valuation theory; see [Stacks, extensions of valuation rings](https://stacks.math.columbia.edu/tag/0ASF) and [extensions of DVRs](https://stacks.math.columbia.edu/tag/0EXQ).

For any normalized prolongation `wbar` to `Kbar`, its value group is `Q` and its residue field is `k`. Indeed every algebraic element lies in a finite extension, where its value is rational and its residue is algebraic over `k`. Conversely, adjoining an `n`th root of a parameter gives value `1/n` for every positive `n`, including inseparable roots in positive characteristic. Algebraic closedness of `k` identifies every algebraic residue extension with `k`.

The following distinctions matter.

- Different prolongations can assign different values to a specified algebraic coefficient. For example, over `k(z)` in characteristic zero, the two places over `z=0` in `a^2=1+z` have `a` specializing to `1` and `-1`; accordingly `a-1` has value `1` at the first place and `0` at the second.
- In characteristic zero, a normal direction defined over `K(z^{1/n})` may have fractional coefficient order. This records ramification of its field of definition. One must retain the conjugate directions and their descent data before drawing a statement over `K`.
- A henselization chosen inside a prolongation fixes a local branch and makes algebraic lifting convenient; it does not make the initial choice of prolongation canonical. Completion is needed only when actually taking infinite coefficient-adic limits. Neither `Kbar` nor an arbitrary algebraic extension should be called complete.
- The mu4 example needs no extension of `K` in either characteristic: the characteristic-zero fourth roots of unity already belong to `k`; the characteristic-two nilpotent transverse direction is not an algebraic field extension of `K`.

## 2. A correct real-weight Gauss domain

Let `(L,w)` be a valued coefficient field whose value group is embedded in `R`; examples are `(K,ord_p)` and a fixed prolongation to `Kbar`. For real positive `alpha,beta`, every nonzero polynomial has the weighted Gauss valuation

\[
 v_{w;\alpha,\beta}\!\left(\sum a_{ij}U^iV^j\right)
 =\min_{a_{ij}\ne0}\{w(a_{ij})+i\alpha+j\beta\}.                 \tag{1}
\]

This is a valuation on `L[U,V]` and extends by quotients to `L(U,V)`. To prove multiplicativity, take initial forms in the polynomial ring over `gr_w(L)`, assigning weights `alpha,beta` to `U,V`. This associated graded coefficient ring is a domain. The product of two nonzero initial polynomials is therefore nonzero, so the minimum value of a product is the sum of the minima. This also proves the assertion for weights with rational dependencies; equal weights create residue polynomials, not a failure of the valuation property. The value group on the rational function field is the subgroup generated by `w(L*)`, `alpha`, and `beta`.

Formula (1) **does not define a finite real-valued valuation on all of `L[[U,V]]`**. Already in `K[[U]]`, with `w(z)=1`,

\[
 f=\sum_{n\ge0}z^{-n^2}U^n
\]

has term values `-n^2+n alpha`, unbounded below for every finite real `alpha`. Completion in normal degree alone does not control coefficient poles.

A sufficient explicit domain is

\[
 \mathscr R_{w;\alpha,\beta}
 =\left\{\sum a_{ij}U^iV^j:\
 \text{for every }B\in\mathbf R,
 \#\{(i,j):a_{ij}\ne0,\ w(a_{ij})+i\alpha+j\beta\le B\}<\infty
 \right\}.                                                       \tag{2}
\]

This is a subring of `L[[U,V]]`, containing polynomials and `O_w[[U,V]]`. Each nonzero support in (2) has a minimum: choose one term; the nonempty finite set below its value has a least element. For products, if the two minimum values are `a,b`, every pair of terms whose total value is at most `B` comes from the finite sets bounded by `B-b` and `B-a`. Thus products remain in (2). The initial polynomial of each element is finite, so the same graded-domain argument proves multiplicativity. Formula (1) gives a valuation on this ring and its fraction field. Its actual value group is the subgroup generated by the term values that occur; it need not be discrete.

This claim does not identify (2) with a complete Tate algebra or assert completeness. If the coefficient field is incomplete, a Cauchy sequence of constant series may already lack a limit. One may replace `L` by its completion if a complete coefficient field is needed, while retaining the explicit tail condition. The case of zero or negative normal weights requires different convergence hypotheses; no assertion about all formal series is made in that case.

## 3. A normal-first valuation on the full generic formal ring

There is a different, rank-two construction valid on **all** of `K[[U,V]]`. For nonzero `f`, let `n` be its least total normal degree and `f_n` its degree-`n` homogeneous part. Set

\[
 \nu_p(f)=\left(n,\ \min_{i+j=n}w(a_{ij})\right)
 \in\mathbf Z\times\mathbf Z
\]

with lexicographic order. There are finitely many terms of degree `n`, regardless of how rapidly poles grow at higher degree. The lowest homogeneous part of a product is `f_n g_m`; coefficient Gauss order on homogeneous polynomials is multiplicative. Thus `nu_p` is a valuation, extends to the fraction field, and satisfies

\[
 \nu_p(U)=\nu_p(V)=(1,0),\qquad \nu_p(a)=(0,w(a))\quad(a\in K^*).
\]

It differs from a real weighted sum: every positive normal order dominates every coefficient order, including arbitrarily large poles. It is not a valuation **centered on** `K[[U,V]]`: both a nonconstant coefficient and its inverse are units of that ring, whereas their values can be nonzero. It is centered on the subring `O_{C,p}[[U,V]]` in an integral local frame, where its center is `(m_p,U,V)`.

More generally, a valuation centered on the whole generic slice `K[[U,V]]` must be trivial on `K`. This follows immediately because each `a` and `a^{-1}` belongs to that ring. A nontrivial coefficient valuation should therefore not be described as a centered generic-slice valuation without specifying a smaller coefficient-integral model.

## 4. Intrinsic realization by blowup flags

Let `pi: Xtilde=Bl_C(X)->X`, and let `E` be its exceptional divisor. Since `C` and `X` are smooth,

\[
 E=\mathbf P(N_{C/X})\longrightarrow C.
\]

For each closed `p` of `C`, the fiber `E_p` is an irreducible divisor on the smooth surface `E`. Consider the flag

\[
 Xtilde\supset E\supset E_p.
\]

First take `ord_E` on the ambient function field `k(X)`. Its residue field is `k(E)`, which has the canonical subfield `k(C)` from `E->C`. Then compose with `ord_{E_p}` on `k(E)`. This gives an intrinsic rank-two valuation **ring**, centered at the generic point of `E_p` on the blowup and at `p` on `X`. Composition of valuation rings is justified directly by taking the inverse image of the second valuation ring under the residue map; see [Stacks, Lemma 10.50.10](https://stacks.math.columbia.edu/tag/088Z).

In a coefficient and normal formal model integral at `p`, this is precisely the preceding normal-first construction restricted to the ambient field. An arbitrary generic coefficient-field embedding is not such a model automatically. On the blowup chart `V=U T`, a lowest term has the form

\[
 U^n\sum_{i+j=n}a_{ij}T^j.
\]

After taking its residue along `E`, its order along `E_p` is the minimum coefficient order: the nonzero residue polynomial in the transcendental fiber parameter `T` cannot vanish identically. The final residue field is `k(E_p)=k(T)`, rather than `k`.

The valuation ring is canonical. Writing its value group as `Z^2` requires a splitting, equivalently a rational uniformizer for `E`. Replacing that uniformizer by another can change the numerical second coordinate by an integer multiple of the first. Integral choices near the generic point of `E_p` give the displayed local formula. This splitting issue does not change the valuation ring or its flag.

This is the simplest intrinsic construction here that retains coefficient vanishing without choosing a coefficient-field embedding into the ambient field. It is only one family of valuations. Further refinements can remember a point of `E_p`, thereby detecting a selected normal direction; the rank-two flag alone remembers a generic direction in that fiber.

There is **no general canonical restriction map** from all ambient valuations centered over `C` to valuations of `k(C)` merely because `C` is a closed subvariety. The closed embedding gives a residue quotient, not an inclusion `k(C)->k(X)`. A chosen formal coefficient field gives an inclusion into a completed local field and hence a restriction map, but that map depends on the choice. For valuations whose specified coarsening is `ord_E`, one can instead restrict the induced residue valuation on `k(E)` along the canonical `K->k(E)`. This is a genuine partial construction; it does not extend by assertion to every ambient valuation.

Accordingly the useful intrinsic organization is the space of ambient valuation rings with centers on models over `C`, together with the indicated blowup flag and residue maps when available. The individual relative Gauss charts remain computational charts on this structure. No stack, relative tropical space, or canonical global weight lattice is needed for the claims proved here.

## 5. Coordinate changes can require residue data

Even linear changes of normal coordinates need not act by integral linear transformations on a weight vector. For the Gauss valuation trivial on coefficients with

\[
 v(U)=1,\qquad v(V)=2,
\]

put `U'=U`, `V'=V+U`. Then `v(U')=v(V')=1`; however

\[
 v(V'-U')=v(V)=2.
\]

The monomial Gauss valuation with the new apparent weights `(1,1)` would assign `V'-U'` value `1`. Thus the transported valuation in the new chart needs the residue relation `in(V')=in(U')`, not just the two weights. This example is already in `GL_2(k)`. Scaling `U'=z^r U` also changes its weight to `alpha+r`; coefficients therefore participate in the coordinate transformation.

A sufficient invariance condition is that a coordinate substitution and its inverse both preserve the chosen filtration. For equal real normal weights and changes with coefficients regular at `p`, integral invertible linear term, and higher terms of at least that weight, this follows by substitution in both directions on the convergent domain. Arbitrary `K`-linear substitutions with poles do not satisfy this condition automatically.

For the normal-first flag valuation, changes of an integral normal frame with linear matrix in `GL_2(O_{C,p})` preserve the coefficient Gauss order of each lowest homogeneous form: both the substitution and its inverse have integral coefficients. This is the local reason its intrinsic flag construction glues. Merely changing a rational frame without transporting the model at `p` need not preserve the same numerical formula.

## 6. A nontrivial coefficient/normal calculation for mu4

Use the affine chart `x0=1`, and write

\[
 z=x_1,\qquad U=x_3-z^4,\qquad V=x_2-z^3.
\]

Then `F=-U`, and direct expansion gives

\[
 G=P(z,V)-3z^8U-3z^4U^2-U^3,
\]

where

\[
 P(z,V)=V^4+4z^3V^3+6z^6V^2+4z^9V.
\]

Consequently `(F,G)=(U,P)` in this chart. This cancellation uses the full ideal; the individual first normal symbols do not suffice in characteristic two.

At the endpoint `p: z=0`, set `w=ord_z`, give `V` positive real weight `rho`, and give `U` weight `17`. The coefficient field is unchanged. In characteristic zero,

\[
 v_\rho(P)=\min\{4\rho,3+3\rho,6+2\rho,9+\rho\}
 =\begin{cases}
 4\rho&0<\rho\le3,\\
 9+\rho&\rho\ge3.
 \end{cases}                                                    \tag{3}
\]

At `rho=3` all four displayed terms have value `12`. In characteristic two `P=V^4`, so

\[
 v_\rho(P)=4\rho.                                                \tag{4}
\]

For example, at `rho=4` the values of `(U,P)` are `13` and `16` in characteristics zero and two. At `rho=1` they are both `4`. At the critical weight `rho=3` they are both `12`, but their residue equations differ decisively. On the chart `V=z^3 xi`, divide by `z^12`:

\[
 \operatorname{in}(z^{-12}P)
 =\begin{cases}
 (1+\xi)^4-1=\xi^4+4\xi^3+6\xi^2+4\xi,&\operatorname{char}k=0,\\
 \xi^4,&\operatorname{char}k=2.
 \end{cases}                                                     \tag{5}
\]

In characteristic zero the four residue roots are `xi=zeta-1`, with `zeta^4=1`. The three nonidentity branches approach `C` with order `3` at this endpoint. They are actual residual curve components by the accepted global result, not exceptional components created downstairs by a blowup. In characteristic two the residue root is a single point of scheme length four. The derivative at the distinguished root is `4` in characteristic zero and zero in characteristic two.

The normal generic calculation has a different emphasis: since `z` is a nonzero element of `K`, the least normal power of `P` is `V` in characteristic zero and `V^4` in characteristic two. Thus the full generic initial ideals are `(U,V)` and `(U,V^4)`, with quotient lengths `1` and `4`. The endpoint weighted calculation retains the collision order of the residual branches, information absent from these generic colengths.

The second endpoint admits the analogous calculation in the accepted `x3=1` chart. The frame above has poles there and must not be treated as an integral frame at infinity.

The coefficient value groups remain `Z` in the displayed calculations, or `Q` after algebraic coefficient closure in either characteristic. The characteristic change is in the coefficients and residue algebra. It is the nonreduced group scheme `mu4` and the resulting transverse nilpotence; it need not produce ramification of a coefficient-field extension. Calling the characteristic-two nilpotent direction a ramified field branch would conflate different objects.

### 6.1 The precise characteristic-two boundary of the surface argument

The prescribed pair also shows exactly why the moving-singularity argument in the separate [intrinsic K3 proof proposal](2026-10-23-intrinsic-44-k3-proof-proposal.md) cannot be transported to characteristic two. This is a comparison with that proposal, not a dependency of the valuation constructions.

In characteristic two the first normal symbols of `(F,G)` on `x0=1` are `(U,z^8 U)`. On `x3=1`, with `c=x2/x3` and `A=x0/x3-c^4`, they are `(c^8 A,A)` up to the common unit sign. Hence the symbols have no common zero in their saturated line bundle `M(4)`, and their associated map is

\[
 C=\mathbf P^1\longrightarrow\mathbf P^1,
 \qquad [s:t]\longmapsto[s^8:t^8].
\]

This map is purely inseparable of degree eight. It follows that `M(4)=O(8)`, so `M=O(-8)` and the primitive quotient line `L=E/M` has degree `-6`, using `deg E=-14`. Thus the actual moving-symbol line has degree eight, yet a general symbol has **one eightfold zero**. Explicitly `1+lambda z^8=(1+a z)^8` for `a^8=lambda`; the characteristic-zero separability step that gives eight distinct zeros is unavailable.

There is also a stronger failure of the general-surface hypotheses. Put `H=F+lambda G` with nonzero `lambda`, and work over the algebraically closed characteristic-two field. Its only potentially nonzero partial derivatives are

\[
 H_{x_0}=x_3(x_0^2+\lambda x_3^2),\qquad
 H_{x_3}=x_0(x_0^2+\lambda x_3^2).
\]

The common zero set of all partial derivatives in projective space is the plane `x0+sqrt(lambda)x3=0`. On that plane,

\[
 H=(x_1+\lambda^{1/4}x_2)^4.
\]

The reduced singular locus of the surface is therefore the line

\[
 x_0+\sqrt\lambda x_3=0,\qquad
 x_1+\lambda^{1/4}x_2=0.
\]

Its dimension is one, so the surface fails regularity in codimension one and cannot be normal. Consequently this example violates both the separability and the normal-general-member inputs of the characteristic-zero surface proof. The conclusion is stronger and more precise than merely observing that the characteristic-two Picard-rank bound differs.

## 7. Even all scalar ideal values do not determine length

In `K[[U,V]]` consider

\[
 J_1=(U^2,V^2),\qquad J_2=(U^2,UV,V^2).
\]

For every valuation centered on the formal local ring, writing `a=nu(U)` and `b=nu(V)`,

\[
 \nu(J_1)=\min(2a,2b)=2\min(a,b)
 =\min(2a,a+b,2b)=\nu(J_2).
\]

Nevertheless their colengths are `4` and `3`: the standard monomials are respectively `1,U,V,UV` and `1,U,V`. This proves that retaining **all** scalar ideal values over all centered valuations still need not recover colength. Full initial or residue ideals retain information that these scalar values discard. Valuations on the quotient itself also kill nilpotents and hence cannot by themselves encode its nonreduced scheme structure.

The scalar Gauss computations in (3)-(4) are therefore diagnostics, not a length criterion. Neither equal valuation data nor equal value groups prove equal intersection schemes. Conversely the concrete difference at `rho=4` is not a universal characteristic-zero quartic obstruction: it belongs to the prescribed pair alone.

## 8. Verification boundary and successor handoff

The stdlib script

```
python3 research/computations/verify_intrinsic_valuations_2026_10_23.py
```

independently expands the two prescribed equations, verifies their cancellation identity over `Z` and mod `2`, computes (3)-(5) with exact rational weights, checks the characteristic-two derivatives and moving-symbol inseparability, checks the coordinate-change counterexample, and counts the monomial quotient bases in section 7. It prints `PASS` on success. These finite checks substantiate the explicit examples; they do not prove the general valuation lemmas, extension theory, global support premise, or a new `(4,4)` exclusion.

An independent read-only reviewer reconstructed the rank-two multiplicativity argument, the restricted-tail subring argument, the blowup-flag construction, the coefficient-extension scopes, and the explicit examples; it found no substantive error and ran the script successfully. Its requested precision improvement, requiring a coefficient **and** normal model integral at `p` in the flag comparison, has been incorporated. This review does not promote a canonical result or certify the separate global K3 argument. The characteristic-two surface comparison was added afterward and is verified by the extended script and direct derivative calculation above.

The strongest construction is the intrinsic rank-two blowup-flag valuation, together with an explicit convergent domain for real weighted coefficient/normal valuations. The main mathematical limitation is sharp: scalar ideal values lose colength, and generic formal data lose global ambient-realizability constraints. The next justified experiment is to retain the actual filtered residue ideal along the flag and the image of the ambient quartic jet map, and compare its allowable residue relations with the proposed intrinsic contact determinant. No claim that this comparison has already replaced the quartic-pencil classification is made here.



---

### Consolidated valuation theorem, example and limits

The preceding coefficient-valuation construction and the independent review establish one scoped local framework. Every nontrivial valuation of \(k(C)=k(z)\) trivial on algebraically closed \(k\) is proportional to \(\operatorname{ord}_p\) for a unique closed point \(p\in C\). A chosen prolongation to an algebraic closure has value group \(\mathbf Q\) and residue field \(k\); the prolongation itself is not canonical. For a valued coefficient field \((L,w)\) and positive weights \(\alpha,\beta\), the minimum
\[
v\!\left(\sum a_{ij}U^iV^j\right)=\min_{a_{ij}\ne0}\{w(a_{ij})+i\alpha+j\beta\}
\]
is a multiplicative valuation on \(L[U,V]\) and extends to \(L(U,V)\), because the coefficient associated graded ring is a domain. It is **not** finite on arbitrary \(L[[U,V]]\): the series \(\sum_{n\ge0}z^{-n^2}U^n\), at \(w(z)=1\), has unbounded-below term weights. A bounded-tail completion or a normal-first valuation is required.

The valuation's expression depends on a chosen normal frame. Under a general \(\mathrm{GL}_2(K)\) change, the values of the two new variables alone need not determine the original valuation; residue relations between their initial forms are necessary. Even the full collection of scalar ideal values does not in general recover Artin colength. The blowup-flag interpretation is intrinsic only when the flag, residue and descent data are retained. The \(\mu_4\) calculation is a prescribed local test, not a characteristic-zero exclusion. The proof, counterexamples and independent reconstruction remain in the source sections below; the separate weighted-chamber continuation is in [weighted initials and boundary lifting](NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md).

## 2026-10-23-intrinsic-contact-valuations-independent-audit.md

# Independent review of intrinsic contact and coefficient valuations

Date: 2026-10-23. Reviewer: `secondary_audit`, with a separate narrow external-source review by `valuation_link_audit` and the contact author's separately commissioned module review. Status: **independently reviewed secondary constructions; no new global nonvanishing or exclusion theorem is asserted here**.

## Scope and reviewed evidence

This review concerns the new [coefficient-valuation note](#2026-10-23-intrinsic-coefficient-valuations), its new [stdlib verification script](../computations/verify_intrinsic_valuations_2026_10_23.py), and the new [intrinsic cubic-contact note](2026-10-23-intrinsic-cubic-contact-construction.md). The repository [retrieval index](../INDEX.md), [authority rules](../AUTHORITY.md), and [independent-review requirements](../CONTRIBUTING_AGENT.md) govern the review. No inherited proof or computation was rerun.

The valuation note assumes the fixed smooth rational quartic over algebraically closed `k`, with `K=k(C)=k(z)`, and valuations trivial on `k`. Its characteristic-two calculation concerns the prescribed roots-of-unity pair only. The contact construction assumes an embedded pure quasiprimitive triple in a smooth threefold, saturated nilpotent layers `L` and `E2=L^2(D)`, and a surjection `I/I^2 -> L`. Statements about the corresponding rank-two module do not apply by assertion to arbitrary nonpure thickenings.

Both notes are supporting research. In particular, a limitation of either construction is not an objection to a separate proof that does not use it. Their scope does not change a promoted result or the status of any separately reviewed K3 argument.

## 1. Independent valuation reconstruction: retained qualifications

The primary coefficient-valuation section already proves classification of valuations on \(k(z)\), prolongation properties, multiplicativity of the weighted minimum on polynomials, the bounded-tail domain for series, the normal-first alternative and the blowup-flag construction. The independent reconstruction verified those arguments without changing their scope. In particular:

- The bounded-tail ring is closed under multiplication: only finitely many pairs of terms can contribute below a fixed bound, and the finite lowest-weight initial polynomials multiply without cancellation to zero. Its fraction-field value group is generated by the coefficient group and the two chosen weights; completeness is not asserted.
- The normal-first lexicographic valuation exists on the entire generic formal ring, but a nontrivial coefficient valuation is **not centered** on \(K[[U,V]]\), where coefficients and their inverses are units. Centering requires the coefficient-integral model.
- The intrinsic flag through the exceptional fiber \(E_p\) has final residue field \(k(E_p)=k(T)\), **not** the coefficient valuation's residue field \(k\). The flag determines a valuation ring without a canonical splitting of its rank-two group.
- Under a change such as \(V'=V+U\), the residue relation between initial forms is necessary to recover the valuation of \(V'-U'\). The source's invariance statement concerns integral frames, not arbitrary rational frames with poles.

These points are qualifications to the original proofs, not a second independent theorem or a global STCI obstruction.

## 2. External source checks

The external-source reviewer checked the primary Stacks sources. The sections originally linked as `0ASF` and `0EXQ` are appropriate. The exact composition lemma is [Stacks Lemma 10.50.10, tag 088Z](https://stacks.math.columbia.edu/tag/088Z); `00I8` is its containing section, not its direct lemma tag. The author was asked to use the direct tag.

More precise supporting statements are the [finite-extension value-group and residue-degree bound, tag 0ASH](https://stacks.math.columbia.edu/tag/0ASH), the [finite separable DVR normalization description, tag 09E8](https://stacks.math.columbia.edu/tag/09E8), [Galois transitivity on places, tag 09EA](https://stacks.math.columbia.edu/tag/09EA), the [purely inseparable extension statement, tag 0H37](https://stacks.math.columbia.edu/tag/0H37), and [henselization of valuation rings, tag 0ASK](https://stacks.math.columbia.edu/tag/0ASK). No material valuation-theoretic error was identified.

## 3. Exact finite replay and its limit

The reviewer independently ran only the new command

```
python3 research/computations/verify_intrinsic_valuations_2026_10_23.py
```

It exited successfully and printed all four `PASS` lines. This reproduces the integer polynomial cancellation, reduction modulo two, the weighted values `(4,4)`, `(12,12)`, `(13,16)` at the three selected weights, the critical residue polynomial, the coordinate-change example, and the two monomial colengths.

The general piecewise minimum formula follows directly from the four affine term weights, not from the finite sample of weights in the script. Likewise the divergent-tail obstruction and all-valutions equal-value example require their written general proofs; the finite replay alone would not establish their quantifiers. The global support of the prescribed roots-of-unity pair remains the explicitly inherited premise. The calculations distinguish coefficient/normal behavior for that pair and do not prove universal nonexistence of characteristic-zero quartic pairs.

## 4. Contact module and determinant: reconstruction

The essential local defect calculation is correct under the stated saturated-layer hypotheses. Over a completed local coefficient DVR `A`, the triple has algebra

```
A[x,y]/(x^2-a*y, x*y, y^2),
```

where `a` cuts out `D`. At a defect point, the second ambient normal direction must supply the saturated second layer because `x^2` cannot do so modulo the maximal ideal. With `f=x^2-a*y`, `g=x*y`, `h=y^2`, the two Hilbert--Burch relations reduce modulo `I J` to `a*h=0`. Thus

```
J/IJ = A*f + A*g + (A/(a))*h,
(J/IJ)/torsion = A*f + A*g.
```

The first-symbol image is `K0(-D)`, and its kernel is `L tensor E2`. Products of lifts define this latter arrow independently after passing to the torsion-free quotient: changing a first-layer lift by the second layer introduces a square of a second-layer lift, whose class is torsion. This explains both the need for the torsion-free quotient and the exact cancellation

```
det M_Y = (L tensor E2) tensor K0(-D)
        = K0 tensor L^3 = det(E) tensor L^2.
```

Accordingly the determinant of the actual ambient source has the asserted global target, of degrees four and six for the two stated quartic cases. A source-basis change multiplies its coordinate representative by the source determinant; an adapted target change multiplies it by the inverse target determinant. The displayed generic law `Delta'=Delta/(a*d^3)` follows by expanding the triangular basis change. These are line-bundle transitions, not invariance of a numerical polynomial without its trivializations.

Two precision corrections were requested from the contact author during review. First, the equivalence between vanishing of the relation-line image and vanishing of the determinant requires the first-symbol map to be generically nonzero. If that map is zero, its kernel is all of `W` and the determinant is already zero, while the image of `W` in the kernel line can be nonzero. Second, a Taylor remainder denoted only `O(normal order 4)` must not silently absorb the possible terms `m^2` and `m*t^2`. The suitable remainder for the displayed cubic-contact calculation is `(m^2,m*t^2,t^4)`, or equivalently weight at least four for weights `(2,1)` before replacing `m` by `m-f2*t^2`. These corrections do not alter the determinant construction.

With a nonzero first symbol and common contact at least three, substituting the formal branch of one equation gives a residual `t^3` coefficient `Delta/h0`. Hence nonzero determinant is equivalent to local length three; zero determinant gives length at least four when the colength is finite. The two successive blowup interpretation agrees with this calculation. Defect points require the global module, because the displayed rational normal charts need not extend there.

## 5. Accepted boundary and remaining implication

The two secondary constructions correctly isolate what their data retain. Scalar values of ideals discard colength even when all centered valuations are included; the example `(U^2,V^2)` versus `(U^2,UV,V^2)` has equal ideal values and colengths four and three. The contact determinant retains a residue linear-dependence condition absent from a scalar ideal value.

Neither construction forces the determinant of every actual ambient quartic source to be nonzero. The stated abstract vector-bundle examples and the local pair `(n,n+t^4)` correctly exhibit the gap in a degree-only or purely formal argument. The missing implication in that route is a global assertion about the image of actual ambient quartic sections. This is a precisely scoped limit of that route; it does not make a separate intrinsic proof provisional when that proof does not invoke global determinant nonvanishing.

No claim has been promoted by this audit, no inherited proof was reopened, and no unrestricted STCI conclusion is asserted.

## 6. Integration follow-up on the characteristic-two comparison

The root integration review also checked the subsequently added section 6.1
of the valuation note. Direct differentiation of H=F+lambda G in
characteristic two gives H_x0=x3(x0^2+lambda x3^2) and
H_x3=x0(x0^2+lambda x3^2), with both other derivatives zero. Their
projective common zero set is the plane x0+sqrt(lambda)x3=0. Restriction
of H to it is (x1+lambda^(1/4)x2)^4, so the reduced surface singular
locus is the indicated line. The two endpoint symbol charts give the
map [s:t] to [s^8:t^8], which is purely inseparable of degree eight.
These direct calculations establish the stated failure of the separable
moving-symbol and normal-general-member hypotheses for this prescribed
positive-characteristic example. The extended valuation script was
replayed successfully and includes the additional characteristic-two
moving-symbol and singular-line PASS output. This follow-up does not
change the general domain or colength limitations reviewed above.



---

## 2026-10-23-intrinsic-quadruple-local-algebra.md

# Intrinsic quadruple algebras and the singularities of a general pencil member

Date: 2026-10-23. Status: **independently reviewed supporting local-algebra
proof; not a promoted canonical result**. This note supplies the local step
for the proposed intrinsic K3 proof of the fixed characteristic-zero (4,4)
exclusion. It uses no classification of normal directions, primitive triples,
quartic carriers, or quartic contact pencils.

## Precise local hypotheses

Let k be an algebraically closed field of characteristic zero, R=k[[t]],
and K=k((t)). Let B be a finite-free local R-algebra of rank four, with
reduction R and generic algebra B_K=K[z]/(z^4). Suppose B is a relative
Gorenstein algebra. Put

    N_i = B intersect (z^i)B_K,   E_i=N_i/N_(i+1).

The saturated pairing theorem gives an isomorphism

    E_1 tensor E_2 -> E_3.

Write d for the valuation of the multiplication E_1^2 -> E_2. In the
global notation E_i=L^i(D_i), this is the local multiplicity of D_2;
perfect pairings give D_2=D_3. The pairing theorem is the accepted general
local-algebra premise in
[the MF6 pairing audit](2026-10-05-mf6-pairing-audit.md), sections 1--2.
It is independent of any quartic-carrier classification.

For the assertion about ambient formal coordinates, assume additionally

    B = k[[t,x,y]]/J,   radical(J)=(x,y).

A complete intersection supported on the smooth curve satisfies these
finite-flat hypotheses: its Cohen--Macaulay property makes t a
nonzerodivisor, and its Artin special fibre is Gorenstein. The choice of
the lift t of a parameter of the reduced curve supplies the R-algebra
structure. This is a local choice, not a claimed global retraction.

## 1. A normal form from multiplication, with no direction classification

Choose a in N_1 lifting a generator of E_1 and b in N_2 lifting a
generator of E_2. The product ab generates N_3=E_3, by the perfect pairing.
The elements 1,a,b,ab form an R-basis, by the saturated filtration. Since
N_i N_j is contained in N_(i+j),

    b^2=0,  a(ab)=0,
    a^2 = t^d u b + lambda ab,

where u is a unit and lambda belongs to R. Rescale b by u, and then replace
a by a-lambda b/2 (with the coefficient lambda interpreted after the
rescaling). Because b^2=0, this gives exactly

    a^2=t^d b,   b^2=0.

The algebra R[A,B]/(A^2-t^d B,B^2) is free on 1,A,B,AB, so the resulting
surjection onto B is an isomorphism. Thus

    B is isomorphic over R to R[A,B]/(A^2-t^d B,B^2).

This is an isomorphism of algebras with the saturated filtration. Its proof
uses the complete multiplication, rather than just an associated graded
algebra. In particular, the possible correction lambda ab was removed
explicitly. In characteristic two this removal is unavailable, which is a
real restriction on this argument.

If d>0, the special fibre is k[A,B]/(A^2,B^2). Hence A,B give an independent
basis of its cotangent space. Any lifts of A,B to the ambient formal ring,
together with t, form formal coordinates by the formal inverse function
theorem. The embedded ideal therefore has the exact normal form

    J=(x^2-t^d y, y^2).                                      (1)

There is no omitted higher-order ambient correction: after the coordinate
change the quotient by the displayed two generators is already free of
rank four and maps isomorphically onto B.

For d=0 the special fibre has embedding dimension one. A smooth relative
normal coordinate belongs to J, and a lift u of its remaining nilpotent
generator gives formal coordinates with

    J=(v,u^4).                                               (2)

Equivalently, the abstract normal form in this case is R[A]/(A^4), and a
surjection from the smooth ambient ring can be completed by one element
of its kernel to a formal coordinate system.

## 2. The fixed divisor of the first normal symbols is exactly D_2

At d>0, reduce (1) modulo (x,y)^2. Its image in the ambient conormal
module R x direct sum R y is

    t^d R y.

The saturated image is R y. Thus the vanishing multiplicity of the actual
first-normal image relative to its saturation is exactly d. At d=0,
(2) has a primitive first-normal image. Consequently, globally the fixed
divisor A of the first symbols of a generating pair is exactly D_2=D_3,
not only bounded above by D_3.

The equality uses the rank-four Gorenstein multiplication. It is not
asserted for arbitrary lengths or arbitrary non-Gorenstein algebras.
The linearized image belongs to J modulo I_C^2; it must not be confused
with the torsion-free quotient of the ordinary nilradical conormal.

## 3. The defect singularity for coefficient functions of all variables

Let d>0. A general element of a pencil generating J is

    f=U(t,x,y)(x^2-t^d y)+V(t,x,y)y^2,

where U and V are units. This unit condition excludes at most two members
of the pencil at each defect point: the local change from the original
two generators to the generators in (1) has invertible coefficient matrix.
After dividing by U, put v=V/U, a unit, and write

    f=x^2-t^d y+v(t,x,y)y^2.                                (3)

The Hessian in x,y is invertible at the origin. The formal implicit
function theorem gives its critical section x=x(t),y=y(t). The critical
equations imply

    y(t)=t^d/(2v(t,0,0))+O(t^(2d)),
    x(t)=O(t^(2d)).

Substitution gives the critical value

    h(t)=-t^(2d)/(4v(0,0,0))+O(t^(2d+1)).

The formal Morse lemma with parameter t therefore transforms (3) into a
nondegenerate quadratic form in two variables plus h(t). As k is
algebraically closed of characteristic zero, a unit root and a linear
change of the quadratic variables identify it with

    X Y + T^(2d).

The surface has rational double point type A_(2d-1), whose minimal
resolution has 2d-1 independent exceptional (-2)-curves. This proves the
claim for general unit coefficient functions, not only for constant
linear combinations of the displayed normal-form generators.

## 4. A simple moving zero gives type A3

At a primitive point use (2). Write a member of the global pencil as

    f=A(t,u,v)v+B(t,u,v)u^4.

Suppose A(t,0,0) has a simple zero at t=0. Since the two original members
generate J, B(0,0,0) is nonzero for the member whose first coefficient
vanishes. Because the t derivative of A is a unit, t'=A(t,u,v),u,v are
formal coordinates. Then

    f=t'v+B'(t',u,v)u^4.

A fourth root of the unit B' gives the further coordinate
u'=u(B')^(1/4), producing exactly f=t'v+(u')^4. Thus the singularity is A3.
This also proves that varying coefficients cannot lower its exceptional
rank below three.

## 5. Application to the two numerical quadruple types

In this section O(n) denotes degree n on P1, while M(4) denotes the
ambient twist M tensor O_C(4)=M tensor O_P1(16).

For the fixed C=[s^4:s^3t:st^3:t^4], use the accepted
E=O(-7)^2 and the general saturated Gorenstein duality, together with
omega_Z=O_Z(4) for a hypothetical (4,4) intersection. These give

    L=O(e-7),  E_3=O(-18),
    deg D_2=deg D_3=3-3e,  e=0 or 1.

Let M be the kernel of E -> L. Then M=O(-7-e). The first symbols of the
two quartics are sections of M(4)=O(9-e), and section 2 proves that their
fixed divisor is D_2. Removing it yields a basepoint-free pencil of degree

    n=(9-e)-(3-3e)=6+2e.

The pencil is nonconstant because the pullback of O_P1(1) is the generated
line bundle O(n), whose degree is positive. A nonconstant map of smooth
curves in characteristic zero is separable, so a general fibre has n
distinct points avoiding the finitely many defect points.

For e=1 this produces eight A3 points, hence exceptional rank 24.
For e=0 it produces six A3 points, hence rank 18, and every defect of
multiplicity d adds rank 2d-1. Since deg D_2=3, its three possible
partitions have total extra ranks

    1+1+1 -> 3,   2+1 -> 4,   3 -> 5.

Every case therefore has exceptional rank at least 21. The K3 Picard bound
then finishes the proposed global proof, once integrality, Bertini
smoothness away from C, and the K3-resolution hypotheses are supplied by
the principal note. Those global facts are not replaced by this local
note.

## Evidence, status, and reproducibility

The new elementary identities, generic Frobenius determinant, and
representative Jacobian algebras are
checked without external packages by

    python3 research/computations/verify_intrinsic_quadruple_local_algebra_2026_10_23.py

The [independent K3 proof audit](2026-10-23-intrinsic-44-k3-independent-audit.md)
reconstructs this local argument and its use in the principal proof.
The calculation checks local formulas and the numerical rank budget; the
proof above establishes the classification-free normal form and the
variable-coefficient assertion. The script does not by itself prove the
global exclusion. The unbounded-degree STCI problem is unaffected.



---

## 2026-10-23-intrinsic-cubic-contact-construction.md

# Intrinsic cubic contact of an embedded quasiprimitive triple

Date: 2026-10-23. **Independently reviewed new construction; not canonically promoted.**
This note supplies an intrinsic replacement for the *definition* and coordinate
invariance of the cubic-contact determinant. It does not supply an intrinsic
nonvanishing theorem for the quartic source, and therefore does not prove the
characteristic-zero (4,4) exclusion independently of the existing proof.

## Scope and inherited inputs

Let X be a smooth threefold, C a smooth curve in X, I its ideal, and
E=I/I². Let Y be a pure embedded quasiprimitive triple supported on C,
with ideal J. Its saturated nilpotent layers are line bundles

    E1=L,  E2=L²(D),

where D is the effective divisor of the nonzero multiplication
L² → E2. The quotient E → L is assumed surjective; put
K0=ker(E → L). These are the hypotheses used below. In particular,
this is not a claim about arbitrary non-Cohen–Macaulay thickenings or a
filtration by unsaturated nilradical powers.

For the rational quartic C=[s⁴:s³t:st³:t⁴] in characteristic zero,
the accepted inputs E=O(-7)² and O_C(1)=O(4) come from
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md).
The two possible first layers L=O(-7), O(-6) in a hypothetical (4,4)
intersection are inherited from adjunction and the saturated pairing argument
in [the pairing audit](2026-10-05-mf6-pairing-audit.md). This note does not
reprove that numerical reduction. It does not use the primitive-direction
classification or any quartic-carrier exclusion.

The existing coordinate determinant being reconstructed is in
[the filtered proof proposal](2026-10-23-quartic-44-filtered-proof-proposal.md),
section “A common pencil criterion.” Its meanings are exactly these:

    H=h_H*m+k_H*ell²+e_H*m*ell+c_H*ell³+R_H,
    m=f2*ell² on the triple,
    k_H+h_H*f2=0,
    tau_H=c_H+e_H*f2,
    Delta=h_H0*tau_H1-h_H1*tau_H0.

Here R_H has weighted order at least four for weights (m,ell)=(2,1).
It may contain terms m², m*ell², m²*ell and m³ of ordinary normal
order two or three: these terms do not contribute after substituting
m=f2*ell². Thus the notation that suppresses these terms is not literally
an ordinary fourth-power remainder. The notation tau is not an
independent third normal symbol.

## 1. The canonical rank-two target

Define the coherent O_C-module

    M_Y=(J/IJ)/torsion.

Here “torsion” means the subsheaf supported at finitely many points of the
smooth curve C. It is essential to remove it. The module J/IJ itself can
have torsion at the nonprimitive points of the triple.

**Proposition 1 (new, proof below).** M_Y is a rank-two vector bundle, with
a canonical exact sequence

    0 → L⊗E2 → M_Y → K0(-D) → 0.                 (1)

Consequently there is a canonical identification

    det M_Y = K0⊗L³ = det(E)⊗L².                (2)

In particular, the defect divisor cancels from the determinant line. This
cancellation does not mean the module or its extension class is independent
of the defect or of the embedded triple.

Proof. Away from D the triple is primitive. Local normal parameters x,y
can be chosen with J=(y,x³). The quotient J/IJ is freely generated by y,x³;
its first-symbol map has image K0 and kernel L³. This gives (1) there.

At a point of D, work in the formal local ring, choosing a coefficient
parameter along C and normal parameters x,y. A local generator of L lifts
to x. Since the embedding generates the triple algebra, a normal parameter
y mapping to the saturated second layer is a generator of E2 at a defect
point: in the fiber there x²=0, so the second normal generator must supply
E2. After multiplication by units and adjustment of lifts, the algebra is

    O_Y = O_C[x,y]/(x²-a*y, x*y, y²),

where a is a local equation for D. This description can be made after
formal completion; the ideal and module conclusions descend by faithful
flatness. The use of local coefficient parameters does not assert that Y
admits a global retraction to C.

Put f=x²-a*y, g=x*y, h=y². The Hilbert–Burch relations are

    y*f-x*g+a*h=0,
    y*g-x*h=0.

Modulo IJ the only surviving relation is a*h=0. Hence

    J/IJ = O_C*f ⊕ O_C*g ⊕ (O_C/(a))*h,
    M_Y = O_C*f ⊕ O_C*g.

Its first-symbol image is generated by -a*y, namely K0(-D), and its
kernel is generated by x*y. The latter has the transition law L⊗E2.
Intrinsically, lift a section of L and a section of E2 to I and multiply.
The product is in J. Changing a lift by J changes the product by IJ;
changing the first lift by the second layer changes it by a product of
two second-layer lifts, whose class is torsion and disappears in M_Y.
This constructs the left arrow in (1) independently of the parameters.
The displayed local calculation proves exactness and local freeness.
Taking determinants and using E2=L²(D) proves (2). □

The local model is also a warning: replacing M_Y by J/IJ and taking a
naive determinant would carry torsion supported on D, and replacing E2
by the ordinary nilradical square would lose the divisor a.

## 2. The determinant of an actual global source

Let A be a line bundle on X, and let W be a two-dimensional k-vector
subspace of H⁰(X,J⊗A). Restriction induces an intrinsic morphism

    rho_Y: W⊗O_C → M_Y⊗A|C.

Its top exterior power is the section

    delta_Y(W)=wedge²(rho_Y)
      in H⁰(C, det(W)^*⊗det(E)⊗L²⊗A|C²).       (3)

This is the natural global target. The source must be actual ambient
sections through the embedded triple. Replacing W by arbitrary abstract
sections of a symmetric conormal bundle changes the problem.

At the generic point, write K=k(C), choose normal parameters n,t with
J_K=(n,t³), and trivialize A. The images of a basis H0,H1 in M_Y⊗K are

    H_i = h_i*n+tau_i*t³ mod I J.

Then the coordinate representative of (3) is precisely

    Delta=h0*tau1-h1*tau0.                     (4)

Equivalently, let B be the kernel of the first-symbol map
W⊗O_C → K0(-D)⊗A|C. The restriction of rho_Y to B lands canonically in
L⊗E2⊗A|C. If the first-symbol map is generically nonzero, B has rank one
and its generic vanishing is equivalent to Delta=0. If both first symbols
vanish, Delta vanishes automatically and this equivalence is unavailable.
Thus one may
regard cubic contact as the next image of the relation between the first
symbols. It is not an independently chosen third Taylor coefficient.

For quartics A=O_X(4), A|C=O(16), det E=O(-14). Therefore

    L=O(-7):  target degree 4,
    L=O(-6):  target degree 6.                 (5)

The known nonzero affine expression 32*z*(z-2)*(z+2) in the degree-four
case is consistent with a degree-four determinant line. Identifying its
divisor, including its behavior at infinity, additionally requires the
transition from the coordinates used there to a regular local frame of
that line. This consistency check is not used to prove nonvanishing.

## 3. Coordinate and generator transformation laws

At the generic point, any other adapted basis of the same triple has

    n'=a*n+b*t³ mod IJ,
    t'³=d³*t³ mod IJ,

with a,d in K^× and b in K. Consequently

    h_i'=h_i/a,
    tau_i'=(tau_i-(b/a)*h_i)/d³,
    Delta'=Delta/(a*d³).                     (6)

The factor a*d³ is exactly the transition of K0⊗L³. Nonlinear changes
of the normal parameters, and changes of the tangential ambient
coordinate restricting to the same coordinate on C, are absorbed by
this basis change in the intrinsic module M_Y. They need not act by
integral linear transformations on exponent lattices.

Changing the basis of W by A0 in GL2(k) multiplies Delta by det(A0).
More generally, changing local generators of the same ideal by an
invertible matrix over the ambient local ring multiplies it by the
determinant of that matrix restricted to C. Multiplying the local
trivialization of the hypersurface bundle by a unit has the square
transition prescribed by A|C². These statements follow directly from
the morphism rho_Y, without Taylor calculations.

There are two different changes sometimes called changing a “triple
lift.” Replacing n by n-r*t³ leaves J=(n,t³) unchanged and changes
tau_i to tau_i+r*h_i; Delta is unchanged. This is the freedom to choose
a candidate fourth-order extension of a fixed triple. In contrast,
changing f2 in m=f2*t² changes the embedded triple itself; it changes
the quadratic containment conditions and is not an invariance of (3).
When one of the first coefficients h_i is nonzero and the pair has
contact at least three, its common generic triple has f2=-k_i/h_i and
is therefore determined by the pair.

## 4. Exact blowup interpretation over K

This construction works over any coefficient field; no characteristic-zero
division occurs. Take R=K[[m,t]], and suppose that the two equations have
normal order one and contain m=f2*t² modulo t³. Write

    H_i=h_i*m+k_i*t²+e_i*m*t+c_i*t³+R_i,
    k_i=-h_i*f2.

The remainder R_i has weighted order at least four for weights
(m,t)=(2,1), so it becomes a term of order at least two after the
substitution m=t²*(u+f2) and division by t².

Choose a basis of their pencil for which both h_i are nonzero. Such a
basis exists over the infinite field K whenever the common first-symbol
map is nonzero. Blow up the closed point in the normal slice. On the
chart m=t*m1, divide both equations by t. Their strict transforms pass
through m1=t=0, with common tangent m1=f2*t.

Blow up that point, using m1=t*m2 and dividing the original equations
by t². At the common point m2=f2, put u=m2-f2. Then

    H_i/t² = h_i*u+tau_i*t+terms in (u,t)²,
    tau_i=c_i+e_i*f2.                        (7)

Thus Delta is the wedge of the two tangent covectors of the twice
transformed equations. Its nonvanishing means that those strict
transforms meet transversely at the second infinitely near point.
The three successive local contributions are 1,1,1, giving total
intersection length three.

An algebraic proof avoids using an intersection formula: solve H0=0
formally for n=m-f2*t², and substitute in H1. The t³ coefficient is
Delta/h0. Hence, if the pair has finite colength,

    Delta != 0  iff  length_K R/(H0,H1)=3,
    Delta = 0   iff  length_K R/(H0,H1)>=4.    (8)

The equivalence assumes common contact at least three and a nonzero
first-symbol map. Vanishing alone does not assert that the length is
exactly four, nor that a global embedded fourth extension exists.

Over the open subset C\D these are the ordinary blowups along the
successive common normal-direction sections. At points of D, a rational
expression f2 can have poles and these particular charts cease to be
valid. Formula (3), obtained from M_Y, still extends across D. No claim
is made here that the same affine blowup charts cover those points, or
that a vertical exceptional locus supplies a residual component in X.

## 5. Initial ideals and valuations

After choosing a common triple, give n weight 3 and t weight 1. The
weight-three initial forms are

    h_i*n+tau_i*t³.

If Delta is nonzero, they generate (n,t³); all later terms have higher
weight. The quotient therefore has length three. If Delta vanishes,
the weight-three initial forms align and a cancellation must be
continued. Solving one equation exactly gives a parameter n0 whose
first equation is a unit times n0; the *full* initial ideal of the
pair then has the form (n0,t^r), with r the generic intersection length.
This description uses the full ideal and the formal branch defined by
one equation, rather than the separate original initial forms.

In this chart a single valuation of the ideal, such as its minimum
weight, does not distinguish (n,t³) from (n,t⁴): both contain n and have
the same minimum for many weights. The determinant detects linear
independence in a residue graded piece; its information includes
coefficients, not just values.

## 6. What this construction does and does not replace

The construction replaces the coordinate definition of Delta by the
canonical map (3), including its extension through a quasiprimitive
defect. It explains the exact two-blowup meaning and the fourth-extension
obstruction. It is valid in characteristic two as well as in
characteristic zero. Characteristic dependence must enter through the
actual embedded triple and actual ambient source rho_Y, not through
the determinant formalism itself.

It does **not** replace the old proof's assertion that delta_Y(W) is
nonzero for every permitted proper quartic pencil. The degree in (5)
permits nonzero sections but does not force them. More strongly, the
bundle numerics and (1) alone permit rank-one maps from independent
two-dimensional spaces of sections. For example, the abstract
degree-four situation admits

    0 → O(-2) → O(2)² → O(6) → 0

by using two degree-four polynomials with no common zero for the left
arrow. Two independent sections inside one O(2) summand give a map
O² → O(2)² with identically zero determinant. Similarly the
degree-six situation permits

    0 → O(-2) → O(3)² → O(8) → 0,

and independent sections of one O(3) summand. These examples match the
twist by O_C(4) of the two numerical exact sequences (1). They are
abstract bundle examples, not asserted embedded triples or ambient
quartic pencils. They prove that a degree-only argument has an explicit
logical gap: it must still impose the actual global jet source.

Locally the pair (n,n+t⁴) contains the triple (n,t³), has Delta=0,
and has length four in every characteristic. Thus local formal
geometry by itself also cannot provide the sought characteristic-zero
contradiction.

If pursuing the determinant route, the unresolved intrinsic task is sharply
expressible: for the actual
embedding C⊂P³ and the two adjunction-allowed types of Y, prove that
every two-dimensional proper ambient quartic source W⊂H⁰(J(4)) has
wedge²(rho_Y) nonzero, without enumerating triple directions or
quartic pencils. The argument must use more than the degrees of the
bundles in (1).

The separate [K3 proof proposal](2026-10-23-intrinsic-44-k3-proof-proposal.md)
offers a different intrinsic route: its singularity budget aims to replace
the need to prove this determinant nonvanishing at all. That argument is a
separate proposal with its own audit and dependencies; no assertion in the
present note uses it as a premise.

## Verification record and independent review

The identities (6) and (7), the cubic-contact reduction, and the local
Hilbert–Burch identities are checked by
[the reproducible verification script](../computations/verify_intrinsic_cubic_contact_2026_10_23.py)
using `/tmp/stci-z4-env/bin/python`; the tested residuals include

    Delta' - Delta/(a*d³),
    H(t²*(u+f2),t)/t² - (h*u+(c+e*f2)*t+e*u*t),

with k=-h*f2. Both simplify to zero. This is a check of the displayed
polynomial identities, not of the geometric global-source nonvanishing.

The [independent secondary audit](2026-10-23-intrinsic-contact-valuations-independent-audit.md)
reconstructs the local normal form at D, the torsion-free quotient in
Proposition 1, the canonical gluing of L⊗E2 into M_Y, and the distinction
between changing the triple and changing its fourth-order lift. Its two
precision corrections, the nonzero-first-symbol hypothesis and the
weighted Taylor remainder, are incorporated above. No canonical theorem
status is changed.

