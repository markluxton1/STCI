# Normal singularities, primitive cubic carriers, and ancestor charts

The normal-surface arguments below retain their broader smooth rational
quartic scope, including an independent weighted simple-elliptic proof.
The primitive calculations use the fixed C0 and provide explicit cubic
carriers, higher-extension controls and exact ancestor chart equations.
These are distinct statements: the completed [fixed-C0 all-quartic proof](../synthesis/quartic_carrier_proof.md)
does not make the broader normal-curve arguments or ancestor equations
redundant.

---

## Numerical self-intersection and the normal line

The full proof, ordinary-node correction, unbounded Cartier-index control,
and conditional split-sextic application now have one mathematical home:
[numerical pullback and the normal line](../synthesis/numerical_surface_pullback.md).
The inequality for an integral surface regular generically along the smooth
curve was independently reconstructed in this consolidation. Its special
split-sextic numerical antecedents remain conditional.

---

<a id="2026-10-05-normal-quartic-carriers"></a>

## Normal singularities and smooth rational quartics

Work with normal quartic surfaces in characteristic zero. The classical
rational-singularity exclusion, the passage-through-nonrational-points
reduction, and the smooth elliptic exceptional-curve exclusion below
are proved for the displayed smooth rational quartic scope. They do
not treat nonnormal quartics or higher minimum carrier degree.

Let `C` be a smooth nondegenerate rational quartic, in particular
`C0=[s^4:s^3t:st^3:t^4]`. Suppose an integral normal quartic `S` and a
surface `T` meet set-theoretically in `C`. There is no restriction on `deg T`
or on common singular points.

### 1. Jaffe's rational-singularity theorem

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

### 2. The complete normal quartic classification narrows the survivors

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

### 3. Passage through a nonrational singularity

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

### 4. A smooth elliptic exceptional curve

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

#### Local passage and first-normal orders from a checked classification

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

#### A quartic supplies at most nine first-normal zeros

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

#### The exact harmonic ADE bound

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

#### Contradiction

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
`research/computations/verify_normal_quartic_simple_elliptic.py`, run with `python3`, checks the weighted homogeneity,
axis differential orders and smooth weighted charts of all five local
pair forms, 53 permitted ADE rows of rank at most 11, and the three strict
rational gaps. It returned `PASS`. The saved output is
`research/computations/normal_quartic_simple_elliptic_2026-10-06.json`.
The script checks formulas, not the classification theorems or the
geometric deductions; those hypotheses remain explicit in this proof.

### 5. Scope of the normal arguments

The rational-resolution classification allows effective exceptional
anticanonical divisors of square -2,-1,-1,-3 in Types B1,B2,B3,D.
The weighted proof above handles the smooth reduced elliptic case.
Its local pair table and exact first-normal orders are a distinct
proof from the [common fixed-C0 normal-carrier proof](../synthesis/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing),
which completes the reducible, singular and nonreduced cases for
that fixed embedding. The broader smooth-rational-quartic statements
in Sections1--4 retain exactly their stated hypotheses.

The ADE correction identity Delta=6 is used here only when the curve
avoids the nonrational points, so c.K_M=0. It is invalid when c.E>0;
the later smooth elliptic calculation instead uses its actual
c.E=1, weighted first-normal order and elliptic correction1/d.
Neither equality follows from an ADE tangent type alone.

