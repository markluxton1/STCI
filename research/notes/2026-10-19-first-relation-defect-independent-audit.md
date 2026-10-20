# Independent audit: first-relation defects and the effective resultant budget

Date: 2026-10-19.
Reviewer: `saturation_defects/defect_formula_audit`.
Status: **PASS within the exact hypotheses. Reviewed proposal, not a promoted result.**

Proposal audited: [first-relation defect investigation](2026-10-19-first-relation-defect-investigation.md).
No accepted proof, inherited computation, or canonical result record was modified or rerun.

## 1. Exact scope and authority

The setting is an actual locally complete-intersection thickening `Y` of a smooth connected projective curve `C` in a smooth threefold, over an algebraically closed field of characteristic zero, with **unique reduced support** `Y_red=C`. Write `J=I_C O_Y`, `E=N_C^*`, and assume the **full** generic ordinary initial algebra is the coprime binary CI of degrees `2<=r<s`.

The primitive saturation `R` of the actual first relation `K_r` is a line subbundle, but the actual kernel is allowed to be `K_r=R(-D)` for a nonzero effective divisor `D`. This allowance is essential: it prevents direct application of promoted [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) to the entire curve.

The accepted saturated-duality input is the construction and proof in [the filtered-duality note](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md), section 3, as independently checked in [its audit](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md), section 2. That lemma does not require a saturated first relation. It uses actual Gorenstein CM duality, purity, unique support, and generic graded Gorenstein symmetry.

The local exact-order normal-flatness theorem used for the support statement and small-gap conclusion is [the reviewed local theorem](2026-10-19-filtered-generic-ci-normal-flatness.md), with [its separate independent audit](2026-10-19-filtered-local-normal-flatness-independent-audit.md). It remains supporting evidence rather than a separately promoted result record. The new note identifies this authority distinction correctly. Its classical planar Gorenstein Hilbert-function drop input is accepted as stated there; this audit does not re-prove an inherited theorem.

The doubled-positive-divisor lemma is accepted evidence for promoted [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md). The apolar pure-power calculation is accepted evidence for promoted [STCI-R-0009](../results/moving_purepower_boundary.md). The general defect package and its new numerical consequences remain proposals.

## 2. Early saturation and the actual maps

Set `P_i=saturation(J^i in O_Y)` and `B_i=P_i/P_(i+1)`. Accepted saturated duality gives bundles `B_i`, the socle line `S=B_d`, `d=r+s-2`, and perfect pairings `B_i tensor B_(d-i)->S`.

For `j<r`, the generic kernel `K_j` is zero. Since it is a subsheaf of the bundle `Sym^j E`, it is zero everywhere. Thus the ordinary layers through degree `r-1` are vector bundles. Their extensions show that `O_Y/J^i` is CM for `i<=r`, so `P_i=J^i` there. In particular the two exact early identifications needed later really are

    B_(r-1)=Sym^(r-1)E,
    B_(r-2)=Sym^(r-2)E.

No saturation of `K_r` was imported into this step.

For `r<=j<s`, multiplication by a primitive local frame of `R` has constant rank in every binary-form fiber. Therefore `R Sym^(j-r)E` is a subbundle of `Sym^j E`. It has exactly the generic fiber of `K_j`, and hence is its saturation. Multiplication of actual relations gives

    R(-D) Sym^(j-r)E subset K_j subset R Sym^(j-r)E.

Consequently the ordinary torsion is precisely

    tors(J^j/J^(j+1))=(R Sym^(j-r)E)/K_j,

with length `tau_j<=(j-r+1)delta`, where `delta=deg D`.

The primitive relation maps to zero in `B_r` because its image is generically zero and `B_r` is torsion free. Thus it and all its multiples vanish in the saturated graded algebra. This justifies `A_j->B_j` without falsely asserting that `A_j` maps to the ordinary layer. For `j<s`, this is an injection of equal-rank bundles with finite cokernel. At `j=s`, its kernel `T` is a line subbundle: the quotient is its image inside the torsion-free bundle `B_s`.

