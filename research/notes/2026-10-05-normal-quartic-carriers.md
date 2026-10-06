# Normal quartic carriers: rational singularities are already excluded

Started: 2026-10-05; extended: 2026-10-06. Lane: normal quartic surfaces
in characteristic zero. Status: classical uniform exclusion recovered and
checked; additional normal-carrier reduction and simple-elliptic subclass
exclusion proved below. This note does not address nonnormal quartics, nor
pairs with minimum carrier degree greater than four.

Let `C` be a smooth nondegenerate rational quartic, in particular
`C0=[s^4:s^3t:st^3:t^4]`. Suppose an integral normal quartic `S` and a
surface `T` meet set-theoretically in `C`. There is no restriction on `deg T`
or on common singular points.

## 1. A stronger classical theorem than the planned ADE enumeration

David B. Jaffe, [Applications of iterated curve blowup to set theoretic
complete intersections in P^3](https://arxiv.org/pdf/alg-geom/9410008),
Theorem 11.11, printed p.45 (PDF page index 44), proves that a smooth
set-theoretic intersection on a quartic surface with only rational
singularities is linearly normal. The introduction, printed p.2,
explicitly allows an arbitrary second surface and common singular points.

The hypothesis is substantially different from Jaffe's
no-common-singular-point theorems. It must not be omitted when listing the
known quartic-carrier frontier. Since `h^0(C,O_C(1))=5` whereas ambient
linear forms have dimension four, every smooth rational quartic violates
the conclusion. Thus **a normal quartic carrier with only rational
singularities is excluded for every mate degree**.

A normal hypersurface surface with rational singularities is Gorenstein,
so these singularities are rational double points. The theorem therefore
already covers every normal ADE quartic. A new lattice scan of that class
would reproduce a classical exclusion, rather than advance the frontier.

Jaffe states the theorem over the complex numbers. All assertions in this
note extend to an arbitrary algebraically closed characteristic-zero field
by finitely generated coefficient-field transfer. For precision, descend
the equations of the hypothetical pair, a parametrization of the smooth
rational quartic, and a resolution together with its exceptional divisors
to a sufficiently large finitely generated field `k0` of characteristic
zero. Geometric normality and smoothness can be retained after increasing
`k0`. The two ideal containments expressing radical equality have finite
polynomial witnesses: powers of generators of `I_C` belong to `(F,G)`, and
`F,G` belong to `I_C`. Include those witnesses in `k0` as well. Embed `k0`
in the complex numbers and base change. This preserves the set-theoretic
intersection, the resolution, intersection numbers, exceptional curve
genera, and the rational/simple-elliptic hypotheses being used. The
complex result then supplies the contradiction. Thus no uncountability
assumption on the original field is needed.

## 2. The complete normal quartic classification narrows the survivors

Yuji Ishii and Noboru Nakayama,
[Classification of normal quartic surfaces with irrational singularities,
J. Math. Soc. Japan 56 (2004), 941–965](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf),
give constructions of all such surfaces. The
[author-hosted preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf)
is particularly convenient for its readable extraction and page numbering.
The published Main Theorem, p.955, confirms that the constructions are
exhaustive, so the argument below does not infer a classification from
examples alone. Its introduction lists four possibilities for the resolution:
K3, a bundle over a smooth plane quartic (the cone case), an elliptic ruled
surface, or a rational surface.

For the non-K3 cases, write `sigma:M→S`, `H=sigma^*O_S(1)` and
`K_M=-E`, where `E` is a nonzero effective exceptional anticanonical
divisor. Their condition C includes `H∩E=empty`. Their exhaustive
construction shows:

- Cone case: `M` is a bundle over a curve of genus three and `H` has degree
  one on its ruling fibers.
- Elliptic ruled case (Type C): the general ruling fiber has `H`-degree two
  or three. See preprint §3.3, printed pp.30–34, together with §2.3.
- Rational case: Picard number is 12 for Type B1, 11 for B2 and B3, and
  13 for Type D. See preprint printed pp.14, 17, 19 and 23.

Any rational curve on a surface ruled over a positive-genus curve maps
constantly to the base. Its strict transform is therefore an irreducible
component of a fiber. Because `H` is nef, its `H`-degree is at most the
degree of the whole fiber, which is at most three in these cases.
Consequently **the cone and elliptic ruled normal quartics cannot even
contain a rational curve of degree four**. This statement uses the
classification and elementary intersection theory, independently of a
mate.

It follows that a surviving normal quartic STCI carrier has rational
minimal resolution, contains a nonrational singularity, and has
`rho(M)≤13`.

## 3. New reduction: the quartic must pass through a nonrational singularity

Suppose, for contradiction, that `C` avoids every nonrational singularity
of such a rational normal quartic. Let `c` be its strict transform in `M`.
It is again a smooth rational curve: the blowup centers restrict to
invertible ideals on the smooth support, and the strict-transform map is
an isomorphism. Since `E` lies over the nonrational singularities,
`c.E=0`. Adjunction gives `c^2=-2`.

The divisor of the mate on `S` is `bC`, where `b=deg T`, because both
`S` and `C` have degree four. Thus `bC~bH` on `S`. Its numerical pullback
to `M` gives

`c+Z ≡ H`,

where `Z` is the effective rational exceptional correction. It is supported
only at rational double points on `C`. Orthogonality to each exceptional
curve gives `c.Z=-Z^2`; hence

`Delta := -Z^2 = H^2-c^2 = 4-(-2)=6`.

Let `N` be the total ADE root rank at these points. Jaffe's classification
of smooth curve–rational double point pairs (Theorem 4.1 and Proposition
5.7, printed pp.15 and 23) gives the following local contributions:

| Pair | Root rank | Contribution to Delta |
|---|---:|---:|
| `A_n^k`, `1≤k≤(n+1)/2` | `n` | `k(n+1-k)/(n+1)` |
| `D_n^1` | `n` | `1` |
| `D_n^n` | `n` | `n/4` |
| `E_6^1` | `6` | `4/3` |
| `E_7^1` | `7` | `3/2` |

Every contribution is at most half its root rank. For the `A_n` row,
the quadratic's maximum is `(n+1)/4≤n/2`; the other rows are immediate.
Therefore `Delta≤N/2`.

The ADE exceptional curves above points on `C` are linearly independent
by their negative definite intersection matrix. At least one further
exceptional dimension is supplied by the nonzero anticanonical divisor
`E`, whose support lies above distinct points and whose square is negative.
All these classes are orthogonal to `H`, and `H^2=4`. Thus

`N+1≤rho(M)-1≤12`, so `N≤11`.

We obtain `6=Delta≤11/2`, a contradiction.

**Conclusion.** A normal quartic surface occurring in a characteristic-zero
STCI presentation of a smooth rational quartic must have rational minimal
resolution and the quartic curve must pass through a nonrational
singularity. Normality alone is not an exclusion. No assertion is made
that every quartic carrier is normal, or that the remaining nonrational
points are ADE.

## 4. New bounded exclusion: a smooth elliptic exceptional curve

Assume the anticanonical exceptional divisor `E` is a single smooth,
reduced elliptic curve. This hypothesis specifies the surviving
nonrational singularity as a **simple elliptic singularity**; all other
singularities are rational double points. This section proves that no
normal quartic with this property can be an STCI carrier for a smooth
rational quartic, for any mate degree.

By §3 the curve passes through the simple elliptic point. Put
`d=-E^2`. The exhaustive rational-resolution classification gives

| `d` | Possible rational type | `rho(M)` | ADE rank upper bound `N` |
|---:|---|---:|---:|
| 1 | B2 or B3 | 11 | 9 |
| 2 | B1 | 12 | 10 |
| 3 | D | 13 | 11 |

The rank bound follows from the independence of `H`, `E`, and the ADE
exceptional curves, just as in §3. For a smooth elliptic `E`, its fiber is
the full exceptional locus of the simple elliptic singularity: a further
minimal exceptional curve of discrepancy zero attached to `E` would have
`K_M.R=-E.R<0`, contradicting minimality. Other connected exceptional
fibers are disjoint ADE configurations.

### Local passage and first-normal orders from a checked classification

Guangfeng Jiang and Dirk Siersma,
[Local embeddings of lines in singular hypersurfaces, Ann. Inst. Fourier
49 (1999), 1129–1147](https://www.numdam.org/item/10.5802/aif.1711.pdf),
§3.7, Theorem and Table 3 on p.1141, classify every smooth
curve–simple elliptic hypersurface pair. Here their local “line” means a
smooth curve germ, straightened to the `x`-axis by an analytic coordinate
change (§1.1). Their invariant `lambda` is the length of the Jacobian
restricted to that axis (§2.3–2.4). Since the tangential derivative
vanishes on the support, it is exactly the common vanishing order `s` of
the two first-normal coefficients.

The following entries of Table 3 were checked visually against the PDF;
the omitted coefficient restrictions are its nondegeneracy conditions.

| Type | Pair normal form, support `y=z=0` | weights `(x,y,z)` | `s` |
|---|---|---|---:|
| `tilde E6` | `x^2 y+a0 x z^2+a1 y^3+a2 y^2 z+a3 y z^2+a4 z^3` | `(1,1,1)` | 2 |
| `tilde E7` | `x^2 z+x^3 y+b x^2 y^2+c x y^3+d0 y^4+z^2` | `(1,1,2)` | 2 |
| `tilde E7` | `x y (x-y)(x-nu y)+z^2`, `nu≠0,1` | `(1,1,2)` | 3 |
| `tilde E8` | `x^3 z+gamma x^2 y^2+delta x^4 y+y^3+z^2` | `(1,2,3)` | 3 |
| `tilde E8` | `alpha x^4 y+x^2 y^2+y^3+z^2`, `alpha≠0,1/4` | `(1,2,3)` | 4 |

The weight of the support parameter `x` is one in every row. In the
weighted `x`-chart put `y=x^(w_y)Y`, `z=x^(w_z)Z`. Factoring the weighted
degree leaves an equation `P(Y,Z)=0`, while the support is `Y=Z=0` and
the exceptional curve is `x=0`. At `(Y,Z)=(0,0)`, `P_Y` or `P_Z` is
nonzero: the five rows respectively have a linear `Y`, a linear `Z`, a
linear `Y`, a linear `Z`, and a linear `alpha Y`. The surface and its
exceptional elliptic curve are smooth in this chart, and the strict
transform of the support meets it transversely with parameter `x`.

This chart belongs to the simple elliptic resolution. In these weighted
forms the exceptional weighted-projective elliptic curve has degree
`d=3,2,1` respectively, and the normal bundle has degree `-d`. It misses
the ambient weighted-projective quotient points because their pure
`y` or `z` terms do not vanish there. Thus the weighted blowup introduces
no extra exceptional component at the support point. Equivalently, the
unique minimal elliptic exceptional curve meets the support once. We have
proved the local data

`c.E=1`, and `s≥3` if `d=1`, while `s≥2` if `d=2` or `3`.

### A quartic supplies at most nine first-normal zeros

For a smooth rational quartic in characteristic zero,
`N_C^*=O_P1(-7)^2`. The differential of its quartic carrier gives

`O_P1(-16)→O_P1(-7)^2`.

It is a nonzero pair of binary forms of degree nine. Their greatest
common divisor has degree at most nine, and this degree is the sum of
the local first-normal orders over the singular points of the surface on
`C`. Thus the sum `P` of the ADE first-normal orders satisfies

`P≤6` for `d=1`, and `P≤7` for `d=2,3`.

This bound does not require a regular first-normal quotient between the
two defining surfaces or any bound on the mate degree. It uses only the
normal quartic carrier's differential. In the repository's notation its
degree is `9-e`; the weaker bound at most nine is sufficient here.

### The exact harmonic ADE bound

For a smooth curve through an ADE point, let `n` be its root rank,
`s` its first-normal order, and `delta` its contribution to the numerical
pullback correction. Jaffe's Propositions 5.2 and 5.7 give

| Pair | `s` | `delta` |
|---|---:|---:|
| `A_n^k` | `k` | `k(n+1-k)/(n+1)` |
| `D_n^1` | 2 | 1 |
| `D_n^n`, `n` even | `n/2` | `n/4` |
| `D_n^n`, `n` odd | `(n-1)/2` | `n/4` |
| `E_6^1` | 2 | `4/3` |
| `E_7^1` | 3 | `3/2` |

Every row satisfies `delta≤n s/(n+s)`. In the `A_n` row, after cancelling
positive factors the inequality is `k(1-k)≤0`. For the spin `D_n` row it
is `n≤3s`, true for the permitted `n`; the remaining three rows are
immediate. Summing and applying Cauchy–Schwarz gives

`sum delta ≤ sum n_i s_i/(n_i+s_i) ≤ N P/(N+P)`,

where `N=sum n_i` and `P=sum s_i`. One proof of the second inequality is
to write the middle sum as `N-sum n_i^2/(n_i+s_i)` and use
`sum n_i^2/(n_i+s_i)≥N^2/(N+P)`. When there are no ADE points the
correction is zero, with no denominator needed.

### Contradiction

Adjunction now gives `c^2=-1`, because `K_M=-E` and `c.E=1`.
The STCI relation still gives numerical pullback `c+Z≡H`, so the whole
correction is `-Z^2=4-c^2=5`. At the simple elliptic point, orthogonality
forces `Z_ell=E/d`, contributing `1/d`. Hence the ADE correction must
equal `5-1/d`.

The necessary correction exceeds its permitted harmonic upper bound
in every row:

| `d` | Required ADE correction | Upper bound | Exact positive gap |
|---:|---:|---:|---:|
| 1 | 4 | `9·6/(9+6)=18/5` | `2/5` |
| 2 | `9/2` | `10·7/(10+7)=70/17` | `13/34` |
| 3 | `14/3` | `11·7/(11+7)=77/18` | `7/18` |

The function `NP/(N+P)` is increasing in each nonnegative variable,
so using the rank and first-normal upper bounds is legitimate. These
strict inequalities contradict the mate relation. This proves the
claimed uniform simple-elliptic subclass exclusion.

Exact companion verification:
`research/computations/verify_normal_quartic_simple_elliptic.py`, run with
`/private/tmp/stci-cas-venv/bin/python`, checks the weighted homogeneity,
axis differential orders and smooth weighted charts of all five local
pair forms, 53 permitted ADE rows of rank at most 11, and the three strict
rational gaps. It returned `PASS`. The saved output is
`research/computations/normal_quartic_simple_elliptic_2026-10-06.json`.
The script checks formulas, not the classification theorems or the
geometric deductions; those hypotheses remain explicit in this proof.

## 5. Continuation boundary

The classification leaves rational-resolution Types B1, B2, B3 and D,
with effective exceptional anticanonical divisor of square respectively
`-2,-1,-1,-3`. Section 4 removes the smooth reduced elliptic `E` case.
Reducible, singular, or nonreduced `E` and its associated nonrational
singularities must be retained. A promising next bounded move is to combine
the numerical pullback `c+Z≡H`, anticanonical intersection `c.E`, the full
local Cartier-order condition, and the first-normal singularity length
`9-e`, `e≤2`, at the point actually lying on `C`. The local correction
cannot be inferred just from an ADE tangent type at that point.

The ADE total-correction calculation `Delta=6` is classical in the all-ADE
case (also Ellia 2014, Lemma 11). Here it is used only when `C` avoids
the nonrational points, so `c.K_M=0`; it is invalid if `c.E>0`.

Read-only primary-source PDF download:
`/private/tmp/stci-normalquartic-rims1370.pdf`;
text extraction: `/private/tmp/stci-normalquartic-rims1370.txt`.
These temporary files are convenience copies, not the durable evidence
record. Exact paper URLs and section/page references above are the
continuation references.