The surface classification and local analytic pair table above are
characteristic-zero inputs. They do not establish the same cases in
positive characteristic. The exact polynomial identities have their
own reduction scope after denominators and bad-prime rank changes are
checked; this is separate from transporting those classification
hypotheses. In particular, fixed C0 has quartic-carrier mates in
[every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

---

<a id="2026-10-05-primitive-carrier-theory"></a>

## Explicit cubic carriers for the primitive fourth locus

Scope: characteristic zero and the fixed monomial smooth
rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

This note independently reconstructs the geometric meaning of the
degree-two primitive-fourth zero locus and the quartics carrying its
canonical primitive triple. The universal primitive-fourth obstruction
calculation is recorded separately by the primitive-quadruple investigation.
Its vanishing locus, on the open set of coprime binary quadratic pairs, is
the linear locus used below. No primitive multiple curve constructed here
is asserted to be a global complete intersection.

### 1. Frames, obstruction degrees, and the factorization of the quadratic jet

On the first affine chart write

\[
z=t/s,\quad a=x_2/x_0-z^3,\quad b=x_3/x_0-z^4,
\quad u=b-\frac32za,\quad v=a.
\]

The split conormal frame has transition \(u'=z^{-7}u\),
\(v'=z^{-7}v\) to first order. A quotient to \(L=O(-5)\) is specified
by a coprime pair of binary quadratics, written on this chart as

\[
u\longmapsto A(z),\qquad v\longmapsto B(z).
\]

Its kernel is \(M=O(-9)\). Consequently

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6),\qquad
\operatorname{Hom}(M,L^4)=O(-11).
\]

Both cohomology groups of \(O(-1)\) vanish. Thus each quotient has a
unique embedded primitive triple, with no free extension parameter. The
next two obstruction spaces have dimensions five and ten respectively.

Let \(D=A'B-AB'\), where primes denote ordinary differentiation in \(z\).
The moving-coordinate calculation in
`research/scratch/primitive47/obstruction.py` gives the following
Bezout-independent expression for its quadratic cocycle:

\[
\boxed{
h_2=-\frac{2A+zB}{8z^5}
       \left(12A^2+3z^2B^2+4z^2D\right).
}
\]

Indeed the first displacement of the opposite affine coordinate is

\[
W_1=-z^{-5}A-\frac12z^{-4}B.
\]

The quadratic ambient jets are

\[
u'_2=-\frac52z^{-11}A^2-3z^{-10}AB-\frac38z^{-9}B^2,
\quad
v'_2=3z^{-12}A^2-z^{-11}AB-\frac94z^{-10}B^2.
\]

Using \(b_V'(1/z)A-a_V'(1/z)B=D\), and multiplying the quadratic
coefficient of \(b_V(W)u'-a_V(W)v'\) by \(z^9\), proves the boxed
formula. In particular, this calculation retains the displacement of the
base coordinate; fixing \(W=1/z\) would omit its final summand.

Write \(\gamma_U\) for the nonnegative Laurent part of \(h_2\). With
\(m=Bu-Av\), the first-chart primitive-triple equation is

\[
m+\gamma_U\ell^2=0\pmod{\ell^3}.
\]

### 2. A distinguished cubic on the fourth-obstruction zero locus

The separately computed universal fourth-obstruction vanishing locus is

\[
A=a_0+a_1z+a_2z^2,\qquad
B=-2a_1-2a_2z+b_2z^2.
\]

Define

\[
q_0(z)=2A+zB=2a_0+b_2z^3.
\]

The homogeneous resultant on this locus is

\[
a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, coprimality implies \((a_0,b_2)\ne(0,0)\), so
\(q_0\) is a nonzero section of \(O(3)\).

Use ambient coordinates \([x:y:Z:W]\), and set

\[
Q=xW-yZ,\quad
R_1=x^2Z-y^3,\quad
R_2=xZ^2-y^2W,\quad
R_3=yW^2-Z^3.
\]

The distinguished cubic is

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
  +a_0^2R_1+a_0b_2R_2-\frac{b_2^2}{4}R_3.
}
\]

It lies in \(I(C_0)_3\), and its first conormal symbol in the split
\((u,v)\) frame is

\[
\sigma_1(T)=-\frac{q_0}{2}(B,-A).
\]

Here is an elementary uniqueness derivation. The cubic first symbols have
the form

\[
P=c_0+c_1z-c_5z^2+c_2z^3+c_3z^4+2c_6z^5,
\]

\[
Q_{
m n}=c_4+\frac12c_0z+\frac12c_1z^2
                 +\frac12c_5z^3+\frac12c_2z^4+\frac12c_3z^5,
\]

so \(Q_{
m n}-zP/2=c_4+c_5z^3-c_6z^6\). A symbol proportional to
\((B,-A)\) therefore has a scalar of degree three proportional to
\(q_0\). Equating coefficients gives the displayed cubic. This also
covers \(a_0=0\) or \(b_2=0\) individually: the other coefficient is
nonzero on the coprime locus. Thus the cubic with this conormal direction
is unique up to scalar.

The boxed quadratic-cocycle formula verifies directly that \(T\) contains
the canonical primitive triple. Substituting \(u=A\ell,v=B\ell\) gives
zero constant and linear coefficients for \(T\); its quadratic
coefficient is \(-q_0\gamma_U/2\). The correction
\(m=-\gamma_U\ell^2\) contributes the opposite coefficient, because
the first symbol of \(T\) is \(-q_0m/2\).

### 3. Every quartic containing this triple is a cubic multiple

The exact quartic-symbol image is independently verified in
`research/computations/verify_localcoh_direction_image.py`:

\[
Q_{{\rm n},2}=P_1/2,\quad
Q_{{\rm n},5}=P_4/2,\quad
Q_{{\rm n},8}=P_7/2,
\]

and the kernel of the symbol map is \(kQ^2\). On the present degree-two
direction locus, a quartic symbol has the form \(h(B,-A)\), where

\[
h=h_0+h_1z+h_3z^3+h_4z^4+h_6z^6+h_7z^7.
\]