These map assertions pass. In particular, using `c_s` for the **cokernel** length, rather than for a rank-one kernel or its degree, is necessary for the signs below.

## 3. The sharper first-defect upper budget

Write `d_i=length(P_i/J^i)` and let `c_i` denote the generation-cokernel length. The ordinary-to-saturated exact comparison yields

    tau_i=d_(i+1)-d_i+c_i.

Also `C_i=P_i/(J^i+P_(i+1))` is a quotient of `P_i/J^i`, so `c_i<=d_i`. Since `d_r=0`, it follows that `c_r=0` and

    d_j<=sum_(i=r)^(j-1) tau_i.

For `g=s-r`, this independently gives

    c_(s-1)<=d_(s-1)
             <=sum_(i=r)^(s-2)(i-r+1)delta
              =binom(g,2)delta.

Every step is a statement of finite module lengths at a stalk. The inequality therefore holds both pointwise and after summation. No pointwise resultant-divisor identity is being deduced from it.

## 4. Independent reconstruction of the degree identities

Put `h=deg E`, `a=deg R`, `ell=deg S`, and `c=c_(s-1)`. The exact symmetric-power quotient gives

    deg A_j=r(2j-r+1)h/2-(j-r+1)a.

Pairing `B_(s-1)` with the exact early bundle `B_(r-1)` then gives

    r ell=r(s-1)h-(s-r)a+c.

At degree `s` the exact sequence is

    0 -> T -> A_s -> B_s -> C_s -> 0,

and duality identifies `B_s=(Sym^(r-2)E)^vee tensor S`. In particular

    deg T=deg A_s-deg B_s+c_s
         =s h-(s/r)a-((r-1)/r)c+c_s.

The plus sign on `c_s` is correct. Any actual example must satisfy the resulting integrality conditions.

Local lifts of the quotient relation `T` differ by first-relation multiples. Resultant invariance under such changes gives the section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

The determinant weight `rs` and generator weights `s,r` agree with the homogeneous binary resultant. Generic coprimality makes this section generically nonzero. Its effective zero divisor `Delta` consequently has

    deg Delta=(r-1)c-r c_s>=0.

This proves all three central identities and the advertised upper bound

    deg Delta<=(r-1)binom(g,2)delta.

Only a total-degree identity is asserted. Although determinant sequences also identify the underlying resultant line with a line formed from cokernel divisors, that alone would not identify its particular section with a canonical divisor section. This audit does **not** claim a pointwise equality `Delta=(r-1)C_(s-1)-r C_s`.

## 5. Support and the zero-generation-defect implication

At a point outside `Supp D`, there is an actual order-`r` relation with nonzero special symbol. The reviewed local exact-order theorem therefore makes the entire ordinary normal cone a CI of degrees `(r,s)` in a neighborhood of that point. Its quotient resultant is a unit. Thus `Supp Delta subset Supp D`; the separate local theorem is an explicit dependency.

There is also a useful global consequence. If `c_(s-1)=0`, effectiveness gives `c_s=0` and `deg Delta=0`. Projectivity forces the generic nonzero resultant to be nowhere zero. The quotient relations then define a relative graded CI mapping to `B`. Its top line is `R tensor T tensor(det E)^(-1)` and has the same degree as `S`; the generic top map is a global isomorphism. Perfect fiberwise CI pairings force every graded map to be an isomorphism. Descending induction gives `P_i=J^i` for all `i`, hence all ordinary torsion, all generation defects, and `D` vanish. This uses the same accepted top-socle comparison as R-0010, with the zero-defect degree identities just verified.

This last statement is global and projective. No local vanishing conclusion was inferred merely from a local value of `c_(s-1)` and the global degree formula.

## 6. General nonreduced-root payment

