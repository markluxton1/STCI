# Toric quintic centers: full inverse support and the remaining incidence

Status: **independently reviewed partial exclusion**, with
an unfinished final parameter locus. Fix the embedded rational quartic
`C0=[u^4:u^3v:uv^3:v^4]` over an algebraically closed field of characteristic
zero. This closes out the calculation already in progress; it does not
exclude every toric quintic normalization or settle unrestricted STCI.

## 1. Geometric object and scope

The [marked-source proof, §§4.1–4.2](quintic_non_gorenstein_toric_sources.md)
reduces every hypothetical toric quintic normalization, together with its
marked quartic, to the normal surface in P4

    X: BD-C^2 = AEC-D^3 = ABE-CD^2 = 0,
    c(t)=(t,t^3(t+1),t^2(t+1),t(t+1),(t+1)^2).

The marked curve includes its projective point at infinity. There is an
actual section `q in H0(X,4H)` with `div(q)=5c`; every possible mate pulls
back to a power of q. A projection must be finite and birational and map
c isomorphically to fixed C0. An extra point of X outside c mapping into
C0 prevents every such power from descending. This is a full inverse-support
test, not a count of a residual curve in an ambient intersection. The
[fixed-carrier criterion](../results/fixed_carrier_conductor_criterion.md)
supplies the implication to every mate degree.

The possible centers preserving the marked image form the PGL2 orbit of
the missing-middle-coordinate center of the rational normal quartic.
A finite distinct pair and a one-infinity pair cover this orbit. Coincident
pairs lie on c and are inadmissible centers. We test all admissible centers
in these charts, without replacing exceptional parameters by a generic one.

## 2. Finite-pair chart and certified exclusions

For distinct finite r,q put `m=r+q`, `n=rq`, `Delta=m^2-4n !=0`.
The source center `P=(a,b,c,d,e)` is

    a=3mn, b=3(m+2), c=m^2+2n+3m,
    d=m^2+2n+3mn, e=m^2+2n+6mn+6n^2.

Here c in this coordinate list is a scalar, not the marked curve. Set

    K=bd-c^2=-Delta*K0,   K0=m^2-n+3m+3,
    h(t)=dt^2-2ct+b,      D(t)=t(t+1)h(t).

On the fiber line `c(t)+lambda P`, the quadric equation is
`lambda(D+lambda K)=0`. For K nonzero the nonmarked branch is
`lambda=-D/K`. The residual polynomial W is preserved by its six exact
coefficients in the [finite-center input](../computations/quintic_toric_finite_centers.json),
produced by the [finite-center certificate](../computations/quintic_toric_finite_centers.py).
It satisfies

    W_5=d*N, W(0)=K0*U0, W(-1)=-K0*V1*V2,
    Res_t(W,h)=Delta^4*d^2*K0^3*M,   R(P)=-Delta*N,

where

    N=m^4+6m^3n+9m^2n^2+m^2n+9mn^3-6mn^2-2n^2,
    U0=m^4+4m^2n+4n^2+3m^3+6mn+3m^2-12n,
    V1=m^2+2n+6m+6,
    V2=m^2+2n+6mn+6n^2,
    M=11m^4+15m^3n+36m^3+21m^2n^2+8m^2n+39m^2
      +9mn^3+30mn^2-45mn+27m+6n^3+8n^2-30n+18.

The geometric meaning of a root of W outside `D=0` is an actual extra
inverse point: the resulting lambda is nonzero and all three equations
of X vanish. Thus `d*N*U0*V1*V2*M !=0` excludes full inverse support.
The factor M is essential; an earlier diagnostic omitted it and was
corrected before acceptance.

The following boundary arguments are also certified.

| Parameter locus | Actual reason for exclusion |
| --- | --- |
| `K=0` | `n=m^2+3m+3`. For `m != -1,-2`, take `t=1/(m+1)` and `lambda=-t^2(t+1)/c`; the resulting point has B=C=D=0 and lies on X outside c. The diagonal case m=-2 is inadmissible. At `(m,n)=(-1,1)`, take t=0 and lambda=-1/3, obtaining `[1:-1:0:0:0]`. |
| `K !=0, d !=0, N=0` | At the marked point at infinity, `Q=lambda(d+lambda K)` and `R=lambda^3 R(P)`. The nonzero root `lambda=-d/K` also satisfies T by the toric syzygy, giving an extra point. |
| `K !=0, d=0` | Substitute `n=-m^2/(3m+2)`. W has degree four on the retained locus. Full support would require `W | D^5`. The remainder-coefficient numerator gcd is `243(m+2)^5`, whose only root is diagonal. All denominator zeros are outside the retained locus. |

After these tests, the initially certified remaining finite locus is

    Delta*K0*d*N !=0,   U0*V1*V2*M=0.                 (1)

## 3. The entire one-infinity boundary is excluded

Here

    P(r)=(3r,0,1,1+3r,1+6r+6r^2), K=-1,
    h=(1+3r)t^2-2t, D=t(t+1)h.

