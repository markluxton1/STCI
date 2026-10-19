# Independent adversarial audit: saturated first relation and normal flatness

Date: 2026-10-19.
Reviewer: independent normal-flatness adversarial worker.
Outcome: **PASS for the exact theorem below.** This is independent proof
review evidence, not canonical promotion. No accepted mathematics or
canonical record was edited.

## Exact scope and evidence

Let `k` be algebraically closed of characteristic zero, let `C` be a
smooth connected projective curve regularly embedded with codimension
two in a smooth threefold `X`, and let `Y` be an actual lci thickening
with `Y_red=C`. Write `J=I_C O_Y` and `E=N_(C/X)^*`. Suppose the FULL
generic ordinary initial algebra is

    gr_(J_eta)(O_(Y,eta))=k(C)[x,y]/(f_r,g_s),
    2<=r<s,                         gcd(f_r,g_s)=1,

and the ACTUAL kernel

    R=ker(Sym^r E -> J^r/J^(r+1))

is a line subbundle of `Sym^r E`. Then every ordinary layer
`J^i/J^(i+1)` is locally free on `C`, and its full graded algebra in
every fiber is a binary graded complete intersection of degrees `(r,s)`.
No splitting or balance of `E` is assumed.

Source statement and resultant proof: section 8 of
[the spectral bridge proposal](2026-10-19-saturated-first-relation-spectral-bridge.md).
The ordinary-power recovery is also detailed in its sections 3 and 6.
The saturation-duality proof is section 3 of
[the filtered-duality proposal](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).
Both sources remain proposals; this audit supplies independent review
of this theorem alone and does not certify other conclusions in them.

## Independent reconstruction

Put `d=r+s-2`. Since `O_Y` is Cohen--Macaulay with sole reduced support
`C`, it has no finite-support subsheaf; hence generic vanishing gives
`J^(d+1)=0` globally. Let `P_i` be the saturation of `J^i` in `O_Y`.
These ideals are multiplicative; the quotients `O_Y/P_i` are MCM, and
`B_i=P_i/P_(i+1)` are torsion-free coherent `O_C`-modules, thus vector
bundles. In particular `P_1=J`. The same argument makes
`S=Ann_Y(J)` a rank-one bundle on `C`.

The generic annihilator identity needs an actual justification beyond
the words "graded Gorenstein." In the generic Artin Gorenstein algebra
`A`, the containment

    (J_eta)^(d+1-i) subset Ann_A((J_eta)^i)

holds by nilpotence. Gorenstein duality gives the length of its right
side as `length(A/(J_eta)^i)`. Symmetry of the generic graded CI Hilbert
function makes this equal the length of its left side. Thus the
containment is equality. Both global annihilators and the `P_i` are
saturated, so

    Ann_Y(P_i)=P_(d+1-i).

Dualizing
`0 -> B_i -> O_Y/P_(i+1) -> O_Y/P_i -> 0` over the one-dimensional
Gorenstein ring `O_Y` is exact because the last term is MCM and its
local `Ext^1(-,O_Y)` vanishes. The annihilator identities identify the
resulting quotient with `B_(d-i)`. Since maps from `B_i` land in `S`,
this gives the perfect pairing

    B_(d-i)=Hom_C(B_i,S)

by actual multiplication. No retraction to `C`, or ordinary-layer
flatness, enters this step.

For `j<r`, the actual relation kernel has generic rank zero and is a
subsheaf of the bundle `Sym^j E`, hence is zero. For `r<=j<s`, the
product `R tensor Sym^(j-r)E` is a subbundle: multiplication by the
nonzero binary form in each fiber is injective with constant rank.
The actual kernel contains it and has the same generic rank. The
quotient is a torsion subsheaf of the locally free quotient by this
product and must vanish. Consequently all ordinary layers through
`s-1` are bundles, and `P_i=J^i` for `i<=s`.