Now restrict to the rational base with balanced conormal, exactly as in the proposal. The full finite-flat root divisor `Z` has class `(epsilon,r)` and retains all multiplicities. The quotient inclusion is adjoint to a section

    sigma of O_Z(-n,s), n=s lambda+deg T.

Generic coprimality makes it invertible on the full generic root algebra, including nilpotents. Since `Z` is a Cartier CM curve with no vertical components, it is a nonzerodivisor. The finite-length zero scheme has length

    s epsilon-r n=deg Delta.

The norm description agrees with the resultant: locally one can choose a direction point avoiding the finite root fiber, write the first form as a monic polynomial, and identify both sections with the determinant of multiplication by the second quotient relation. Changes of these local choices multiply by units.

Write `Z=sum_i m_i D_i`, with reduced integral `D_i` of class `(a_i,b_i)` and `b_i>0`. Restriction of the section to each component is nonzero, so

    rho_i=s a_i-n b_i>=0,
    deg Delta=sum_i m_i rho_i.

For an integral singular component this uses the degree of a line bundle and the finite cokernel of a nonzero section; smoothness of `D_i` is unnecessary.

Suppose `m_i>=2`, `a_i>0`, and `rho_i=0`. The component section would be nowhere zero on `D_i`. Its restriction to the contained subscheme `2D_i` is then a unit by the local unit criterion modulo a nilpotent ideal. It would trivialize `O(-n,s)|_(2D_i)`. The accepted doubled-positive-divisor Picard injectivity lemma used by R-0011 forbids this because `s>0`. Therefore such a component has `rho_i>=1` and contributes at least `m_i` to `deg Delta`.

A repeated constant component has `a_i=0`, hence `n<=0` by nonnegativity of `rho_i`. If the full root moves (`epsilon>0`), this yields `deg Delta>=s epsilon`, which is at least three under `s>r>=2`. Thus every moving nonreduced full root indeed satisfies `deg Delta>=2`, whether its repeated components move or remain constant. This distinction was tested explicitly and is handled correctly.

The result constrains repeated components of the **total root divisor**. It does not exclude a reduced total root with nonreduced special fibers.

## 7. Pure-power strengthening

For `R=(H^-1 M)^r` and `deg M=-e<0`, the accepted characteristic-zero apolar formula makes `A_s` a constant rank-`r` bundle tensored with a line of degree `-s lambda+(g+1)e`. A nonzero map from the kernel line `T` to this bundle gives

    deg T<=-s lambda+(g+1)e.

Substituting the independently verified degree of `T` gives

    ((r-1)/r)c-c_s>=(r-1)e,
    deg Delta>=r(r-1)e.

This is also consistent with the exact divisor identity for a pure power: locally `Res(m^r,g)=Res(m,g)^r`, so `Delta` is `r` times the evaluation zero divisor. Consequently the left side of the first inequality is an actual integer divisor degree in this case, not merely a rational numerical expression.

The inequalities `c>=r e` and, when its denominator is nonzero, `delta>=r e/binom(g,2)` follow. They are necessary conditions; no ambient construction or unrestricted STCI exclusion follows.

## 8. Small gaps, the local example, and one qualification

Let `q` be the first ideal order of any transverse planar special fiber. Purity gives `q>=r`. The accepted drop-at-most-one theorem, starting with `1,2,...,q`, forces a tail of total size at least `q(q-1)/2`; hence every such fiber has length at least `q^2`. Its length is the generic length `rs`, so

    r<=q<=floor(sqrt(rs)).

For `s-r<=2`, `rs<(r+1)^2`, forcing `q=r` everywhere. The reviewed local exact-order theorem then gives normal flatness without initially assuming saturation. This argument also permits `r=s` under the equal-degree scope of that separate local theorem. It does not extend the distinct-degree resultant construction to equal degrees.