The [boundary certificate](../computations/quintic_toric_boundary_centers.py)
uses exact identities on `lambda=D`:

    (R/lambda)=t(t+1)W_b[1-(3r+1)t],
    (T/lambda)=-t^2(t+1)W_b.

The polynomial W_b has constant coefficient one, leading coefficient
`(3r+1)(9r^3+9r^2+6r+1)`, value
`W_b(-1)=-(6r^2+6r+1)`, and resultant with h equal to
`(3r+1)^2(9r^3+21r^2+15r+11)`. Away from these four parameter factors,
any root supplies an extra point. The complete exceptional tests give:

| Parameter factor | Degree of W_b | Degree of gcd(W_b,D^5) |
| --- | ---: | ---: |
| `3r+1` | 4 | 0 |
| `9r^3+9r^2+6r+1` | 4 | 0 |
| `6r^2+6r+1` | 5 | 1 |
| `9r^3+21r^2+15r+11` | 5 | 1 |

Each factor is irreducible over Q and the factors are pairwise coprime;
the exact number-field computations therefore cover every conjugate
parameter in characteristic zero. The strict degree inequality supplies
an extra root in every case. The support test uses D^5 rather than D,
so repeated roots are retained.

The projective marked endpoint was separately checked with fiber coordinates
`(3rz,1,z,(1+3r)z,(1+6r+6r^2)z)`. It has an extra point when
`9r^3+9r^2+6r+1=0`; at r=-1/3 the fiber is a double point supported
on c. The limiting center r=infinity is `[0:0:0:0:1]` on X and is
inadmissible. These endpoint checks do not replace the finite-t argument.

## 4. Three exceptional curves and the uncompleted locus

For nonzero W in characteristic zero, the exact elementary criterion is

    Supp V(W) subset Supp V(D)  iff  W divides D*W'.     (2)

At a root of multiplicity e, W' has order e-1. This explains both
necessity and sufficiency and why characteristic zero matters; it is
not a characteristic-independent support certificate.

The [three-curve calculation](../computations/quintic_toric_exception_centers.py)
uses (2) on U0, V1 and V2. The independent source closeout review **passes**:
all three curves are excluded on `Delta*K0*d*N !=0`. It supplies the
[separate specialization audit](../computations/quintic_toric_exception_audit.py)
and the following complete evidence, rather than inferring coverage from a
generic remainder.

