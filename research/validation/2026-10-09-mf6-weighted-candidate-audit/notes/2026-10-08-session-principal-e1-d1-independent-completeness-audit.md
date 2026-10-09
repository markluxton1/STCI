# Independent completeness audit of principal e1,d2=1 quartic ancestors

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic zero.
Scope: the principal `a0*b1!=0` direction lane for a genuine second defect
of degree one, in the accepted canonical-triple reduction for common
quartic ancestors. This audit combines the complete open-frame proof
with fresh all-35-column boundary calculations. No canonical frontier
file is edited.

**ACCEPTED, with the recorded antecedents:** no quartic common ancestor
for the independent fixed targets u,v has such a canonical triple. The
complete quartic fibre has dimension one throughout the declared open
and at its remaining genuine boundary points, except the node
`(p,r)=(2,1/2)`. The node has dimension four with a fixed cubic factor
and is excluded for ancestors by P-037. A literal uniform dimension-one
claim on the entire principal lane would be false.

This is an ancestor exclusion. A dimension-one containing-quartic space
does not by itself prohibit that single quartic from having an STCI mate
of some other degree. No all-mate carrier theorem is inferred here.
Other e-strata, second-defect degrees, higher multipliers, positive
characteristic, and the universal problem retain their separate scopes.

## 1. Parameter and triple coverage

For `b0!=0`, common direction scaling and the actual ambient torus give
the representative

```text
A=1+r*z, B=1+p*z,
p!=0, p-r!=0,
H=8p^3-(64r^2+128r+16)p^2
 +(96r^4+512r^3+592r^2+128r+6)p
 -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9)=0.
```

Here p nonzero is the principal condition and p-r nonzero is basepoint
freedom of the homogeneous linear direction pair. No arbitrary change
of the support coordinate or conormal frame is used to normalize it.
The accepted quadratic cocycle has coordinates c1,c2,c3 with
`H=64(c1*c3-c2^2)`. Its linear killing-section matrix is
`[[c1,c2],[c2,c3]]`.

Away from c1 zero the unique defect section is

```text
delta=-8c2+8c1*z=(2r+1)(8p+12r^2+4r+3)-p*P*z,
P=2p+12r^2+16r+9,
Gamma=the polynomial part of delta*h2.
```

The correction is unique because `H0(O(-4+d2))=H0(O(-3))=0`.
On pP nonzero, the z coefficient of delta is nonzero, so its homogeneous
degree-one section has no infinity zero. The exact resultant
`Res_z(delta,Gamma)=p^4*P^4/8` proves flatness at its finite zero.
Repeated-root assumptions do not enter this argument.

If c1=c2=0 and c3 nonzero, the correct alternative killing section is
`delta=1` in the finite chart, a homogeneous section with its zero at
infinity. It must not be replaced by the identically zero expression
`-8c2+8c1*z`. The boundary source explicitly makes this switch. The
surviving c3 gives the nonzero opposite-chart correction at that zero;
its negative has norm 24 over the quadratic field on the two affected
fibres. Thus these fibres are retained rather than deleted by the
generic choice of killing section.

The actual projective coordinate change was independently checked.
The raw reversed-chart normals have linear transition
`(Uraw_inf,Vraw_inf)=z^-7*(V/2,2U)`. Taking
`Uop=Vraw_inf/2,Vop=2Uraw_inf` gives the balanced opposite chart
`x3=1,x2=w,x1=w^3+2Uop,x0=w^4+Vop/2+3wUop` and the direction
`A_inf=r+w,B_inf=p+w`. The literal-form companion uses exactly this
chart. It computes `Gamma_inf=3w^2+(-6+3a)w+4/3-10a/3`, with
`a^2=-2`, by exact zero-remainder division of the actual quadratic
coefficient; its constant is `-c3`, of norm 24. This verifies genuine
flatness at infinity in the actual frame, beyond a finite-chart
resultant with constant delta.

The `b0=0` chart is also retained. Its weighted H equation specializes,
after scaling r to one, to
`p^3-8p^2+12p-72=0`. Before that scaling, r zero would force p zero,
contradicting the principal condition. These are exactly three geometric
points. The cubic has no root modulo five: its values at 0,1,2,3,4 are
`3,3,3,4,2`. Hence it is irreducible over QQ; its discriminant is
`-160704`, so the three characteristic-zero embeddings are distinct.
One exact cubic-field calculation therefore covers all three points.