The proposed local counterexample also passes: the algebra

    k[[t,x,y]]/(x^a-t y^r, y^(q r)), a>r>=2, q>=2,

has a finite free basis `x^i y^j`, `0<=i<a`, `0<=j<q r`. Over `k((t))` its ideal equals `(y^r-t^-1 x^a,x^(a q))`, whose coprime leading forms give the full generic initial CI of degrees `(r,a q)`. Its actual order-`r` kernel is generated by `t y^r`, so the first saturation defect has length one. The special fiber has first order `min(a,q r)>r`. The example demonstrates local defects and is correctly not presented as a projective C0 construction.

The subsequently supplied sharper example at gap three passes as well. Put

    F=t x y+x^3+y^4, G=x y^2,
    A=k[[t,x,y]]/(F,G).

The exact identity

    t^2 G+(x^2-t y)F=x^5-t y^5+x^2 y^4=:H

shows `(F,G)=(F,H)` over `k((t))`. Their initial forms there are `t x y` and `x^5-t y^5`, which are coprime. Thus the **full** generic initial ideal is a binary CI of degrees `(2,5)`. Every prime containing `(F,G)` contains `x` or `y` by `G`, then both by `F`, so the reduced support is precisely the `t`-axis. Height two gives an actual CI; its CM quotient has `t` regular and is finite free over `k[[t]]`. The special intersection multiplicity is

    i(x^3+y^4,x y^2)=i(x^3+y^4,x)+2i(x^3+y^4,y)
                    =4+2*3=10,

agreeing with generic length `2*5`. The actual degree-two kernel is generated by `t x y`, of saturation colength one, while the special first order is three. Thus the threshold `g>=3` cannot be improved solely under these local hypotheses. This remains a local example.

The proposal's additional exact filtration certificate also checks. The ten listed elements span using `x^3=-txy-y^4`, `xy^2=0`, and `y^6=0`; the verified free rank ten makes them a basis. Direct multiplication gives

    J^3=<txy,x^2y,y^3,y^4,y^5>,
    J^4=<t x^2y,y^4,y^5>, J^5=<y^5>, J^6=0.

For example `x^3y=-y^5`, `x^4=-t x^2y`, and `x^5=t y^5` give all remaining degree-four and degree-five products. Their saturations are

    P_3=<xy,x^2y,y^3,y^4,y^5>,
    P_4=<x^2y,y^4,y^5>, P_5=<y^5>.

Thus `B_3` has basis `xy,y^3` and its ordinary-symbol image is generated by `txy,y^3`; `B_4` has basis `x^2y,y^4` with image `t x^2y,y^4`. It follows that `c_3=c_4=1` and `c_2=c_5=0`, exactly as stated. The resultant of `xy` and `x^5-t y^5` is a unit times `t`, so has a simple zero. The special and generic Hilbert functions are respectively `(1,2,3,2,1,1)` and `(1,2,2,2,2,1)`.

The initial audit requested one denominator qualification: `r e/binom(g,2)` is undefined at `g=1`. The proposal now explicitly restricts that quotient inequality to `g>=2` and treats `g=1` by the contradiction `c=0` against the pure-power lower bound. This presentation issue has been fixed; no unresolved qualification remains.

## 9. Verdict and retained frontier

The exact kernel/saturation maps, sharper upper budget, corrected socle identity, second quotient-line degree, effective resultant degree, full-root payment, pure-power strengthening, small-gap consequence, and exact gap-three filtration example pass independent reconstruction. The denominator qualification identified during review has been incorporated in the proposal.

The note still concerns actual lci thickenings with unique smooth support and a **full generic coprime binary CI** initial algebra. Generic initial ideals with additional generators, intersections with residual reduced components, reduced-root ambient lifting, and global realization of defective models are not settled. No finite computation, local example, vertical exceptional feature, or new necessary inequality is equated with a global existence or nonexistence theorem. The package remains a reviewed proposal pending the repository's canonical promotion procedure.