Write the source equations on the fiber line as R and T, distinguishing
the coordinate D of P4 from the polynomial D(t). The exact identities are

    K^2 (R/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(dt-c),
    K^2 (T/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(ct-b).

The two linear cofactors have resultant `c^2-bd=-K !=0`. Thus the
specialized residual gcd after the universal endpoint factors is exactly
W up to a unit at every retained point, not only generically.

The parameterizations and numerator-gcd tests are:

| Curve | Parameterization | Gcd of numerator coefficients of rem(D W',W) |
| --- | --- | --- |
| V1 | `m=k, n=-(k^2+6k+6)/2` | `81(k+2)^4` |
| V2, m nonzero | `m=-2k/q, n=km`, `q=6k^2+6k+1` | `81(2k+1)^4(10k^2+6k+1)` |
| U0, m nonzero | `m=-12(k+3)/p`, `x=6+(k-3)m/2`, `n=(x-m^2)/2`, `p=k^2+27` | `139968(k-3)^3(k+3)(k^2-12k+63)` |

Every root of these gcds has Delta=0 or K0=0. The V1 graph is complete.
For V2 with m nonzero, k=n/m gives `mq+2k=0`; q=0 would also force k=0,
so its poles give no affine center. The m=0 points are `(0,0)`, excluded
by Delta, and `(0,-1/3)`, whose separately computed remainder has
coefficient-numerator gcd 800 and is nonzero. For U0 put
`x=m^2+2n`, `y=2x+3m-6`; then
`y^2+27m^2+36m-36=4U0`. With m nonzero, `k=(y-6)/m` gives
`pm+12(k+3)=0`. Its poles again give no finite center. The two m=0
points are `(0,3)` with K0=0 and `(0,0)` with Delta=0.

For explicit denominator coverage, define

    A1=k^2+4k+2,
    B1=k^6+14k^5+78k^4+212k^3+276k^2+144k+8,
    A0=k^3-3k^2+99k+135,
    B0=k^9+3k^8+144k^7+648k^6+15066k^5-30618k^4
       +577368k^3-1714608k^2-6528195k+27497151.

| Curve | Leading coefficient of W (dN) | Common denominator of canceled remainder coefficients, up to rational units |
| --- | --- | --- |
| V1 | `27(k+2)^2 A1 B1/16` | `8 A1 B1^3` |
| V2 | `1728 k^10(2k+1)^2/q^6` | `k^3 q^8` |
| U0 | `5038848(k-3)^2 A0 B0/p^10` | `p^10 A0 B0^3` |

All additional denominator zeros lie on dN=0, on an excluded Delta=0
point, or at parameter poles with no affine center. W therefore has
degree five throughout the retained open set, division commutes with
specialization there, and no degree-drop point was silently omitted.

The remaining finite incidence is consequently

    M=0, Delta*K0*d*N*U0*V1*V2 !=0,
    W divides h*W'.                                      (3)

The omitted t(t+1) factor in (3) is invertible on Supp(W), by the
nonzero U0,V1,V2 conditions. The infinity fiber is already controlled
by N nonzero. The quadratic h has two distinct roots, since its
discriminant is `4(c^2-bd)=-4K !=0`. Thus (3) is equivalently

    W=gamma*(t-alpha)^j*(t-beta)^(5-j), j=0,...,5,

where alpha,beta are those two roots and gamma is nonzero. Up to their
exchange there are three multiplicity patterns, 5+0, 4+1 and 3+2.
Geometrically all five residual-polynomial roots would have to coalesce
at the two parameters where the nonmarked branch returns to the marked
point. These are candidate full-support configurations, not demonstrated
centers or residual components downstairs. This is a useful formulation
for a later bounded test, not a completed classification of (3).

The unfinished M calculation must be kept separate. A previous scratch
run formed the remainder of D W' modulo W, found coefficient numerators
of degree 22 and their scalar gcd with M equal to one, then stopped
before the multivariate Groebner calculation completed. The process was
cancelled at the user's earlier closeout request. A gcd of one in two
variables proves neither an empty common zero locus nor finiteness.
There is no certified classification of M, no surviving admissible center,
and no STCI construction from this calculation. The temporary unfinished
program has no continuing consumer; the exact input W and condition (2)
preserve the mathematical question.

## 5. Exact evidence and integration scope

The proof and five exact support files are selectively preserved from commit
`61290bdf906aa419c9542732f32fdcc34ba338a1`. The finite chart, boundary,
three exceptional curves and specialization audit keep their original formulas
and characteristic-zero hypotheses. This integration makes no new mathematical
deduction. Independent preservation and scope
review passed without a material finding, by direct comparison to the fixed
source and all five exact support files. This review made no fresh CAS replay;
the unchanged source arguments retain the reviews described below.

The independent source implementation review checked the finite chart and
corrected one-infinity calculation and executed them with Python 3.15.2 /
SymPy 1.14.0, exit zero. The retained finite copy differed only in execution
metadata and removal of an unused no-op; the boundary copy was byte-identical
to that reviewed version. The support lemma (2) separately received mathematical
reconstruction. A fresh independent closeout review reconstructed the final
written §§1–4, including the K=0 points, universal residual-factor identities,
parameter coverage, denominator and leading-coefficient specializations, endpoints
and exact remaining multiplicity patterns. It found no material correction.
That reviewer executed the retained three-curve program and retained independent
specialization audit with Python 3.15.2 / SymPy 1.14.0, both exit zero; the
latter ended in PASS. No M-locus calculation was performed or certified.

| Exact retained support | SHA-256 |
| --- | --- |
| [Finite-center program](../computations/quintic_toric_finite_centers.py) | `091e9b878f2dbb3b4cca64cac3e366449111dc26305936a13330da516ba05e80` |
| [Finite-center JSON input](../computations/quintic_toric_finite_centers.json) | `924bc8245c2b9cbee76f98862e7e304e9aecb32c4d2a96279666734f10a5b6ec` |
| [One-infinity boundary program](../computations/quintic_toric_boundary_centers.py) | `6de86103d9539039366cee0d99693b06f7d2eed511dad4566bb5233ac6a420b5` |
| [Three-curve program](../computations/quintic_toric_exception_centers.py) | `46a86f93c6aec48a8a79ec897bb60203d226cb27a263435cb4dfae863208016f` |
| [Independent specialization audit](../computations/quintic_toric_exception_audit.py) | `4d2b338367b09858427bcf8f036b5ffe64d39570bc9add8809198607618cdd00` |

The JSON preserves the six coefficients of W and the earlier four-curve gate
(1). Its remaining-incidence field describes that stage of the calculation;
§4 gives the later reviewed exclusion of U0,V1,V2. The JSON is an exact input,
not an independent statement that all four curves are still open. Both the
three-curve program and audit read the sibling JSON; no temporary input is
needed. The audit additionally prints the three-curve program's hash. The
finite and boundary programs are otherwise self-contained apart from SymPy
and the Python standard library.

For reproduction, use Python with SymPy and run these individual scripts from
`research/computations/`. This integration checks exact source-byte preservation
and dependencies; it does not claim a fresh CAS replay. The source closeout's
captured three-curve output SHA-256 was
`e11e46536605ea9153e71be7e52a06d1bd5cade48929368e06f17deee51fe94f`;
the specialization-audit output SHA-256 was
`5f0a79542fb6f4a95c7886108fbc81a4d8b6b4bf87c17bdb11a14cd90db563f6`.
These identify the source executions, not executions in this integration.

The result is a partial exclusion for the exhaustive toric quintic-source
reduction. It leaves (3) unresolved and does not imply a complete toric-quintic
exclusion, a classification of non-Gorenstein quintic normalizations, or an
unrestricted characteristic-zero STCI conclusion. Even a surviving full-support
center would still require actual descent of a pure power q^N through its
projection/conductor algebra.
