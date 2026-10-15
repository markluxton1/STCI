# Smooth formal branch and the ruled-model degree bound

Date: 2026-10-15.

Status: independent conceptual review of the normalization and intersection-theoretic steps in the proposed no-infinite-lift argument. This note assumes the stated algebraization-as-a-branch theorem applies; it does not re-prove that theorem, establish existence of an all-orders Cartier lift, or promote the resulting exclusion to an accepted repository theorem.

## Input and purpose

Let `B = Bl_C(P^3)` for the smooth rational quartic `C`, let `E = P^1 x P^1`, and let `Z` be a smooth curve of class `(2,2)` on `E`. Thus `Z` has genus one. Assume an all-orders lift yields a smooth formal surface `V` along `Z`, transverse to `E`, with

`N_{Z/V} = O_Z(7,-1)`, of degree `12`.

Assume moreover that `V` is a formal branch of an actual integral surface `W` in `B`. The original concern was whether the entire completion of `W` must equal this branch. The degree-bound argument reviewed below does not need that assertion. Other formal branches, or other curves of `W cap E`, may remain.

## 1. Normalization preserves the chosen smooth branch

The precise local input is that, at each closed point `z` of `Z`, the induced maximal-ideal completion of `V` is a regular two-dimensional minimal branch of `O_{W,z}^`. This is the meaning of "formal branch" needed here; a merely generically finite formal map into `W` would require a separate argument.

Surfaces of finite type over a field are excellent, and their normalization is finite. For an excellent reduced local ring, normalization and completion identify the completed local factors of the normalization with the normalizations of the completed branches. The chosen branch is regular, hence normal already. Its normalization factor therefore coincides with it. In particular the selected point of the normalization of `W` has regular completion, hence is a regular point.

The global formal branch makes these local choices compatible. Equivalently, each local integral element of the normalization maps into the regular formal branch because the latter is integrally closed in its fraction field. This gives a morphism from `V` to `W^nu`; reducing modulo the ideal of `Z` gives a section `Z -> W^nu` over `Z`. Its image `Z'` is isomorphic to `Z`, the normalization is smooth along `Z'`, and its formal completion along `Z'` is the chosen `V`.

Reference for the normalization/completion mechanism: Stacks Project, [Branches of the completion, Section 15.110](https://stacks.math.columbia.edu/tag/0C27), especially the proof of Lemma 15.110.8. It decomposes the completed normalization into completed local normal factors and identifies their minimal branches. One should check this exact local branch hypothesis when inserting the algebraization theorem into the final proof.

Resolve the normalization with centers outside its regular neighborhood of `Z'`. This yields a smooth projective surface `T` containing the same curve `Z'`, with unchanged formal neighborhood. Write `Z` again for this curve. Consequently

`Z^2_T = 12`.

Let `H` denote the pullback of a hyperplane under `T -> W -> B -> P^3`. It is nef. Since `H|E = O_E(4,0)` and `Z = (2,2)`,

`H.Z = 8`.

The surface `W` is not `E` because the selected branch is transverse to `E`. Thus its image in `P^3` is a surface, and the map is birational onto that image. If its degree is `d`, the projection formula gives

`H^2 = d > 0`.

Surface resolution references: Stacks Project, [Resolution, Section 54.14](https://stacks.math.columbia.edu/tag/0BGJ). Resolution can preserve a prescribed regular open set. Since the starting normalization is projective, the resulting smooth proper surface is projective.

## 2. Hartshorne's theorem supplies a ruled model near the curve

Hartshorne's Theorem 4.1 applies because

`Z^2 = 12 > 4 g(Z) + 5 = 9`.

It gives a geometrically ruled surface `R -> Z` and a section `Z_0` such that `(T,Z)` and `(R,Z_0)` are equivalent. "Equivalent" is defined in the paper as a birational map inducing the identity on the curve and an isomorphism on open neighborhoods of it. In particular

`Z_0^2 = 12`.

Primary reference: R. Hartshorne, *Curves with high self-intersection on algebraic surfaces*, Publ. Math. IHES 36 (1969), 111--125, [Theorem 4.1, printed p. 122; definition on printed p. 111](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).

## 3. The square comparison is valid

Resolve the birational map into a common smooth surface

`q: U -> T`, `p: U -> R`.

Because the birational equivalence is an isomorphism near the curves, this can be done with all point-blowup centers outside those neighborhoods. Put `L = q^*H` and `D = p_*L`. Choose an actual Cartier divisor representing `L` before pushing forward; `R` is smooth, so its pushforward is Cartier. Equivalently this construction is well-defined on numerical divisor classes.

For a single point blowup `b: X' -> X`, any divisor class `A'` has a unique expression

`A' = b^*A + c E_b`,

where `A=b_*A'`; orthogonality and `E_b^2=-1` imply

`(A')^2 = A^2 - c^2`.

Iterating through `p`, using total-transform exceptional classes if desired, gives

`H^2 = L^2 = D^2 - sum_i c_i^2 <= D^2`.

No sign assertion for the coefficients `c_i`, and no nefness assertion for `D`, is required for this inequality. The neighborhoods of `Z` are unchanged, so

`D.Z_0 = L.Z = H.Z = 8`.

Also `D` is nef: for any integral curve `Gamma` on `R`, its total transform `p^*Gamma` is effective, hence

`D.Gamma = L.p^*Gamma >= 0`.

Here `L` is nef because it is a pullback of `H`.

The point-blowup factorization used above is standard for proper birational morphisms between smooth surfaces; see Stacks Project, [Lemma 54.17.1](https://stacks.math.columbia.edu/tag/0C5Q).

## 4. The numerical bound

Write the numerical class of `D` on the ruled surface as

`D == a Z_0 + b f`,

where `f` is a fiber. Here `a=D.f` is an integer. Nefness gives `a>=0`; if `a=0`, then `D^2=0`, contradicting `D^2>=H^2>0`. Hence `a>=1`. From `Z_0^2=12`, `Z_0.f=1`, and `f^2=0`,

`8 = D.Z_0 = 12a+b`,

and therefore

`D^2 = 12a^2+2ab = 16a-12a^2`.

For integral `a>=1`, this expression is at most `4` (its value at `a=1`); for `a>=2` it is negative and hence impossible here. Thus in fact `a=1`, `D^2=4`, and

`d = H^2 <= 4`.

This establishes the contested square comparison and degree estimate, under the stated local branch input. It does not assert that `W` has only one branch along `Z`.

## 5. Connection to the proposed contradiction

The remaining elementary geometric implication is that the strict transform `W` has generic multiplicity `m>=2` along `C`: the effective divisor `W|E` contains the entire integral `(2,2)` curve `Z`, whose degree over `C` is two. For a general fiber of `E -> C`, the degree of `W|E` is precisely `m`, so `m>=2` even if extra components exist.

Consequently a general plane section of the integral image surface of degree `d<=4` is an integral plane curve singular at the four distinct points where the plane meets `C`. Each such singularity has delta invariant at least one. This contradicts the arithmetic-genus bound `(d-1)(d-2)/2<=3`.

To use this as a finished exclusion, the parent proof should explicitly state the algebraization theorem's exact branch conclusion and the generic-plane-section/Bertini hypotheses. The normalization and ruled-model square comparison themselves do not require G3 in `B`, G3 in `W`, or exclusion of extra formal branches.