Take the universal exact lift of this symbol from that verifier, and add
\(kQ^2\). Let \(f_2\) denote its quadratic coefficient after the straight
substitution \(u=A\ell,v=B\ell\). The actual coefficient on the
canonical triple is \(f_2-h\gamma_U\). This expression is independent
of the polynomial Bezout gauge: the second correction has normal kernel
coordinate exactly \(-\gamma_U\).

Introduce the two linear expressions

\[
E_0=4a_0^2h_6-2a_0b_2h_3+b_2^2h_0,
\qquad
E_1=4a_0^2h_7-2a_0b_2h_4+b_2^2h_1.
\]

The coefficients of \(f_2-h\gamma_U\) at degrees four and one are
\(-b_2E_0/8\) and \(-a_0E_0/4\). The coefficients at degrees five and
two are \(b_2E_1/8\) and \(a_0E_1/4\). Since \((a_0,b_2)\ne(0,0)\),
vanishing requires \(E_0=E_1=0\). These two equations have rank two
on the entire coprime locus and are equivalent to

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4).
\]

With this substitution the only remaining condition is

\[
k=4a_0a_2c_3+2a_1b_2c_1.
\]

For explicit coefficient checking, before that substitution the remaining
coefficients at degrees six, three, and zero are respectively

\[
\frac{b_2}{4}
 (4a_0a_1h_7-4a_0a_2h_6-2a_1b_2h_4+b_2k),
\]

\[
\frac12(4a_0^2a_1h_7-4a_0^2a_2h_6-2a_0a_1b_2h_4
 -2a_0a_2b_2h_3+2a_0b_2k-a_1b_2^2h_1+a_2b_2^2h_0),
\]

\[
-a_0(2a_0a_2h_3-a_0k+a_1b_2h_1-a_2b_2h_0).
\]

It follows that the quartic space has dimension four. The four products
\(xT,yT,ZT,WT\) are linearly independent, contain the triple, and span
it. Therefore

\[
\boxed{
H^0(\mathcal I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).
}
\]

The assertion already holds for the primitive triple; imposing the fourth
layer cannot produce an irreducible quartic carrier. In particular, every
quartic containing a primitive quadruple on this fourth-obstruction zero
locus has the same cubic factor. This supplies a carrier exclusion once
the numerical filtration of a hypothetical complete intersection forces
that primitive triple. It does not exclude multiple structures whose
third layer has nonzero defect.

### 4. A sample fifth obstruction vanishes, with no STCI implication

For \(A=z^2+1,B=-2z\), the first-chart correction coefficients through
degree four are all zero. On the second chart the successive primitive
equation coefficients are

\[
\gamma_V=4+8w^2+3w^4,
\]

\[
\rho_V=-18w-50w^3-39w^5-9w^7,
\]

\[
\tau_V=102w^2+360w^4+\frac{1695}{4}w^6
                   +\frac{405}{2}w^8+\frac{135}{4}w^{10}.
\]

The successive moving-coordinate Laurent cocycles are

\[
h_2=-4z^{-1}-8z^{-3}-3z^{-5},
\]

\[
h_3=18z^{-7}+50z^{-9}+39z^{-11}+9z^{-13},
\]

\[
h_4=-102z^{-13}-360z^{-15}-\frac{1695}{4}z^{-17}
                         -\frac{405}{2}z^{-19}-\frac{135}{4}z^{-21}.
\]

Thus \(h_3\) has no Laurent terms \(z^{-1},\ldots,z^{-5}\), and
\(h_4\) has none of \(z^{-1},\ldots,z^{-10}\). The sample extends to a
primitive quintuple, uniquely at these two extension steps. The displayed
second-chart coefficients are the exact Laurent splittings:
\(\rho_V=-z^6h_3\), \(\tau_V=-z^{11}h_4\), written in \(w=1/z\).
In computing \(h_4\), both \(\gamma_V\) and \(\rho_V\) are evaluated at
the full moving coordinate \(W\) before truncation.

Its distinguished cubic is

\[
T=x^2Z-2y^2Z+2xyW-y^3.
\]

An exact restriction of the full eighteen-dimensional quartic space to
the first-chart embedding \(u=(z^2+1)\ell,v=-2z\ell\), modulo
\(\ell^4\), has rank fourteen and kernel
\(\langle xT,yT,ZT,WT\rangle\). Each of these products restricts
identically to zero in this sample; \(Q^2\) does not contain its triple.

### 5. Scope and pitfalls