## 2. Complete frame on the open

Put

```text
T=2p-4r^2-4r-1, S=p-2r-1, Q=12r^2+20r+11,
U={H=0, p*P*(p-r)*(2r-1)*T!=0}.
```

The audited open source reconstructs eighteen independent actual
quartics vanishing on C0. These forms contain no direction parameters;
their only free symbols are the four ambient coordinates. All 35
ambient quartic monomials restrict to
the seventeen distinct powers `z^0,...,z^16`; consequently the curve
restriction has rank 17 and these eighteen forms span the full ideal
space in degree four.

The actual first-normal matrix M1 has shape `11x18`. Its columns

```text
0,1,2,3,4,5,6,11,12,14,15
```

have the exact determinant

```text
D=p^4*(p-r)*(2r-1)*T^2/256.
```

The raw saved seven-column kernel N satisfies `M1*N=0`, and its rows
`7,8,9,10,13,16,17` are precisely the diagonal matrix `-D*I7`.
Thus M1 has rank eleven and N has rank seven in **every** fibre of U;
rank-nullity proves N is the complete kernel there. This statement
does not assume a generic nullspace specializes correctly. The new
independent countercheck reconstructs M1 from the actual quartic jets
and recomputes the determinant and the raw diagonal identities.

The source divides the seven columns by their recorded polynomial gcds.
Every divisor is a unit on U. Its normalized free determinant is
`-p^8*(2r-1)^6*T^11/2^52`. It then reconstructs the second contact map
from the exact condition `delta*q2-Gamma*h=0`. On H zero all but six
contact rows vanish, with the seventh row a multiple of H. The six
recorded row divisions use only p and p-r, also units on U. The resulting
`6x7` matrix is therefore the contact operator on the complete
first-normal kernel, without omitted quartics.

## 3. Two cofactors, their exact norms, and the nonunit S branch

The open verifier recomputes all seven actual maximal cofactors before
reducing modulo H, and checks their retained factorizations. The
cofactors omitting columns six and five have the shared prefactor

```text
(27/2^51)*p^5*(2r-1)^4*(2r+1)^3*S^3*T^7,
```

times the recorded residuals R6 and R5. The factor 2r+1 is also a unit
on U: `H(p,-1/2)=8p(p+2)^2` and `P(p,-1/2)=2(p+2)`, so every point
there violates pP nonzero. S is **not** a unit and is handled separately.

On S nonzero, if both cofactors vanished at a point of H, R6 and R5
would vanish. Their two resultants in p would both vanish at its r
coordinate. The exact resultant gcd is, up to a nonzero rational scalar,

```text
(2r-1)^16*(2r+1)^26*Q^5.
```

The r-half fibres have already been removed on U. Q has discriminant
`-128`, so it defines a quadratic field. Exact Euclidean polynomial
division at one root, together with an extended-Euclidean identity,
gives `gcd(H,R6,R5)=p-(2r+1)`; conjugation covers its other root.
But `P(2r+1,r)=Q`, so this common root violates P nonzero. Therefore
the two cofactors cannot vanish simultaneously on this part of U.
Leading-coefficient specializations of a resultant can only add
possible exceptional r values; they cannot conceal a finite common
root. The exact gcd and field-fibre calculation remove those possible
extras rather than assuming generic resultant sufficiency.

The entire S-zero branch is retained using

```text
H(2r+1,r)=-(2r-1)^2*(2r+1)*(6r+1)*Q,
P(2r+1,r)=Q.
```

Only `r=-1/6,p=2/3` survives the U conditions. Its actual cofactor
omitting column four is
`1073741824/36472996377170786403`, nonzero. The independent countercheck
also verifies the full first/contact matrix in the eighteen-dimensional
ideal space has rank 17 there. Consequently the contact rank is six
everywhere on U, and the complete containing-quartic space has dimension
`18-11-6=1`.

## 4. Exhaustive complement and fresh ambient boundary evidence

The independent countercheck verifies the precise polynomial identities

```text
H|P=0=-9*(2r+1)^2*Q^2,
H|T=0=-9*(2r-1)^2*(2r+1)^4,
H(p,1/2)=8*(p-8)*(p-2)^2,
H(p,-1/2)=8*p*(p+2)^2.
```