Write `h=deg E`, `a=deg R`, and `ell=deg S`. The first-relation quotient
`A_j` for `j>=r-1` has rank `r` and degree

    deg A_j=(r*j-r*(r-1)/2)*h-(j-r+1)*a.

The perfect pairing of `B_(r-1)` and `B_(s-1)` therefore gives

    ell=(s-1)*h-(s-r)*a/r.

Because `P_s=J^s`, the map `A_s -> B_s` is surjective, with
`B_s=(Sym^(r-2)E)^* tensor S`. Its kernel `T` is a line subbundle and

    t=deg T=s*h-s*a/r.

Locally lift the quotient generator of `T` to a degree-`s` polynomial.
Adding a multiple of the first polynomial leaves its binary resultant
unchanged. The local resultants therefore glue even when this lift
does not split globally. Their generator-scaling exponents `s,r` and
normal-frame determinant weight `rs` give the resultant section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

Its degree is `rs*h-s*a-r*t=0`; its generic value is nonzero precisely
by generic coprimality. A nonzero section of a degree-zero line bundle
on the smooth connected projective curve has no zero divisor. Hence
the two local polynomial generators are coprime in EVERY fiber.
The criterion retains repeated roots and nonreduced first-root fibers.

Use `R` and the full degree-`s` preimage of `T` to form the graded
quotient `D` of `Sym(E)`. The local generators have transition
`f' = u*f`, `g' = v*g+q*f`, so their ideals glue without a global
second-generator splitting. Fiberwise coprimality implies that `D` is
a finite locally free graded CI family with top line

    D_d=R tensor T tensor (det E)^(-1).

The natural algebra map `D -> B` is generically an isomorphism and
`deg D_d=a+t-h=ell=deg B_d`. Its top map is thus an isomorphism of
line bundles. At any closed point, a nonzero element in the kernel of
`D_i -> B_i` would pair with some element of `D_(d-i)` to a nonzero
top element, by the perfect CI multiplication pairing in the fiber of
`D`. Algebra-map compatibility would kill that top element, contradicting
the top isomorphism. Thus every graded map is fiberwise injective and,
by equal ranks, an isomorphism of bundles.

Finally `B` is generated in degree one, so actual multiplication gives
`P_i=J^i+P_(i+1)`. Descending from `P_(d+1)=0` proves `P_i=J^i` for
all `i`. This recovers the ORDINARY filtration, rather than proving
only a statement about its saturation.

## Adversarial tests and boundaries

* **Base change:** no ordinary fiber kernel is identified by an
  unjustified base-change operation. Before flatness is proved, the
  argument uses the saturated vector bundles `B_i` and the actual
  sheaf kernels. Fiberwise arguments only occur for those bundles and
  the everywhere-CI family `D`.
* **Nonsplit generators:** only the line quotient `T` is global. The
  resultant and top-line formula are invariant under triangular
  changes of its local lifts.
* **Special support and purity:** no extra reduced component is
  allowed. With residual components present, generic vanishing along
  `C` would not imply global vanishing, and the proof would not apply.
* **Displayed symbols:** coprime displayed leading terms are
  insufficient unless they give the FULL generic initial ideal. Its
  exact symmetric Hilbert function is used in both annihilator
  equality and every graded-rank comparison.
* **Saturation:** a generically nonzero first form alone does not make
  first-relation multiples a subbundle. The actual line-subbundle
  hypothesis is used before any degree argument.
* **Projectivity:** generic nonzero resultant plus degree zero removes
  all special degenerations on the projective curve. This review
  neither silently extends this argument to an affine base nor claims
  that projectivity is necessary in every alternative proof.

No counterexample or proof blocker was found under the stated
hypotheses. There is no unresolved mathematical dependency in this
reconstructed proof beyond the standard local duality and graded CI
facts explicitly used above. Canonical promotion is a separate review
and metadata action. The equal-degree case, nonsaturated first
relations, non-CI generic tangent cones, residual components, and the
unrestricted STCI question remain outside this audit.