The scalar \(q_0\) in the cubic conormal symbol is a section of \(O(3)\),
and it vanishes at points. The cubic is therefore not a surface smooth
along the entire curve. For the sample \(q_0=2\) on the first affine
chart, its homogeneous divisor is three times the point at infinity.
In the chart \(W=1\), the cubic has leading term \(2xy\) at that point,
so it is singular there. The primitive extensions and the cubic factor
are entirely compatible with the existing exclusion of characteristic-zero
STCI presentations on cubic surfaces.

No arbitrary \(\operatorname{GL}_2\) change of the split normal frame,
nor arbitrary base \(\operatorname{PGL}_2\) change, may be used to
normalize the binary quadratic pencil while keeping the nonlinear
transition fixed. Such transformations require transport of the full
embedded jet. The ambient symmetries visibly preserving \(C_0\) include
the torus and the coordinate-reversing involution; these alone do not
identify every coprime quadratic pair.

The fifth-order sample is an exact calculation for one quotient. It
establishes neither a universal fifth-order vanishing statement nor
algebraizability of an infinite formal surface. The universal quartic
carrier identity, in contrast, was derived with symbolic coefficients and
uses only the coprimality-open condition. All conclusions in this note are
stated in characteristic zero; special positive characteristics require
their own coefficient and denominator checks.


---

<a id="2026-10-06-localcoh-e2-incidence-charts"></a>

## Four pure-top charts for degree-two ancestor incidence

**Exact specification; full ancestor locus unresolved.** The completed quartic-mate theorem does not compute this ancestor locus.
The companion `localcoh-e2-incidence-2026-10-06.py` exports actual
two-target equations from the verified tensor. This reduces the 30 free
ancestor coordinates while retaining all allowed degeneration of the cyclic
inverse system at its top-symbol zero.

Use the 32-by-30 top map \(M\), of rank 29, and its three-row annihilator
\(L\). For a primitive homogeneous quadratic normal-dual direction
\(\nu=(p,r)\), the pure cubic top is

\[
c_i(t)=h(t)p(t)^i r(t)^{3-i},\qquad i=0,1,2,3,
\]

in the residue divided-power coordinates, where \(h=h_0+h_1t\) is
nonzero. The three equations \(Lc=0\) express precisely that this top lifts
to the 30-dimensional \(H^0(T_4(-7))\) space. They do not assert that its
annihilator quadruple is primitive at the zero of \(h\).

Select 29 independent columns of \(M\) and 29 independent rows of that
column submatrix. Inverting their rational square matrix gives a fixed
rational right inverse \(R\) on \(\operatorname{im}M\). Thus, on the
three-equation top-image locus, every ancestor is uniquely

\[
\alpha=Rc+\lambda k,
\]

where \(k\) spans the one-dimensional \(T_3(-7)\) kernel. The exporter
retains \(\lambda\) and contracts the entire actual quartic multiplication
tensor with these ancestor coordinates.

Primitivity forces at least one of \(p(0),r(0)\) nonzero. Normalize that
coordinate to one. Scaling the ancestor normalizes either \(h_0=1\) when
\(h_0\ne0\), or \(h=t\) when \(h_0=0\). Hence four charts cover every
primitive degree-two ancestor candidate:

| Direction normalization | Top coefficient |
| --- | --- |
| \(p(0)=1\) | \(h=1+h_1t\) |
| \(r(0)=1\) | \(h=1+h_1t\) |
| \(p(0)=1\) | \(h=t\) |
| \(r(0)=1\) | \(h=t\) |

For each chart the exporter writes the three top-image equations and the
74 multiplication equations for each target. The full two-target systems
have 43 variables on the first two charts and 42 variables on the last two:
five free direction coefficients, one optional coefficient \(h_1\), the
one lower correction, and 36 multiplier coefficients. Depending on zero
equations the stored generator count is smaller than 151. A one-target
version is exported as well.

If a computation returns a nonempty closed locus, primitive degree two
requires the homogeneous resultant \(\operatorname{Res}(p,r)\ne0\).
The exported systems do not discard this open condition or pretend that
all their lower-degree boundary directions are primitive degree two. A
unit ideal for the larger chart would suffice for exclusion; a non-unit
ideal requires inspecting this open locus and retaining the rank conditions
in `2026-10-06-localcoh-incidence.md`.

Two direct Gröbner attempts on the \(p(0)=1\) charts were interrupted
after a bounded run on Oct6 without an ideal result. The equations remain
available for continuation. A second run with multiline input and live
terminal output reached the 145-generator ideal on the \(h=t\) chart;
no full-locus conclusion is obtained merely from its progress.

The separate uniform parity certificate excludes the full primitive family
\((p,r)=(a_0+a_2t^2,b_1t)\), whose top coefficient is necessarily the
constant line. It is a verified sublocus of these general charts, not a
classification of all quadratic directions. All other non-ruling direction
strata remain research obligations.