Thus the entire valid complement of U in the b0-nonzero principal chart
consists of the two r-half points and the two Q-root points with
`p=2r+1`, together with the primitive point `p=-2,r=-1/2`. The p-zero
case is nonprincipal; p=r violates basepoint freedom. At the primitive
point all c_i vanish. Its unique primitive correction multiplied by
any degree-one defect shares the zero of that defect, and there is no
additional `H0(O(-3))` correction. It cannot be a genuine positive-defect
finite-flat triple, as in the accepted defective-triple module argument.

The boundary verifier recomputes all 35 ambient monomial columns from
scratch, imposing curve restriction, first normal vanishing, and the
quadratic contact condition in the appropriate exact field. It does
not specialize N at a frame boundary. It asserts the expected ranks
and verifies the complete nullspace, not just a supplied form.

| Genuine parameter fibre | Full 35-column rank | Quartic dimension |
|---|---:|---:|
| `r=1/2,p=2` | 31 | 4, fixed cubic times every linear form |
| `r=1/2,p=8` | 34 | 1 |
| `Q=0,p=2r+1`, both roots, `delta=1` | 34 | 1 |
| `b0=0`, all three cubic-field points | 34 | 1 |
| `r=-1/6,p=2/3` within U, independent frame cross-check | 34 | 1 |

At the node, the four normalized quotient linear forms after dividing
the common cubic C are `x0,x1,x0+x1/2+x2/2,x3`. They span the complete
four-dimensional linear space. If `F*alpha=u,G*alpha=v`, then
`F=C*L,G=C*M` would yield a common ancestor `C*alpha` with linear
multipliers L,M. It is nonzero because u is nonzero, contradicting the
all-stage P-037 theorem. Elsewhere the two quartics would be proportional
in their dimension-one space, contradicting target independence.

These arguments exhaust the principal direction lane for the stated
ancestor problem. They neither decide a higher-degree mate for one
unique carrier nor use an STCI-only second-defect bound.

## 5. Evidence and reproducibility

The open theorem and source are preserved in
[the source-owner's detailed proof](2026-10-08-session-mf6-principal-rank-open-independent-audit.md)
and
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](../computations/verify_session_mf6_principal_rank_open_2026_10_08.py).
Its frozen source hash is
`2fbefebda6723b7d721f0034c0167a2c70a3b79eed01675b99baf453453a9ac8`.
The source owner observed the complete final run exit zero in 82.912
seconds. This audit inspects its reconstruction and exact proof logic
and independently recomputes the frame and coverage checks; it does not
count that owner's run as a second auditor execution.

The fresh
[`coverage-countercheck.py`](../validation/2026-10-08-principal-e1-d1-audit/coverage-countercheck.py)
completed exit zero. Its
[`result`](../validation/2026-10-08-principal-e1-d1-audit/coverage-countercheck-result.json)
binds the actual contact input and source hash, determinant, diagonal,
complement identities, opposite-correction norm, cubic irreducibility,
and S-zero rank. It does not invoke an existing verifier or regenerate
proof inputs.

The frozen all-35-column
[`boundary source`](../computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py)
has hash
`9d485f208f61afc495e43bd62054651df37e65c297534ca9930033c44bfea53e`.
Its exact bytes were replayed with `--scope all` in an isolated snapshot;
the run exited zero, and the output and all five field calculations are
retained separately. The actual two-chart
[`residue source`](../computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py)
was also replayed from exact bytes, with source hash
`02fac92723ff5b5b29c6024e49d8706e4ffe7445431e55cd1761030adaa6dcdb`.
It exited zero. The independent
[`residue-input-comparison.py`](../validation/2026-10-08-principal-e1-d1-audit/residue-input-comparison.py)
then bound all three literal quartics, direction parameters, cocycles,
defect sections and finite corrections to the fresh complete-35-column
output, and derived the raw normal transition from the actual coordinate
change. Its exact checks also passed. The companion's cubic-pole outputs
are separate necessary bounds; they do not strengthen this audit into
an all-mate carrier exclusion.
The complete source/input closure, copied open-proof result/transcript,
fresh boundary and residue results/logs, and both countercheck hashes are in
[`audit-manifest.json`](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
The snapshot preserves the required `research/computations` and
`research/scratch` layout, so the open proof can also be replayed there.

The source-owner note preserves three earlier checker repairs: one
incorrect free-determinant denominator and two structural-expression
comparisons. The frozen source uses `2^52` and exact expanded polynomial
differences. No altered failed source is treated as passing mathematics.
