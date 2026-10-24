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
